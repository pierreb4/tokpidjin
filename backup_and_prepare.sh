#!/bin/bash
# DSL Consolidation Script - BACKUP FIRST, THEN RUN
# This script consolidates _t/_f variants in dsl.py

set -e

DSL_FILE="/Users/pierre/dsl/tokpidjin/dsl.py"

echo "⚠️  CONSOLIDATION READY TO BEGIN"
echo "================================"
echo ""
echo "This script will:"
echo "  1. Back up dsl.py to dsl.py.backup"
echo "  2. Consolidate 34 function pairs (_t/_f variants)"
echo "  3. Remove ~2000 lines of duplicated code"
echo ""
echo "Functions to consolidate:"
echo "  apply, rapply, mapply, first, last, remove, other,"
echo "  get_nth, get_nth_by_key, get_arg_rank, get_val_rank, get_common_rank,"
echo "  sfilter, mfilter, merge, combine, size,"
echo "  valmax, valmin, argmax, argmin, mostcommon, leastcommon,"
echo "  mostcolor, leastcolor, shape, palette, square,"
echo "  hmirror, vmirror, dmirror, cmirror, portrait, colorcount"
echo ""
echo "Backup file: $DSL_FILE.backup"
echo ""

# Create backup
if [ ! -f "$DSL_FILE.backup" ]; then
    cp "$DSL_FILE" "$DSL_FILE.backup"
    echo "✓ Backup created: $DSL_FILE.backup"
else
    echo "✓ Backup already exists: $DSL_FILE.backup"
fi

echo ""
echo "Ready to consolidate. Manual Python script needed for complex replacements."
echo "See: consolidate_dsl_impl.py for implementation details."
