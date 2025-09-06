# Done
- [x] 2025-05-26 Redo b_iz and b_zo
- [x] 2025-05-26 Setup script to replace calls in solvers: replace.py
- [x] 2025-05-26 Start with get_nth_by_key and friends
    - [x] 2025-05-26 Substitute first_[tf] into solvers (except with lbind, rbind, etc)
    - [x] 2025-05-26 Look into mostcolor and leastcolor -> get_color_rank
    - [x] 2025-05-26 Look at argmax and argmin -> get_arg_rank
    - [x] 2025-05-26 Look into maximum and minimum -> get_rank
    - [x] 2025-05-26 Look into valmax and valmin -> get_val_rank
    - [x] 2025-05-26 Look into mostcommon and leastcommon
- [x] 2025-05-26 Parameter mirror and rotation functions: mir_rot_[tf]
- [x] 2025-05-26 Use replace.py to replace calls in solvers
- [x] 2025-05-26 Make random value(s) that can jump around, unlike R_, for switch, mir_rot_[tf], etc -> F_, L_, FL (ranks from first, last or both)
- [x] 2025-05-27 Specialize get_nth_t and get_nth_by_key_t to tuples
- [x] 2025-05-27 Add first_[tf] and last_[tf] to replace.py - see __note__ 1
- [x] 2025-05-27 Refine replace.py and run it from solvers_ref.py
- [x] 2025-05-28 Try PMD CPD
- [x] 2025-05-28 Try Sourcery
- [x] 2025-05-28 Adjust inline-solver.py to work with _split or original and format
- [x] 2025-05-28 Make inline-solver.py output to solver_one/*.def
- [x] 2025-05-28 Keep track of random.choice calls in get_todo_set() and limit them
- [x] 2025-05-30 Stop running solver code in get_todo_set() if/when feasible
- [x] 2025-06-03 Add get_func.py for refactoring hints and statistics
- [x] 2025-06-04 Wrote o_g(grid, R8) to replace objects(grid, ...)
- [x] 2025-06-04 Adjust replace_func.py to replace objects() calls
- [x] 2025-06-05 Remove unused variables in check_done and check_hint signatures
- [x] 2025-06-05 Make sure that check_done checks samples, not just tests
- [x] 2025-06-09 Replace function calls with others with same signature
- [x] 2025-06-10 Count calls for each entry in todo_set
- [x] 2025-06-11 Find lost candidates in todo_set
- [x] 2025-06-11 Study cases when regen.py fails to solve known train tasks
- [x] 2025-06-11 Make regen.py check both train and test samples
- [x] 2025-06-11 Keep an eye out for solvers in solvers_evo.py that don't pass main.py - Refined run_test.py and main.py
- [x] 2025-06-11 Restore R_ etc constant substitution
- [x] 2025-06-12 Get regen.py to attempt unsolved tasks and prioritise smaller ones

# Work in Progress
- [] Work on no-loss mir_rot_t comparison

# To Do
- [] Add symmetry checks to a_mr substitution (task 44f52bb0)
- [] Substitute size-related constants, ratio and absolute
- [] Make more direction-related functions parametered
- [] Annotate all DSL function names and signatures
     See f: Callable[[int, str], float] and g: Callable[..., int]
- [] Work on caching in check_hint

# Notes
1. The intention is to avoid manual edits in solvers_ref.py.
    Experimental edits happen in solvers.py or solvers_xxx.py but are expected to be wiped out eventually by replace.py.

# Github commands
|----------------------------------------------------------------|
| **Step**                                                       |
| Command Example(s)                                             |
| or Rollback/Undo Command(s)                                    |
|----------------------------------------------------------------|
| **Clone your fork**                                            |
| `git clone https://github.com/YOU/REPO.git`                    |
|  or  N/A                                                       |
|----------------------------------------------------------------|
| **Add upstream remote**                                        |
| `git remote add upstream https://github.com/ORIGINAL/REPO.git` |
|  or `git remote remove upstream`                               |
|----------------------------------------------------------------|
| **Create branch**                                              |
| `git checkout -b my-feature`                                   |
|  or `git branch -D my-feature` (if not pushed)                 |
|----------------------------------------------------------------|
| **Stage changes**                                              |
| `git add file1 file2`                                          |
|  or `git checkout -- file1` (uncommitted)                      |
|----------------------------------------------------------------|
| **Commit changes**                                             |
| `git commit -m "Description"`                                  |
|  or `git reset --soft HEAD~1` (local only)                     |
|----------------------------------------------------------------|
| **Push branch**                                                |
| `git push origin my-feature`                                   |
|  or `git push -f origin my-feature` (if needed)                |
|----------------------------------------------------------------|
| **Sync with upstream**                                         |
| `git fetch upstream`                                           |
| `git merge upstream/main`                                      |
|  or `git reset --hard <hash>` (local only)                     |
|----------------------------------------------------------------|
| **Rebase branch**                                              |
| `git checkout my-feature`                                      |
| `git rebase main`                                              |
|  or `git rebase --abort`                                       |
|----------------------------------------------------------------|
| **Undo pushed commit**                                         |
| `git revert <commit-hash>`                                     |
|  or  N/A (safe for shared branches)                            |
|----------------------------------------------------------------|


solver_dir/solver_{task_id}/{task_o_score}/{t_log} -> solver_md5
differ_dir/solver_{task_id}/{task_s_score}/{t_log} -> differ_md5


Scoring:

task_o_score: number of tasks solved by solver
task_s_score: per task, number of tasks differ sees improving

- task_1 -> task_o_score_1 + time_1 -> solver_md5_1.py
- task_1 -> task_s_score_1 + time_1 -> solver_md5_1 -> differ_md5_1.py
- task_1 -> task_s_score_2 + time_1 -> solver_md5_1 -> differ_md5_2.py
- task_1 -> task_s_score_3 + time_1 -> solver_md5_1 -> differ_md5_3.py
- ...

- task_1 -> task_o_score_2 + time_2 -> solver_md5_2.py
- differ_4
- differ_5
- differ_6
- ...

- task_1 -> task_o_score_3 + time_3 -> solver_md5_3.py
- differ_1
- differ_4
- differ_7
- ...