#!/bin/bash

usage() {
  echo "Usage: $0 [-i] [-o] [-b] [-t MAX_TIMEOUT]"
  echo "  -i: Initial run (removes old solvers)"
  echo "  -o: One run only (stops after one iteration)"
  echo "  -b: Build solvers_*.py"
  echo "  -t: Maximum timeout for each run (default is 1.0 seconds)"
}

if [[ "$1" == "-h" || "$1" == "--help" ]]; then
  usage
  exit 0
fi

INITIAL=
ONERUN=
BUILD=
MAX_TIMEOUT=

while getopts "iobt:" opt; do
  case $opt in
    i) INITIAL=true ;;
    o) ONERUN=true ;;
    b) BUILD=true ;;
    t) TIMEOUT="$OPTARG" ;;
    *) echo "Invalid option: -$OPTARG" >&2; usage; exit 1 ;;
  esac
done
shift $((OPTIND -1))

if [ -n "$INITIAL" ]; then
  echo "Initial run - removing old solvers"
  rm -r solver_dir/* solver_md5/* solver_def/*
  CARD_OPTION="-fs" 
fi

if [ -z "$TIMEOUT" ]; then
  TIMEOUT=1.0
fi

TMPFILE=$(mktemp)
STOP=0
clear
while date && [ $STOP -eq 0 ]; do
  if [ -n "$ONERUN" ]; then
    echo "-- One run only --"
    STOP=1
  fi

  python card.py $CARD_OPTION
  unset CARD_OPTION
  cp -f batt.py batt_run.py
  RND_TIMEOUT=$(echo "scale=2; $TIMEOUT * $((RANDOM % 10 + 1)) / 10" \
      | bc)
  unbuffer timeout 900s python run_batt.py -i -t $RND_TIMEOUT -c 1000 \
      | tee batt.log
  
  python card.py -fs
  cp -f batt.py batt_main.py
  unbuffer python main.py -t 2.0 --solvers solvers_dir \
      | tee main.log

  # Build solvers_*.py if requested
  if [ -n "$BUILD" ]; then

    # TODO Reactivate when we start replacements again
    #      Make more efficient

    >solvers_dir.py
    echo -e "from dsl import *\nfrom constants import *\n\n" >>solvers_dir.py 
    find solver_md5 -type f -name '*.py' -exec cat {} >>solvers_dir.py \; -exec echo >>solvers_dir.py \; -exec echo >>solvers_dir.py \;

    # This should be a one-time thing after a change in replace_*.py

    # # From solvers_dir.py to solvers_yyy.py
    # python replace_func.py -q --input solvers_dir.py --output solvers_yyy.py
    # python list_solvers.py -q --input solvers_yyy.py >key_yyy.txt
    # # From solvers_yyy.py to solver_md5/
    # for k in `cat key_yyy.txt`
    # do python replace_arg.py -q --input solvers_yyy.py --output-dir solver_md5/ $k
    # done

    for f in solver_dir/solve_*; do bash clean_def.sh $f; done

    # Remove .def files in solver_def if corresponding .py file does not exist in solver_md5
    find solver_def -maxdepth 1 -name '*.def' -print0 | while IFS= read -r -d '' def_file; do
      base=$(basename "$def_file" .def)
      py_file="solver_md5/${base}.py"
      if [ ! -f "$py_file" ]; then
        rm "$def_file"
      fi
    done

    # Remove .py files in solver_md5 if corresponding file does not exist in ../solver_dir
    find solver_md5 -maxdepth 1 -name '*.py' -print0 | while IFS= read -r -d '' py_file; do
      base=$(basename "$py_file" .py)
      if ! find solver_dir -type l -name "${base}.py" | grep -q .; then
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
