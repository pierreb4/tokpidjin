import os

import arc_types
import dsl

def iz( S: SampleType, function: Callable ) -> Any:
    x1 = apply(first, S)
    x2 = apply(second, S)
    x3 = apply(function, x1)
    x4 = apply(function, x2)
    x5 = papply(difference_tuple, x3, x4)
    O = first(x5)
    return O


def zo( S: SampleType, function: Callable ) -> Any:
    x1 = apply(first, S)
    x2 = apply(second, S)
    x3 = apply(function, x1)
    x4 = apply(function, x2)
    x5 = papply(difference_tuple, x4, x3)
    O = first(x5)
    return O


def get_data(train=True):
    path = f'../data/{"training" if train else "evaluation"}'
    data = {}
    for fn in os.listdir(path):
        with open(f'{path}/{fn}') as f:
            data[fn.rstrip('.json')] = json.load(f)
    ast = lambda g: tuple(tuple(r) for r in g)
    return {
        'train': {k: [{
            'input': ast(e['input']),
            'output': ast(e['output']),
        } for e in v['train']] for k, v in data.items()},
        'test': {k: [{
            'input': ast(e['input']),
            'output': ast(e['output']),
        } for e in v['test']] for k, v in data.items()}
    }


# Add main to load train data from a few samples in data/training and test with function palette_tuple
if __name__ == "__main__":
    # Load training data
    train_data = get_data()
    
    # Test with function palette_tuple
    for sample in train_data:
        result = iz(sample, palette_tuple)
        print(f"Result for sample {sample}: {result}")