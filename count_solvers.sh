  SOLVER_DIR=$1

  echo -n Total solvers:
  ls $SOLVER_DIR/*/*/*.def | wc -l
  echo -n Known solvers:
  for f in `ls $SOLVER_DIR/*/*/*.def`; do 
    for n in `echo $f | grep -o solve_........`; do 
      grep $n solvers.py
    done
  done | wc -l

