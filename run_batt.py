import random

from utils import *
from batt import batt 


def main():
    train_data = get_data(train=True)
    eval_data = get_data(train=False)

    total_data = {}
    for k in ['train', 'test']:
        total_data[k] = {**train_data[k], **eval_data[k]}

    task_list = list(total_data['train'].keys())

    task_sizes = []
    for task_id in task_list:
        size = 0
        for S in total_data['train'][task_id] + total_data['test'][task_id]:
            for ex in S.values():
                size += sum(len(inner) for inner in ex)
        task_sizes.append(size)

    weighted_tasks = list(zip(task_list, task_sizes))
    inverse_weights = [1/size for _, size in weighted_tasks]

    task_id = random.choices(
        [t_id for t_id, _ in weighted_tasks],
        weights=inverse_weights,
        k=1
    )[0]

    task = total_data['train'][task_id] + total_data['test'][task_id]

    for sample in task:
        S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in task)
        I = sample['input']
        
        batt(S, I)


if __name__ == "__main__":
    main()