#!/opt/homebrew/bin/bash

# Workflow script to optimize DSL function calls
# Usage: ./workflow.sh [sample_size]
#   sample_size: Number of solvers to sample (default: all keus)

# Note:
# grep "^def [a-z]*_t(" dsl.py | sort

# Copy hand-made reference solvers
cp solvers_ref.py solvers.py

d=`date +%F`

# Set sample size from command line argument or all keys
if [ -z "$1" ]; then
    python list_solvers.py --quiet >key_$d.txt
else
    sample=$1
    python list_solvers.py --sample $sample --seed 0 --quiet >key_$d.txt
fi

# Process the keys
echo "Processing the following keys:"
cat key_$d.txt

rm -f stats/generic_dsl_*
rm -f error/generic_dsl_*
for k in `cat key_$d.txt`; do timeout 10s python track_solver.py $k --quiet; done

rm -f stats/special_dsl_*
for f in stats/generic_dsl_*; do python gen_special_dsl.py $f --threshold 100.0; done

for f in stats/special_dsl_*; do python optimize_solvers.py $f --apply --force; done

#####################################################################################
# Process generated solvers
###########################
# Expand one-line solvers
python expand_solver.py -q --source solver_evo/ --solvers-file solvers_evo.py

# Check for errors
python main.py --solvers solvers_evo.py

# Split solvers
python split_solver.py --source solver_evo/ --no-condensed --no-expanded

# Add type hints to solver_evo/solve_*_split.py
python add_type_signatures.py

# Replace and transform solvers #############################################
# From solvers_ref.py to solvers.py
python replace_func.py
# From solvers.py to solver_pre/
for k in `cat key_pre.txt`; do python transform_solver.py $k; done
# From solver_pre/ to solvers.py
python expand_solver.py --source solver_pre/ --solvers-file solvers.py

#####################################################################################
## Terminal commands ################################################################

# Upper left term
clear; bash run_regen.sh 12

# 2nd from upper left
g='c_iz_n c_zo_n a_mr'
while true
  do for izzo in $g
  do echo -n $izzo
    grep $izzo solvers_evo.py | wc -l
    done
  sleep 60
done

# Lower left
clear; time timeout 15s python regen.py

# Lower right
python expand_solver.py -q --source solver_evo/ --solvers-file solvers_evo.py && \
python main.py --solvers solvers_evo.py


# Smallest solvers in solver_pre/ but not in solver_evo/
for f in `cd solver_pre && ls *.def`
do ls solver_evo/$f &>/dev/null || ls -l solver_pre/$f
done | sort -rnk5

# Regenerate train solvers starting from smallest one
clear
while date
do for f in `cd solver_pre && ls *.def`
  do ls solver_evo/$f &>/dev/null || ls -l solver_pre/$f
  done | sort -rnk5 | tail -5
python regen_dev.py `cat next_task_dev.txt`
sleep 120
done

# Regenerate any solver, preferring smallest tasks
clear
while date
do python regen_dev.py
sleep 60
done

# Remove bad evo solvers and check
rm solver_evo/solve_bb43febb*
python expand_solver.py -q --source solver_evo/ --solvers-file solvers_evo.py
python main.py --solvers solvers_evo.py
#####################################################################################
#####################################################################################
