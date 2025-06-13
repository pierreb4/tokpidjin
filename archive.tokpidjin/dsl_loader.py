"""
This module provides a way to import either the standard DSL or the statistics-tracking DSL.
"""

# Import this module and use get_dsl(stats_enabled=True/False) to get the appropriate DSL module

def get_dsl(stats_enabled=False):
    """
    Get the appropriate DSL module based on whether statistics tracking is enabled.
    
    Args:
        stats_enabled (bool): Whether to enable statistics tracking
        
    Returns:
        module: The DSL module (either with or without statistics tracking)
    """
    if stats_enabled:
        import dsl_with_stats
        return dsl_with_stats
    else:
        import dsl
        return dsl
