"""
Batch Batt Generator - Generates native batch-processing batt functions

Instead of monkey-patching DSL functions at runtime, this generates batt code
that directly calls batch GPU operations (batch_mapply, batch_o_g, etc.).

Strategy:
1. Read existing solver code
2. Transform DSL calls → batch DSL calls
3. Handle variable naming (S → Ss, I → Is, t1 → t1s)
4. Generate function signature: batt_batch(task_ids, Ss, Is, Cs, log_paths)

Example transformation:
    FROM (single):
        t1 = mapply(rot90, S)
        t2 = apply(first, S)
        t3 = o_g(I, 0)
    
    TO (batch):
        t1s = batch_mapply(rot90, Ss)    # Process all samples
        t2s = batch_apply(first, Ss)      # Batch apply
        t3s = batch_o_g(Is, 0)            # Batch object extraction

Author: Pierre
Date: October 13, 2025
Week: 5 Day 3 - Option 3 Implementation
"""

import re
import argparse
from typing import List, Dict, Tuple


# DSL functions that have batch equivalents
BATCH_OPERATIONS = {
    'mapply': 'batch_mapply',
    'apply': 'batch_apply',
    'o_g': 'batch_o_g',
    'fill': 'batch_fill',
    'colorfilter': 'batch_colorfilter',
}

# Variables that should be pluralized in batch mode
BATCH_VARIABLES = {'S', 'I', 'C'}  # Samples, Input, Context


class BatchBattGenerator:
    """Generate batch-native batt functions from single-sample solvers"""
    
    def __init__(self, source_batt_file: str, output_file: str):
        """
        Initialize batch generator.
        
        Args:
            source_batt_file: Path to source batt.py (single-sample version)
            output_file: Path to output batt_batch.py (batch version)
        """
        self.source_file = source_batt_file
        self.output_file = output_file
        self.transformations = 0
        
    def transform_function_call(self, line: str) -> Tuple[str, bool]:
        """
        Transform a single DSL function call to batch version.
        
        Args:
            line: Source code line
            
        Returns:
            (transformed_line, was_transformed)
        """
        transformed = False
        
        # Pattern: t<N> = function(args)
        match = re.match(r'(\s+)(t\d+)\s*=\s*(\w+)\((.*)\)', line)
        if not match:
            return line, False
        
        indent, var_name, func_name, args = match.groups()
        
        # Check if function has batch equivalent
        if func_name in BATCH_OPERATIONS:
            batch_func = BATCH_OPERATIONS[func_name]
            
            # Pluralize variable name: t1 → t1s
            batch_var = var_name + 's'
            
            # Transform arguments: S → Ss, I → Is, etc.
            batch_args = self.pluralize_args(args)
            
            # Reconstruct line
            new_line = f'{indent}{batch_var} = {batch_func}({batch_args})\n'
            transformed = True
            self.transformations += 1
            
            return new_line, transformed
        
        # For non-batch operations, still pluralize variable if it uses batch vars
        if any(var in args for var in BATCH_VARIABLES):
            # Pluralize the target variable
            batch_var = var_name + 's'
            batch_args = self.pluralize_args(args)
            new_line = f'{indent}{batch_var} = {func_name}({batch_args})\n'
            return new_line, True
        
        return line, False
    
    def pluralize_args(self, args: str) -> str:
        """
        Pluralize batch variables in arguments.
        
        Args:
            args: Function arguments string
            
        Returns:
            Arguments with batch variables pluralized
        """
        result = args
        
        # Replace standalone batch variables
        for var in BATCH_VARIABLES:
            # Match whole word only (not part of another identifier)
            result = re.sub(rf'\b{var}\b', f'{var}s', result)
        
        # Also pluralize t<N> references: t1 → t1s, t12 → t12s
        result = re.sub(r'\bt(\d+)\b', r't\1s', result)
        
        return result
    
    def transform_function_signature(self, line: str) -> str:
        """
        Transform function signature to batch version.
        
        FROM: def batt(task_id, S, I, C, log_path):
        TO:   def batt_batch(task_ids, Ss, Is, Cs, log_paths):
        """
        if 'def batt(' in line:
            return line.replace('def batt(', 'def batt_batch(') \
                      .replace('task_id,', 'task_ids,') \
                      .replace(' S,', ' Ss,') \
                      .replace(' I,', ' Is,') \
                      .replace(' C,', ' Cs,') \
                      .replace('log_path)', 'log_paths)')
        return line
    
    def transform_file(self) -> None:
        """
        Transform entire batt file to batch version.
        """
        print(f"Transforming {self.source_file} → {self.output_file}")
        
        with open(self.source_file, 'r') as src:
            lines = src.readlines()
        
        with open(self.output_file, 'w') as dst:
            # Write header
            dst.write('"""\n')
            dst.write('Batch-native batt function - Auto-generated\n')
            dst.write(f'Source: {self.source_file}\n')
            dst.write('Generator: batch_batt_generator.py\n')
            dst.write('\n')
            dst.write('This version processes entire batches natively using GPU operations:\n')
            dst.write('- batch_mapply: Batch map-apply operations\n')
            dst.write('- batch_o_g: Batch object extraction\n')
            dst.write('- batch_apply: Batch apply operations\n')
            dst.write('- batch_fill: Batch fill operations\n')
            dst.write('"""\n\n')
            
            # Write imports
            dst.write('from dsl import *\n')
            dst.write('from gpu_dsl_operations import get_gpu_ops\n\n')
            dst.write('# Initialize GPU operations\n')
            dst.write('_gpu_ops = get_gpu_ops(enable_gpu=True)\n\n')
            dst.write('# Batch operation shortcuts\n')
            for single, batch in BATCH_OPERATIONS.items():
                dst.write(f'{batch} = _gpu_ops.{batch}\n')
            dst.write('\n')
            
            # Transform function body
            for line in lines:
                # Skip original imports
                if line.startswith('from') or line.startswith('import'):
                    continue
                
                # Transform function signature
                if 'def batt(' in line:
                    line = self.transform_function_signature(line)
                    dst.write(line)
                    continue
                
                # Transform function calls
                new_line, was_transformed = self.transform_function_call(line)
                dst.write(new_line)
        
        print(f"✅ Transformation complete!")
        print(f"   {self.transformations} operations converted to batch versions")
        print(f"   Output: {self.output_file}")


def generate_batch_batt(source_file: str = 'batt_gpu_operations_test.py',
                       output_file: str = 'batt_batch_native.py'):
    """
    Generate batch-native batt function.
    
    Args:
        source_file: Source single-sample batt file
        output_file: Output batch-native batt file
    """
    generator = BatchBattGenerator(source_file, output_file)
    generator.transform_file()
    
    return output_file


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate batch-native batt functions')
    parser.add_argument('-i', '--input', type=str, default='batt_gpu_operations_test.py',
                       help='Input batt file (single-sample version)')
    parser.add_argument('-o', '--output', type=str, default='batt_batch_native.py',
                       help='Output batt file (batch-native version)')
    
    args = parser.parse_args()
    
    print("="*70)
    print("Batch Batt Generator - Option 3 Implementation")
    print("="*70)
    print()
    
    output = generate_batch_batt(args.input, args.output)
    
    print()
    print("="*70)
    print("Next steps:")
    print("1. Review generated file:", output)
    print("2. Test with: from", output.replace('.py', ''), "import batt_batch")
    print("3. Benchmark vs single-sample version")
    print("="*70)
