#!/opt/homebrew/bin/bash

TIMEOUT=$1
BUILD=$2
TMPFILE=$(mktemp)

clear
while date; do 
  python card.py -p
  python main.py --solvers solvers_dir | tee main.log

  python card.py
  numbers=(0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0)
  random_value=$(printf "%s\n" "${numbers[@]}" | shuf -n 1)
  echo "$random_value"
  timeout 900s python run_batt.py -t -to $random_value -c 1000 | tee batt.log

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

    # From solver_dir/ to solvers_dir.py
    # python expand_solver.py -q --source solver_dir/ --solvers-file $TMPFILE && \
    # mv -f $TMPFILE solvers_dir.py

    # for f in `ls solver_md5 | grep 'def$'`; do ls solver_dir/*/$f &>/dev/null || rm solver_md5/$f; done
    for f in `cd solver_md5; ls *.def | grep -o '^................................'`; do 
      ls solver_dir/*/*/${f}.def &>/dev/null || \
      rm solver_md5/${f}.def
    done

    # for f in `ls solver_md5 | grep 'py$'`; do ls solver_dir/*/$f &>/dev/null || rm solver_md5/$f; done
    for f in `cd solver_md5; ls *.py | grep -o '^................................'`; do 
      ls solver_dir/*/*/${f}.py &>/dev/null || \
      rm solver_md5/${f}.py
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
