#!/usr/bin/env python3
"""
Phase 4 Quick Win #1: Solver Body Result Caching

Current situation:
- Inlining cache at 100% (16,000 hits)
- But inlined bodies might be discarded after each task
- Next task with same solver needs to re-inline

Optimization:
- Cache the final inlined solver bodies
- Check cache before running solver
- Skip validation if identical solver already seen

Expected speedup: 3-8% (depending on solver reuse rate)
"""

import hashlib
from pathlib import Path
from typing import Dict, Optional
import json

# Cache directory
CACHE_DIR = Path('.cache')
SOLVER_BODY_CACHE_DIR = CACHE_DIR / 'solver_bodies'

# In-memory cache for this session
_solver_body_cache: Dict[str, str] = {}

# Statistics
_solver_body_stats = {
    'hits': 0,
    'misses': 0,
    'new_bodies': 0,
}


def init_solver_body_cache():
    """Initialize solver body cache."""
    try:
        SOLVER_BODY_CACHE_DIR.mkdir(parents=True, exist_ok=True)
        print(f"[solver_body_cache] Created cache directory: {SOLVER_BODY_CACHE_DIR}")
        _load_solver_body_cache()
        print(f"[solver_body_cache] Cache initialization successful")
    except Exception as e:
        print(f"[solver_body_cache] ERROR during initialization: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        raise


def _load_solver_body_cache():
    """Load solver bodies from disk cache."""
    cache_index_file = SOLVER_BODY_CACHE_DIR / 'index.json'
    
    print(f"[solver_body_cache] Looking for index file: {cache_index_file}")
    
    if cache_index_file.exists():
        print(f"[solver_body_cache] Index file exists, loading...")
        try:
            with open(cache_index_file, 'r') as f:
                index = json.load(f)
                # Don't load all bodies into memory, just the index
                _solver_body_cache.update({k: v for k, v in index.items()})
                print(f"[solver_body_cache] Loaded solver body cache index: {len(_solver_body_cache)} entries")
        except Exception as e:
            print(f"[solver_body_cache] ERROR loading index: {type(e).__name__}: {e}")
            import traceback
            traceback.print_exc()
    else:
        print(f"[solver_body_cache] Index file does not exist (first run or not persisted): {cache_index_file}")


def get_solver_body_cache_key(source_code: str) -> str:
    """Generate cache key for solver source code."""
    return hashlib.md5(source_code.encode()).hexdigest()


def get_cached_solver_body(source_code: str) -> Optional[str]:
    """
    Retrieve cached inlined solver body.
    
    Returns cached body if it exists, None otherwise.
    """
    cache_key = get_solver_body_cache_key(source_code)
    
    # Check memory cache
    if cache_key in _solver_body_cache:
        _solver_body_stats['hits'] += 1
        return _solver_body_cache[cache_key]
    
    # Check disk cache
    cache_file = SOLVER_BODY_CACHE_DIR / f'{cache_key}.py'
    if cache_file.exists():
        try:
            with open(cache_file, 'r') as f:
                body = f.read()
                _solver_body_cache[cache_key] = body
                _solver_body_stats['hits'] += 1
                return body
        except Exception as e:
            print(f"[solver_body_cache] ERROR reading disk cache {cache_file}: {e}")
    
    _solver_body_stats['misses'] += 1
    return None


def cache_solver_body(source_code: str, inlined_body: str):
    """
    Cache an inlined solver body.
    
    This caches the final inlined solver so we don't need to re-inline it
    if we see the same source code again.
    """
    cache_key = get_solver_body_cache_key(source_code)
    
    # Store in memory
    _solver_body_cache[cache_key] = inlined_body
    
    # Store on disk
    cache_file = SOLVER_BODY_CACHE_DIR / f'{cache_key}.py'
    try:
        with open(cache_file, 'w') as f:
            f.write(inlined_body)
        _solver_body_stats['new_bodies'] += 1
    except Exception as e:
        print(f"Warning: Could not cache solver body: {e}")


def get_solver_body_cache_stats() -> Dict[str, int]:
    """Get caching statistics."""
    return _solver_body_stats.copy()


def print_solver_body_cache_stats():
    """Print solver body caching statistics."""
    stats = get_solver_body_cache_stats()
    total = stats['hits'] + stats['misses']
    
    if total > 0:
        hit_rate = stats['hits'] / total * 100
        print(f"\nSolver Body Cache:")
        print(f"  Hits: {stats['hits']}")
        print(f"  Misses: {stats['misses']}")
        print(f"  Total: {total}")
        print(f"  Hit Rate: {hit_rate:.1f}%")
        print(f"  New Bodies Cached: {stats['new_bodies']}")


if __name__ == '__main__':
    # Test the cache
    init_solver_body_cache()
    
    test_code = "def solve_abc(): pass"
    test_body = "expanded_solve_abc_body_here"
    
    # First call should miss
    result = get_cached_solver_body(test_code)
    print(f"First call result: {result}")  # Should be None
    
    # Cache it
    cache_solver_body(test_code, test_body)
    
    # Second call should hit
    result = get_cached_solver_body(test_code)
    print(f"Second call result: {result}")  # Should be test_body
    
    print_solver_body_cache_stats()
