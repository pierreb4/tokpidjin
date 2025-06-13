#!/opt/homebrew/bin/bash

# Print usage if no arguments provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <time_factor>"
    echo ""
    echo "Arguments:"
    echo "  time_factor    Max time for loop (mandatory)"
    echo "      - Timeout for regen.py run = 2/3 * time_factor "
    echo "      - Sleep time between runs = 1/3 * time_factor"
    echo ""
    echo "Example:"
    echo "  $0 30 # Run with time_factor=30 (timeout=20s, sleep=10s)"
    exit 1
fi

FACTOR=${1}
SLEEP=$((FACTOR / 3))
TIMEOUT=$((SLEEP * 2))

clear
while date; do 
  timeout ${TIMEOUT}s python regen.py
  # Obsolete?
  # grep -q '^def ' solvers_gen.py && cat solvers_gen.py

  # echo -n Total solvers:
  # ls -l solver_evo/*.def | wc -l
  echo -n Known solvers:
  for f in `ls solver_evo/*.def`; do 
    for n in `echo $f | grep -o solve_........`; do 
      grep $n solvers.py
    done
  done | wc -l

  # d=`date +%F`
  
  # From solvers_evo.py to solvers_xxx.py
  python replace_func.py -q --input solvers_evo.py --output solvers_xxx.py
  python list_solvers.py -q --input solvers_xxx.py >key_xxx.txt
  # From solvers_xxx.py to solver_evo/
  for k in `cat key_xxx.txt`
  do python replace_arg.py -q --input solvers_xxx.py --output-dir solver_evo/ $k
  done
  # From solver_evo/ to solvers_evo.py
  python expand_solver.py -q --source solver_evo/ --solvers-file solvers_evo.py

  # python main.py -q --solvers solvers_evo.py

  # From solvers_ref.py to solvers.py
  python replace_func.py -q
  python list_solvers.py -q --input solvers.py >key_pre.txt
  # From solvers.py to solver_pre/
  for k in `cat key_pre.txt`
  do python replace_arg.py -q --input solvers.py --output-dir solver_pre/ $k
  done
  # From solver_pre/ to solvers_pre.py
  python expand_solver.py -q --source solver_pre/ --solvers-file solvers_pre.py

  sleep $SLEEP
done