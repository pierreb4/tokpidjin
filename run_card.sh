#!/bin/bash

usage() {
  echo "Usage: $0 [-b] [-c COUNT] [-i] [-o] [-t TIMEOUT]"
  echo "  -b: Build solvers_*.py"
  echo "  -c: Count of tasks to run (default is all tasks)"
  echo "  -i: Initial run (removes old solvers)"
  echo "  -o: One run only (stops after one iteration)"
  echo "  -t: Maximum timeout for each run (default is 1.0 seconds)"
}

if [[ "$1" == "-h" || "$1" == "--help" ]]; then
  usage
  exit 0
fi

BUILD=
COUNT=
INITIAL=
ONERUN=
TIMEOUT=

while getopts "bc:iot:" opt; do
  case $opt in
    b) BUILD=true ;;
    c) COUNT="$OPTARG" ;;
    i) INITIAL=true ;;
    o) ONERUN=true ;;
    t) TIMEOUT="$OPTARG" ;;
    *) echo "Invalid option: -$OPTARG" >&2; usage; exit 1 ;;
  esac
done
shift $((OPTIND -1))

if [ -n "$INITIAL" ]; then
  echo "Initial run - removing old solvers"
  rm -rf solver_dir solver_md5 solver_def
  mkdir solver_dir solver_md5 solver_def
  rm -rf differ_dir differ_md5 differ_def
  mkdir differ_dir differ_md5 differ_def
  rm main.log
  # Gets unset for ONERUN
  # CARD_OPTION="-fs -fd"
  CARD_OPTION="-fd"
  python prep_solver_dir.py
fi

if [ -z "$COUNT" ]; then
  COUNT=0
fi

if [ -z "$TIMEOUT" ]; then
  TIMEOUT=1.0
fi

CHARS=({0..9} {a..f})

TMPFILE=$(mktemp)
TMPBATT="tmp_batt_${TMPFILE##*.}"
STOP=0
clear
while date && [ $STOP -eq 0 ]; do
  if [ "$COUNT" -ne 0 ]; then
    if [ -n "$ONERUN" ]; then
      echo "-- One run only --"
      unset CARD_OPTION
      TMPBATT="tmp_batt_onerun"
      STOP=1
    fi

    # So that tail can get started immediately
    touch ${TMPBATT}_run.log
    touch ${TMPBATT}_main.log

    # Remove old temporary files
    find . -maxdepth 1 -name 'tmp_batt_*' -mmin +120 -exec rm {} \;

    python card.py $CARD_OPTION -c 32 -f ${TMPBATT}_run.py
    # python card.py $CARD_OPTION -f ${TMPBATT}_run.py
    unset CARD_OPTION

    # Pick a random timeout between 0.1 and 0.5 * TIMEOUT
    # RND_TIMEOUT=$(echo "scale=2; $TIMEOUT * $((RANDOM % 10 + 1)) / 20" \
    #     | bc)
    # unbuffer timeout 900s python run_batt.py -i -t $RND_TIMEOUT -c 1200 \
    #     | tee batt.log

    # unbuffer timeout 3600s python run_batt.py -i -t $TIMEOUT -c $COUNT \
    #     -b ${TMPBATT}_run | tee ${TMPBATT}_run.log

    # Limit memory to 1GB
    mem_limit=$((1 * 1024 * 1024))
    ulimit -v $mem_limit &>/dev/null || echo "Memory limit not supported"
    # unbuffer timeout 300s python run_batt.py -i -t $TIMEOUT -c $COUNT \
    timeout 3600s python -u run_batt.py -i -t $TIMEOUT -c $COUNT \
        -b ${TMPBATT}_run
        # -b ${TMPBATT}_run | tee ${TMPBATT}_run.log
  fi

  # Remove results that are too large (for now)
  find solver_md5 -type f -size +10k -delete

  # Note: clean-up is down here too
  if [ -n "$BUILD" ]; then
    # python card.py -fs -fd -f ${TMPBATT}_main.py

    # # Limit memory to 1GB
    # mem_limit=$((1 * 1024 * 1024))
    # ulimit -v $mem_limit &>/dev/null || echo "Memory limit not supported"
    # unbuffer python main.py -t $TIMEOUT --solvers solvers_dir \
    #     -b ${TMPBATT}_main | tee ${TMPBATT}_main.log

    # (date +'%F %T'; grep "Found\|Summary" ${TMPBATT}_main.log) | tee -a main.log

    # >solvers_dir.py
    # echo -e "from dsl import *\nfrom constants import *\n\n" >>solvers_dir.py
    # # find solver_md5 -type f -name '*.py' -exec cat {} >>solvers_dir.py \; -exec echo >>solvers_dir.py \; -exec echo >>solvers_dir.py \;

    # TMP_SOLVER_NAME=$(mktemp)
    # for d in solver_dir/solve_*; do
    #   ls -v ${d}/[0-9]*/[0-9]*/[0-9]*/[0-9a-f]* | tail -1 >$TMP_SOLVER_NAME
    #   mapfile -t TO_SOLVER <$TMP_SOLVER_NAME
    #   if [[ -z "${TO_SOLVER[@]}" ]]; then
    #     echo "No solver for $d"
    #   else
    #     echo "Adding ${TO_SOLVER[0]} to solvers_dir.py"
    #     cat "${TO_SOLVER[0]}" >$TMP_SOLVER_NAME
    #   fi
    # done

    # rm $TMP_SOLVER_NAME

    # This should be a one-time thing after a change in replace_*.py

    # # From solvers_dir.py to solvers_yyy.py
    # python replace_func.py -q --input solvers_dir.py --output solvers_yyy.py
    # python list_solvers.py -q --input solvers_yyy.py >key_yyy.txt
    # # From solvers_yyy.py to solver_md5/
    # for k in `cat key_yyy.txt`
    # do python replace_arg.py -q --input solvers_yyy.py --output-dir solver_md5/ $k
    # done

    # find solver_dir -maxdepth 1 -type d -name 'solve_*' \
    #     -exec bash clean_solve.sh {} \;

    # # Remove .def files in solver_def if corresponding .py file does not exist in solver_md5
    # find solver_def -maxdepth 1 -name '*.def' -print0 | while IFS= read -r -d '' def_file; do
    #   base=$(basename "$def_file" .def)
    #   py_file="solver_md5/${base}.py"
    #   if [ ! -f "$py_file" ]; then
    #     echo rm "$def_file"
    #     rm "$def_file"
    #   fi
    # done

    # Remove empty sub-folders from solver_dir
    find solver_dir -type d -empty -delete

    RANDCHAR="${CHARS[RANDOM % ${#CHARS[@]}]}"
    NAME="*${RANDCHAR}.py"

    # Remove .py files in solver_md5 if corresponding file does not exist in ../solver_dir
    find solver_md5 -maxdepth 1 -name "$NAME" -print0 | while IFS= read -r -d '' py_file; do
      base=$(basename "$py_file" .py)
      if ! find solver_dir -type l -name "${base}.py" | grep -q .; then
        find solver_dir -name "${base}.py" || echo "No link for ${base}.py"
        echo rm "$py_file"
        rm "$py_file"
      fi
    done

    # # Remove differ_dir folders if corresponding .py file does not exist in solver_md5
    # find differ_dir -maxdepth 1 -type d ! -path differ_dir -print0 | while IFS= read -r -d '' dir_name; do
    #   base=$(basename "$dir_name")
    #   solve_file="solver_md5/${base}.py"
    #   differ_dir="differ_dir/${base}"
    #   if [ ! -f "$solve_file" ]; then
    #     echo rm -r "$differ_dir"
    #     rm -r "$differ_dir"
    #   fi
    # done

    # Note maxdepth 2, because of iz and zo sub-folders
    # find differ_dir -maxdepth 2 -type d -name 'solve_*' \
    #     -exec bash clean_solve.sh {} \;

    # # Remove .def files in differ_def if corresponding .py file does not exist in differ_md5
    # find differ_def -maxdepth 1 -name '*.def' -print0 | while IFS= read -r -d '' def_file; do
    #   base=$(basename "$def_file" .def)
    #   py_file="differ_md5/${base}.py"
    #   if [ ! -f "$py_file" ]; then
    #     echo rm "$def_file"
    #     rm "$def_file"
    #   fi
    # done

    # Remove empty sub-folders from differ_dir
    find differ_dir -type d -empty -delete

    RANDCHAR="${CHARS[RANDOM % ${#CHARS[@]}]}"
    NAME="*${RANDCHAR}.py"

    # Remove .py files in differ_md5 if corresponding file does not exist in ../differ_dir
    find differ_md5 -maxdepth 1 -name "$NAME" -print0 | while IFS= read -r -d '' py_file; do
      base=$(basename "$py_file" .py)
      if ! find differ_dir -type l -name "${base}.py" | grep -q .; then
        find differ_dir -name "${base}.py" || echo "No link for ${base}.py"
        echo rm "$py_file"
        rm "$py_file"
      fi
    done

    # # From solvers_ref.py to solvers.py
    # python replace_func.py -q
    # python list_solvers.py -q --input solvers.py >key_pre.txt
    # # From solvers.py to solver_pre/
    # for k in `cat key_pre.txt`
    # do python replace_arg.py -q --input solvers.py --output-dir solver_pre/ $k
    # done

    # # From solver_pre/ to solvers_pre.py
    # Old: python expand_solver.py -q --source solver_pre/ --solvers-file solvers_pre.py
    # SOLVER_PRE="solver_pre.py"
    # >$SOLVER_PRE
    # echo -e "from dsl import *\nfrom constants import *\n\n" >>$SOLVER_PRE
    # find solver_pre -type f -name 'solve_????????.py' -exec cat {} >>$SOLVER_PRE \; -exec echo >>$SOLVER_PRE \; -exec echo >>$SOLVER_PRE \;

  fi
done
