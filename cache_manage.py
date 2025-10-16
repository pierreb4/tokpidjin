#!/usr/bin/env python3
"""
Cache Management Utility

Provides easy commands to manage solver/inlining caches:
- View cache status and size
- Expire old entries
- Clear caches
- Configure TTL

Usage:
    python cache_manage.py status          # Show cache status
    python cache_manage.py size            # Show cache sizes
    python cache_manage.py expire          # Expire entries older than TTL
    python cache_manage.py refresh [days]  # Refresh cache (remove >N days old)
    python cache_manage.py clear [type]    # Clear entire cache
    python cache_manage.py config          # Show cache configuration

Examples:
    python cache_manage.py status
    python cache_manage.py refresh 3       # Remove entries older than 3 days
    python cache_manage.py clear validation
"""

import sys
import argparse
from batt_cache import (
    print_cache_config,
    print_cache_stats,
    get_cache_size,
    expire_old_cache_entries,
    refresh_cache,
    clear_cache,
    CACHE_TTL_SECONDS
)


def cmd_status():
    """Show cache status and stats"""
    print("=== Cache Status ===")
    print_cache_stats()
    print("\n" + "="*60)
    print_cache_config()


def cmd_size():
    """Show cache disk usage"""
    sizes = get_cache_size()
    print("\n=== Cache Disk Usage ===")
    if 'validation_mb' in sizes:
        print(f"Validation: {sizes['validation_mb']:.2f} MB ({sizes['validation_bytes']:,} bytes)")
    if 'inlining_mb' in sizes:
        print(f"Inlining:   {sizes['inlining_mb']:.2f} MB ({sizes['inlining_bytes']:,} bytes)")
    if 'total_mb' in sizes:
        print(f"Total:      {sizes['total_mb']:.2f} MB ({sizes['total_bytes']:,} bytes)")


def cmd_expire():
    """Expire cache entries older than TTL"""
    if CACHE_TTL_SECONDS <= 0:
        print("Cache TTL is disabled (CACHE_TTL_SECONDS = 0)")
        print("No automatic expiration will occur")
        return
    
    print(f"Expiring cache entries older than TTL ({CACHE_TTL_SECONDS} seconds)...")
    stats = expire_old_cache_entries()
    print(f"✓ Validation expired: {stats['validation_expired']} entries")
    print(f"✓ Inlining expired: {stats['inlining_expired']} entries")
    print(f"✓ Total expired: {stats['validation_expired'] + stats['inlining_expired']} entries")


def cmd_refresh(days: int = 7):
    """Refresh cache by removing old entries"""
    print(f"Refreshing cache (removing entries older than {days} days)...")
    stats = refresh_cache(max_age_days=days)
    print(f"✓ Validation removed: {stats['validation_removed']} entries")
    print(f"✓ Inlining removed: {stats['inlining_removed']} entries")
    print(f"✓ Total removed: {stats['validation_removed'] + stats['inlining_removed']} entries")


def cmd_clear(cache_type: str = None):
    """Clear entire cache"""
    if cache_type:
        print(f"Clearing {cache_type} cache...")
    else:
        print("Clearing all caches...")
    
    response = input("Are you sure? (yes/no): ").strip().lower()
    if response != 'yes':
        print("Cancelled.")
        return
    
    clear_cache(cache_type)
    print(f"✓ Cache cleared")


def cmd_config():
    """Show cache configuration"""
    print_cache_config()


def main():
    parser = argparse.ArgumentParser(
        description='Cache Management Utility',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to run')
    
    # Status command
    subparsers.add_parser('status', help='Show cache status and statistics')
    
    # Size command
    subparsers.add_parser('size', help='Show cache disk usage')
    
    # Expire command
    subparsers.add_parser('expire', help='Expire entries older than TTL')
    
    # Refresh command
    refresh_parser = subparsers.add_parser('refresh', help='Refresh cache (remove old entries)')
    refresh_parser.add_argument('days', type=int, nargs='?', default=7,
                               help='Remove entries older than this many days (default: 7)')
    
    # Clear command
    clear_parser = subparsers.add_parser('clear', help='Clear entire cache')
    clear_parser.add_argument('type', nargs='?', choices=['validation', 'inlining'],
                             help='Cache type to clear (default: both)')
    
    # Config command
    subparsers.add_parser('config', help='Show cache configuration')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Execute command
    if args.command == 'status':
        cmd_status()
    elif args.command == 'size':
        cmd_size()
    elif args.command == 'expire':
        cmd_expire()
    elif args.command == 'refresh':
        cmd_refresh(args.days)
    elif args.command == 'clear':
        cmd_clear(args.type)
    elif args.command == 'config':
        cmd_config()


if __name__ == '__main__':
    main()
