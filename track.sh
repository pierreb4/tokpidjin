#!/usr/bin/env bash

# Default values
INTERVAL=300
CMD="python run_test.py -q"

usage() {
    echo "Usage: $0 -i <interval_seconds> -c <command>"
    echo "  -i    Interval in seconds between checks (default: 300)"
    echo "  -c    Command to monitor (required)"
    exit 1
}

# Parse options
while getopts ":i:c:" opt; do
  case $opt in
    i) INTERVAL="$OPTARG" ;;
    c) CMD="$OPTARG" ;;
    *) usage ;;
  esac
done

# Verify command provided
if [ -z "$CMD" ]; then
    echo "Error: command is required"
    usage
fi

# Temporary storage
PREV_OUTPUT="/tmp/monitor_prev_$$.out"
CURR_OUTPUT="/tmp/monitor_curr_$$.out"
trap "rm -f $PREV_OUTPUT $CURR_OUTPUT" EXIT
touch "$PREV_OUTPUT"

while true; do
    # Run the command and capture output
    eval "$CMD" > "$CURR_OUTPUT" 2>&1

    # Compare with previous output
    if ! diff -q "$PREV_OUTPUT" "$CURR_OUTPUT" > /dev/null; then
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] Change detected:"
        diff --unified=0 "$PREV_OUTPUT" "$CURR_OUTPUT"
        echo
    fi

    # Update stored output
    mv "$CURR_OUTPUT" "$PREV_OUTPUT"

    # Sleep for chosen interval
    sleep "$INTERVAL"
done

