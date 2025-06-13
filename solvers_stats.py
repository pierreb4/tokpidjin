#!/usr/bin/env python3
import ast
import re
import os
from collections import Counter, defaultdict
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
from itertools import groupby

def extract_function_calls(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Parse the Python code
    tree = ast.parse(content)
    
    # Dictionary to track function calls within each solve function
    function_calls = {}
    
    # Process all function definitions
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name.startswith('solve_'):
            function_name = node.name
            calls = []
            
            # Extract all function calls in the function body in order
            for subnode in ast.walk(node):
                if isinstance(subnode, ast.Call) and hasattr(subnode.func, 'id'):
                    calls.append(subnode.func.id)
            
            function_calls[function_name] = calls
    
    return function_calls

def calculate_function_associations(function_calls):
    # Count co-occurrences of function pairs
    co_occurrences = defaultdict(Counter)
    all_called_functions = set()
    
    for solve_func, calls in function_calls.items():
        # Count each function called within this solver
        for func in set(calls):  # Use set to count each function once per solver
            all_called_functions.add(func)
            for other_func in set(calls):
                if func != other_func:
                    co_occurrences[func][other_func] += 1
    
    # Create association matrix
    all_functions = sorted(list(all_called_functions))
    n = len(all_functions)
    function_indices = {func: i for i, func in enumerate(all_functions)}
    
    # Create co-occurrence matrix
    matrix = np.zeros((n, n))
    for func, counter in co_occurrences.items():
        i = function_indices[func]
        for other_func, count in counter.items():
            j = function_indices[other_func]
            matrix[i, j] = count
    
    # Calculate cosine similarity
    similarity_matrix = cosine_similarity(matrix)
    
    return all_functions, matrix, similarity_matrix

def find_top_associated_pairs(all_functions, co_occurrence_matrix, similarity_matrix, top_n=20):
    n = len(all_functions)
    pairs = []
    
    # Collect all function pairs with their association scores
    for i in range(n):
        for j in range(i+1, n):
            if co_occurrence_matrix[i, j] > 0:  # Only consider pairs that co-occur
                pairs.append((
                    all_functions[i], 
                    all_functions[j],
                    co_occurrence_matrix[i, j],  # Raw co-occurrence count
                    similarity_matrix[i, j]      # Cosine similarity
                ))
    
    # Sort by co-occurrence count (primary) and similarity (secondary)
    pairs.sort(key=lambda x: (x[2], x[3]), reverse=True)
    
    return pairs[:top_n]

def visualize_function_network(all_functions, co_occurrence_matrix, top_n=50):
    # Create a graph
    G = nx.Graph()
    
    # Add nodes
    for func in all_functions:
        G.add_node(func)
    
    # Add edges for top N co-occurrences
    pairs = []
    n = len(all_functions)
    for i in range(n):
        for j in range(i+1, n):
            if co_occurrence_matrix[i, j] > 0:
                pairs.append((all_functions[i], all_functions[j], co_occurrence_matrix[i, j]))
    
    # Sort and take top N
    pairs.sort(key=lambda x: x[2], reverse=True)
    for func1, func2, weight in pairs[:top_n]:
        G.add_edge(func1, func2, weight=weight)
    
    # Create the visualization
    plt.figure(figsize=(14, 10))
    pos = nx.spring_layout(G, seed=42)
    edge_weights = [G[u][v]['weight'] * 0.5 for u, v in G.edges()]
    
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, 
            font_size=8, font_weight='bold', edge_color='gray', 
            width=edge_weights, alpha=0.7)
    plt.title("Function Co-occurrence Network", fontsize=15)
    plt.tight_layout()
    plt.savefig("function_network.png", dpi=300, bbox_inches='tight')
    plt.show()

def find_sequential_patterns(function_calls, min_length=2, min_support=10):
    """
    Find common sequential patterns of function calls across solvers.
    
    Args:
        function_calls: Dictionary of function calls by solver
        min_length: Minimum length of pattern to consider
        min_support: Minimum number of solvers that must contain the pattern
        
    Returns:
        List of (pattern, frequency) tuples
    """
    all_sequences = list(function_calls.values())
    
    # Helper function to find all contiguous subsequences of a given length
    def find_subsequences(sequence, length):
        return [tuple(sequence[i:i+length]) for i in range(len(sequence)-length+1)]
    
    # Find all patterns of each length and count occurrences
    patterns = Counter()
    
    for length in range(min_length, min_length + 5):  # Look for patterns of increasing length
        for sequence in all_sequences:
            if len(sequence) >= length:
                subsequences = find_subsequences(sequence, length)
                patterns.update(subsequences)
    
    # Filter to patterns that appear in at least min_support solvers
    common_patterns = [(pattern, count) for pattern, count in patterns.items() 
                      if count >= min_support]
    
    # Sort by frequency then by length
    common_patterns.sort(key=lambda x: (-x[1], -len(x[0])))
    
    return common_patterns

def analyze_pattern_transitions(function_calls):
    """
    Analyze transitions between function calls to find common workflows.
    
    Args:
        function_calls: Dictionary of function calls by solver
        
    Returns:
        Dictionary mapping (func1, func2) transitions to counts
    """
    transitions = Counter()
    
    for solver, calls in function_calls.items():
        # Count transitions between consecutive functions
        for i in range(len(calls) - 1):
            transition = (calls[i], calls[i+1])
            transitions[transition] += 1
    
    return transitions

def find_function_roles(function_calls, transitions):
    """
    Identify common roles of functions (starter, middle, finisher)
    
    Args:
        function_calls: Dictionary of function calls by solver
        transitions: Dictionary of transitions between functions
        
    Returns:
        Dictionaries of starter, middle, and finisher functions with counts
    """
    starters = Counter()  # Functions that often start a sequence
    finishers = Counter()  # Functions that often end a sequence
    middle_nodes = Counter()  # Functions that connect many other functions
    
    for solver, calls in function_calls.items():
        if len(calls) > 0:
            starters[calls[0]] += 1
            finishers[calls[-1]] += 1
    
    # Find functions that act as connectors (have many in and out connections)
    function_in_degree = defaultdict(int)
    function_out_degree = defaultdict(int)
    
    for (source, target), count in transitions.items():
        function_out_degree[source] += count
        function_in_degree[target] += count
    
    # Functions with high in-degree and out-degree are likely "middle" functions
    for func in set(function_in_degree.keys()) | set(function_out_degree.keys()):
        in_deg = function_in_degree.get(func, 0)
        out_deg = function_out_degree.get(func, 0)
        if in_deg > 0 and out_deg > 0:
            middle_nodes[func] = in_deg * out_deg  # Product reflects connector importance
    
    return starters, middle_nodes, finishers

def visualize_pattern_heatmap(patterns, top_n=50):
    """
    Visualize the most common function patterns as a heatmap.
    
    Args:
        patterns: List of (pattern, frequency) tuples
        top_n: Number of top patterns to display
    """
    if not patterns:
        print("No patterns to visualize.")
        return
        
    top_patterns = patterns[:top_n]
    
    # Extract pattern strings and frequencies
    pattern_strings = [' → '.join(pattern) for pattern, _ in top_patterns]
    frequencies = [count for _, count in top_patterns]
    
    # Create a heatmap-style visualization
    plt.figure(figsize=(12, 8))
    plt.barh(range(len(pattern_strings)), frequencies, color='skyblue')
    plt.yticks(range(len(pattern_strings)), pattern_strings)
    plt.xlabel('Frequency')
    plt.ylabel('Function Sequence')
    plt.title(f'Top {len(top_patterns)} Common Function Sequences')
    plt.tight_layout()
    plt.savefig("function_sequences.png", dpi=300, bbox_inches='tight')
    plt.show()

def visualize_workflow_diagram(transitions, roles, top_n=15):
    """
    Visualize the function workflow as a directed graph.
    
    Args:
        transitions: Counter of transitions between functions
        roles: Tuple of (starters, middle_nodes, finishers) dictionaries
        top_n: Number of top transitions to include
    """
    starters, middle_nodes, finishers = roles
    
    # Create directed graph
    G = nx.DiGraph()
    
    # Get top transitions
    top_transitions = sorted(transitions.items(), key=lambda x: x[1], reverse=True)[:top_n*2]
    
    # Add nodes and edges
    for (source, target), weight in top_transitions:
        G.add_node(source)
        G.add_node(target)
        G.add_edge(source, target, weight=weight)
    
    # Ensure we include top starters and finishers even if transitions are weak
    top_starters = [func for func, _ in starters.most_common(5)]
    top_finishers = [func for func, _ in finishers.most_common(5)]
    
    for func in top_starters + top_finishers:
        G.add_node(func)
    
    # Only keep the largest connected component
    if not nx.is_connected(G.to_undirected()):
        largest_cc = max(nx.connected_components(G.to_undirected()), key=len)
        G = G.subgraph(largest_cc).copy()
    
    # Node colors based on role
    node_colors = []
    for node in G.nodes():
        if node in top_starters and node in top_finishers:
            # Purple for nodes that are both starters and finishers
            color = '#9370DB'  # Medium purple
        elif node in top_starters:
            # Green for starter nodes
            color = '#66BB6A'  # Green
        elif node in top_finishers:
            # Red for finisher nodes
            color = '#EF5350'  # Red
        elif node in middle_nodes and middle_nodes[node] > np.mean(list(middle_nodes.values())):
            # Blue for important middle nodes
            color = '#42A5F5'  # Blue
        else:
            # Gray for regular nodes
            color = '#90A4AE'  # Gray
        node_colors.append(color)
    
    # Node sizes based on centrality
    centrality = nx.betweenness_centrality(G)
    node_sizes = [2000 * centrality[node] + 300 for node in G.nodes()]
    
    # Edge widths based on transition count
    edge_widths = [G[u][v]['weight'] / 5 for u, v in G.edges()]
    
    # Create the visualization
    plt.figure(figsize=(16, 10))
    pos = nx.spring_layout(G, k=0.3, seed=42)
    
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes, alpha=0.8)
    nx.draw_networkx_edges(G, pos, width=edge_widths, alpha=0.6, edge_color='gray', 
                           connectionstyle='arc3,rad=0.1', arrowsize=15)
    nx.draw_networkx_labels(G, pos, font_size=10)
    
    # Add a legend
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#66BB6A', markersize=10, label='Starter Functions'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#EF5350', markersize=10, label='Finisher Functions'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#9370DB', markersize=10, label='Start & Finish'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#42A5F5', markersize=10, label='Connector Functions')
    ]
    plt.legend(handles=legend_elements, loc='upper right')
    
    plt.title("Function Workflow Diagram", fontsize=18)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig("function_workflow.png", dpi=300, bbox_inches='tight')
    plt.show()

def main():
    file_path = "solvers_evo.py"
    function_calls = extract_function_calls(file_path)
    
    # 1. Extract co-occurrences and similarities (original functionality)
    all_functions, co_occurrence_matrix, similarity_matrix = calculate_function_associations(function_calls)
    
    print("Top associated function pairs:")
    top_pairs = find_top_associated_pairs(all_functions, co_occurrence_matrix, similarity_matrix)
    for i, (func1, func2, co_occur, similarity) in enumerate(top_pairs, 1):
        print(f"{i}. {func1} + {func2}: Co-occurrences={co_occur:.0f}, Similarity={similarity:.4f}")
    
    # Visualize the function network
    # visualize_function_network(all_functions, co_occurrence_matrix)
    
    # 5. NEW: Find and analyze sequential patterns
    print("\nCommon sequential patterns:")
    patterns = find_sequential_patterns(function_calls, min_length=2, min_support=10)
    for i, (pattern, count) in enumerate(patterns[:15], 1):
        print(f"{i}. {' → '.join(pattern)}: Appears in {count} solvers")
    
    # Analyze transitions between functions
    transitions = analyze_pattern_transitions(function_calls)
    print("\nTop function transitions:")
    for i, ((func1, func2), count) in enumerate(transitions.most_common(10), 1):
        print(f"{i}. {func1} → {func2}: {count} occurrences")
    
    # Identify function roles in workflows
    roles = find_function_roles(function_calls, transitions)
    starters, middle_nodes, finishers = roles
    
    print("\nCommon starter functions:")
    for func, count in starters.most_common(5):
        print(f"- {func}: Starts {count} solvers")
    
    print("\nCommon finisher functions:")
    for func, count in finishers.most_common(5):
        print(f"- {func}: Ends {count} solvers")
    
    # Visualize the sequential patterns
    visualize_pattern_heatmap(patterns)
    
    # Visualize the workflow
    visualize_workflow_diagram(transitions, roles)

if __name__ == "__main__":
    main()

