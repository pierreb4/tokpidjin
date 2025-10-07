import asyncio
import hashlib
import math

from timeit import default_timer as timer

from utils import *
from run_test import check_solvers_pre
from expand_solver import generate_expanded_content


async def main():
    train_data = get_data(train=True, sort_by_size=True)
    # eval_data = get_data(train=False, sort_by_size=True)
    # total_data = {k: {**train_data[k], **eval_data[k]} for k in ['demo', 'test']}
    total_data = train_data

    solvers = get_solvers([solvers_pre], best_only=True)

    # Solver = namedtuple('Solver', ['name', 'path', 'source', 'o_score', 't_score'])
    for task_id, solver in solvers.items():

        check_start = timer()
        timed_out, task_o_score = await check_solvers_pre(total_data, task_id, timeout=1)
        t_log = 11 - int(math.log(timer() - check_start))

        # print_l(f'Processed solver for {task_id=} with {task_o_score=}, {timed_out=} and {t_log=}')
        # print(f'{solver.source=}')

        old_head = f'from dsl import *\nfrom constants import *\n\ndef solve_{task_id}(S, I, C):\n'
        solver_body = solver.source.replace(old_head, '')

        # print(f'{solver_body=}')

        solver_source = f'def solve(S, I, C):\n{solver_body}'
        inlined_source = inline_variables(solver_source)
        md5_hash = hashlib.md5(inlined_source.encode()).hexdigest()

        ensure_dir('solver_md5')
        solver_md5_path = f'solver_md5/{md5_hash}.py'

        if not Path(solver_md5_path).exists():
            generate_expanded_content(inlined_source, solver_md5_path)

        # task_o_score = o_score.get(sol_solver_id)
        solver_score = f'solver_dir/solve_{task_id}/{task_o_score}/{t_log}'

        ensure_dir(solver_score)
        solver_link = f'{solver_score}/{md5_hash}.py'

        symlink(solver_md5_path, solver_link)


if __name__ == "__main__":
    asyncio.run(main())
