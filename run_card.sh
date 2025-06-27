#!/opt/homebrew/bin/bash

BUILD=$1

clear
while date; do 
  python card.py
  python run_batt.py

  bash count_solvers.sh solver_dir
  
  # TODO Maybe work on md5 solvers?
  # Also think about removing old files
  # Can hardlinks solve both things?

  # If we got a third option, build solvers_*.py
  if [ -n "$BUILD" ]; then
    # From solvers_dir.py to solvers_yyy.py
    python replace_func.py -q --input solvers_dir.py --output solvers_yyy.py
    python list_solvers.py -q --input solvers_yyy.py >key_yyy.txt
    # From solvers_yyy.py to solver_dir/
    for k in `cat key_yyy.txt`
    do python replace_arg.py -q --input solvers_yyy.py --output-dir solver_dir/ $k
    done
    # From solver_dir/ to solvers_dir.py
    python expand_solver.py -q --source solver_dir/ --solvers-file solvers_dir.py

    # From solvers_ref.py to solvers.py
    python replace_func.py -q
    python list_solvers.py -q --input solvers.py >key_pre.txt
    # From solvers.py to solver_pre/
    for k in `cat key_pre.txt`
    do python replace_arg.py -q --input solvers.py --output-dir solver_pre/ $k
    done
    # From solver_pre/ to solvers_pre.py
    python expand_solver.py -q --source solver_pre/ --solvers-file solvers_pre.py
  fi

done
