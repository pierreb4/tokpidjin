#!/opt/homebrew/bin/bash

MAX_TIMEOUT=$1
BUILD=$2
TMPFILE=$(mktemp)

clear
while date; do 
  python card.py -p
  python main.py -t $MAX_TIMEOUT --solvers solvers_dir | tee main.log

  python card.py
  RND_TIMEOUT=$(echo "scale=2; $MAX_TIMEOUT * $((RANDOM % 10 + 1)) / 10" | bc)
  timeout 900s python run_batt.py -t -to $RND_TIMEOUT -c 1000 | tee batt.log

  # bash count_solvers.sh solver_dir
  
  # TODO Maybe work on md5 solvers?
  # Also think about removing old files
  # Can hardlinks solve both things?

  # If we got a third option, build solvers_*.py
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
