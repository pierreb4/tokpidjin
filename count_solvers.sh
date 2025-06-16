  echo -n Total solvers:
  ls -l solver_evo/*.def | wc -l
  echo -n Known solvers:
  for f in `ls solver_evo/*.def`; do 
    for n in `echo $f | grep -o solve_........`; do 
      grep $n solvers.py
    done
  done | wc -l

