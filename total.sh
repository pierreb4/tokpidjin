#!/bin/bash

total=0
for dir in solver_dir/*; do
  # Read numbers from the file or output
  numbers=$(ls "$dir")
  
  # Find the largest number in the list
  max=$(echo $numbers | tr ' ' '\n' | sort -nr | head -1)
  
  # Add to total
  total=$((total + max))
done

echo "Total score: $total"

