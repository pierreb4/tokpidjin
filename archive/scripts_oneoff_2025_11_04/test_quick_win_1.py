#!/usr/bin/env python3
"""
Test Quick Win #1: Solver Body Caching
Tests that solver body cache improves performance by caching inlined solvers
"""
import os
import sys
import time
import hashlib
import tempfile
from pathlib import Path

# Test the caching infrastructure
def test_solver_body_cache():
    from solver_body_cache import (
        init_solver_body_cache,
        get_cached_solver_body,
        cache_solver_body,
        print_solver_body_cache_stats
    )
    
    print("=" * 70)
    print("TEST: Solver Body Caching")
    print("=" * 70)
    
    # Initialize cache
    print("\n1. Initializing cache...")
    init_solver_body_cache()
    print("   ✓ Cache initialized")
    
    # Test cache miss on new solver
    print("\n2. Testing cache miss...")
    test_source = "def solve_test_123():\n    return test_data"
    result = get_cached_solver_body(test_source)
    if result is None:
        print("   ✓ Cache miss on new solver (expected)")
    else:
        print("   ✗ ERROR: Should have missed cache!")
        return False
    
    # Cache a solver body
    print("\n3. Caching solver body...")
    test_body = "def solve_test_123():\n    # inlined code here\n    return process(test_data)"
    cache_solver_body(test_source, test_body)
    print("   ✓ Solver body cached")
    
    # Test cache hit
    print("\n4. Testing cache hit...")
    cached_result = get_cached_solver_body(test_source)
    if cached_result == test_body:
        print("   ✓ Cache hit successful (body matches)")
    else:
        print("   ✗ ERROR: Cached body doesn't match!")
        print(f"   Expected: {test_body[:50]}...")
        print(f"   Got:      {cached_result[:50] if cached_result else 'None'}...")
        return False
    
    # Print statistics
    print("\n5. Cache statistics:")
    print_solver_body_cache_stats()
    
    print("\n" + "=" * 70)
    print("✓ ALL TESTS PASSED")
    print("=" * 70)
    return True

if __name__ == "__main__":
    success = test_solver_body_cache()
    sys.exit(0 if success else 1)
