#!/opt/homebrew/bin/bash

TIMEOUT=$1
BUILD=$2
TMPFILE=$(mktemp)

clear
while date; do 
  python card.py
  python run_batt.py -t -to $TIMEOUT

  bash count_solvers.sh solver_dir
  
  # TODO Maybe work on md5 solvers?
  # Also think about removing old files
  # Can hardlinks solve both things?

  # If we got a third option, build solvers_*.py
  if [ -n "$BUILD" ]; then

    # TODO Reactivate when we start replacements again
    #      Make more efficient

    # # From solvers_dir.py to solvers_yyy.py
    # python replace_func.py -q --input solvers_dir.py --output solvers_yyy.py
    # python list_solvers.py -q --input solvers_yyy.py >key_yyy.txt
    # # From solvers_yyy.py to solver_dir/
    # for k in `cat key_yyy.txt`
    # do python replace_arg.py -q --input solvers_yyy.py --output-dir solver_dir/ $k
    # done

    for f in solver_dir/*; do bash clean_def.sh $f; done

    # From solver_dir/ to solvers_dir.py
    python expand_solver.py -q --source solver_dir/ --solvers-file $TMPFILE && \
    mv -f $TMPFILE solvers_dir.py

    # for f in `ls solver_md5 | grep 'def$'`; do ls solver_dir/*/$f &>/dev/null || rm solver_md5/$f; done
    for f in `ls solver_md5 | grep -o '^................................'`; do 
      ls solver_dir/*/${f}.def &>/dev/null || \
      rm solver_md5/${f}.def
      ls solver_dir/*/${f}_*.def &>/dev/null || \
      rm solver_md5/${f}_*.def
    done

    # for f in `ls solver_md5 | grep 'py$'`; do ls solver_dir/*/$f &>/dev/null || rm solver_md5/$f; done
    for f in `ls solver_md5 | grep -o '^................................'`; do 
      ls solver_dir/*/${f}.py &>/dev/null || \
      rm solver_md5/${f}.py
      ls solver_dir/*/${f}_*.py &>/dev/null || \
      rm solver_md5/${f}_*.py
    done

    # # From solvers_ref.py to solvers.py
    # python replace_func.py -q
    # python list_solvers.py -q --input solvers.py >key_pre.txt
    # # From solvers.py to solver_pre/
    # for k in `cat key_pre.txt`
    # do python replace_arg.py -q --input solvers.py --output-dir solver_pre/ $k
    # done
    # # From solver_pre/ to solvers_pre.py
    # python expand_solver.py -q --source solver_pre/ --solvers-file solvers_pre.py
  fi

done
