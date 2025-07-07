  SOLVER_DIR=$1

  echo -n Total solvers:
  TMPFILE=$(mktemp)
  find $SOLVER_DIR -type l -name '*.py' >$TMPFILE
  cat $TMPFILE | wc -l
  # echo -n Known solvers:
  # while IFS= read -r f; do
  #   for n in `echo $f | grep -o solve_........`; do 
  #     grep $n solvers.py
  #   done
  # done <$TMPFILE | wc -l
