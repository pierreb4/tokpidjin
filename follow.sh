#!/usr/bin/env bash

# Default values
INTERVAL=300
CLEANUP="rm run_test.log"
CMD="python run_test.py -q"
QUIET=false

usage() {
    echo "Usage: $0 -i <interval_seconds> -c <command> [-q]"
    echo "  -i    Interval in seconds between checks (default: 300)"
    echo "  -c    Command to monitor (required)"
    echo "  -q    Quiet output, only print changed lines"
    exit 1
}

# Parse options
while getopts ":i:c:q" opt; do
  case $opt in
    i) INTERVAL="$OPTARG" ;;
    c) CMD="$OPTARG" ;;
    q) QUIET=true ;;
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
    # Clean up before running
    eval "$CLEANUP"
    # Run the command and capture output
    eval "$CMD" > "$CURR_OUTPUT" 2>&1

    # Compare with previous output
    if ! diff -q "$PREV_OUTPUT" "$CURR_OUTPUT" > /dev/null; then
        echo -n "[$(date '+%Y-%m-%d %H:%M:%S')] "
        if $QUIET; then
            # echo "Changed lines:"
            diff --unchanged-line-format='' --old-line-format='' --new-line-format='%L' "$PREV_OUTPUT" "$CURR_OUTPUT"
        else
            echo "Change detected:"
            diff --unified=0 "$PREV_OUTPUT" "$CURR_OUTPUT"
            echo
        fi
    fi

    # Update stored output
    mv "$CURR_OUTPUT" "$PREV_OUTPUT"

    # Sleep for chosen interval
    sleep "$INTERVAL"
done
