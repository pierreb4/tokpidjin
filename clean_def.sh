#!/bin/bash

# Check if a directory argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <directory> [<max_num_files>]"
    exit 1
fi

SOLVER_DIR="$HOME/dsl/tokpidjin/$1"
MAX_NUM_FILES="$2"

if [ -z "$MAX_NUM_FILES" ]; then
    MAX_NUM_FILES=99
fi

# Check if the provided argument is a valid directory
if [ ! -d $SOLVER_DIR ]; then
    echo "Error: Directory $SOLVER_DIR does not exist."
    exit 1
fi

# Remove old *.pyc files
find $SOLVER_DIR -type f -name "*.pyc" ! -exec sh -c '
  py="${1%__pycache__/*}$(basename "${1%%.cpython-*}" .pyc).py"
  [ -e "$py" ]' _ {} \; -delete

# Remove empty sub-directories
find $SOLVER_DIR -type d -empty -delete

# Change to your target directory (solver_dir/solve_*)
cd $SOLVER_DIR || exit 1

# Step 1: Select files to keep
TMPFILE=$(mktemp)
# ls [0-9]*/[0-9a-f]* | shuf -n "$MAX_NUM_FILES" >$TMPFILE

ls -vd [0-9]*/[0-9]*/[0-9]*/[0-9a-f]*.py | tail -$MAX_NUM_FILES >$TMPFILE
mapfile -t keep <$TMPFILE
rm $TMPFILE

if [[ -z "${keep[@]}" ]]; then
    echo "keep is empty"
    ls -lR "$SOLVER_DIR"
    rm -r "$SOLVER_DIR"
    exit 1
fi

# Step 2: Remove all files not in the keep list
for file in `ls [0-9]*/[0-9]*/[0-9]*/[0-9a-f]*.py`; do
    skip=0
    for k in "${keep[@]}"; do
        if [[ "$file" == "$k" ]]; then
            skip=1
            break
        fi
    done
    if [[ $skip -eq 0 ]]; then
        if [[ ${file:0:1} != "0" ]]; then
            find solver_dir -name "$file"
            echo rm -- "$file"
        fi  
        rm -- "$file"
    fi
done
