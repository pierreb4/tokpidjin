#!/bin/bash

# Check if a directory argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

SOLVER_DIR="$HOME/dsl/tokpidjin/$1"

# Check if the provided argument is a valid directory
if [ ! -d $SOLVER_DIR ]; then
    echo "Error: Directory $SOLVER_DIR does not exist."
    exit 1
fi

# Change to your target directory
cd $SOLVER_DIR || exit 1

# Step 1: Select 10 random files to keep
mapfile -t keep < <(ls | shuf -n 49)

# Step 2: For each .def file, also keep the corresponding .py file
for file in "${keep[@]}"; do
    if [[ "$file" == *.def ]]; then
        base="${file%.def}"
        if [[ -f "$base.py" ]]; then
            keep+=("$base.py")
        fi
    fi
done

# Step 3: Remove all files not in the keep list
for file in *; do
    skip=0
    for k in "${keep[@]}"; do
        if [[ "$file" == "$k" ]]; then
            skip=1
            break
        fi
    done
    if [[ $skip -eq 0 ]]; then
        rm -- "$file"
    fi
done
