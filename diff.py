import os
import json

from arc_types import *
from dsl import *
import solvers_manus as solvers


def second( container: Container ) -> Any:
    """ second item of container """
    iterator = iter(container)
    next(iterator)
    return next(iterator, None)


def difference_tuple( a: Tuple, b: Tuple ) -> Tuple:
    """ set difference """
    return type(a)(e for e in a if e not in b)


def palette_tuple( element: Element ) -> IntegerSet:
    """ colors occurring in object or grid """
    if isinstance(element, tuple) and all(isinstance(row, tuple) for row in element):
        # Handle 2D grid case
        return tuple(set(cell for row in element for cell in row))
    else:
        # Fallback to original implementation for other cases
        try:
            return tuple({v for v, _ in element})
        except ValueError:
            # If element is just a flat collection of values
            return tuple(set(element))


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
    data = get_data(train=True)
    
    for key in data['train'].keys():
        # if key != '253bf280':
        #     continue

        task = data['train'][key]
        print(f"Testing task: {key}")
        print(f"Number of samples: {len(task)}")

        S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in task)

        result_iz = iz(S, palette_tuple)
        print(f"Result iz: {result_iz}")

        result_zo = zo(S, palette_tuple)
        print(f"Result zo: {result_zo}")