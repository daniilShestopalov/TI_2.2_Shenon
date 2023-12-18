import math

import numpy

class ShannonFanoNode:
    def __init__(self, symbols, probabilities):
        self.symbols = symbols
        self.probabilities = probabilities
        self.left = None
        self.right = None


def balanced_partition(probabilities):
    """
    Partition the probabilities into two groups with approximately equal sums.
    """
    total = sum(probabilities)
    half = total / 2
    n = len(probabilities)

    closest_diff = float('inf')
    best_partition_index = 0
    current_sum = 0

    for i in range(n):
        current_sum += probabilities[i]
        if abs(half - current_sum) < closest_diff:
            closest_diff = abs(half - current_sum)
            best_partition_index = i + 1

    return best_partition_index


def shannon_fano_stepwise(symbols, probabilities):
    if len(symbols) == 1:
        return ShannonFanoNode(symbols, probabilities)

    # Step 1: Sort symbols in descending order of probabilities
    sorted_indices = sorted(range(len(probabilities)), key=lambda k: probabilities[k], reverse=True)
    sorted_symbols = [symbols[i] for i in sorted_indices]
    sorted_probabilities = [probabilities[i] for i in sorted_indices]

    # Step 2: Split the symbols into two groups with nearly equal total probabilities
    index = balanced_partition(sorted_probabilities)

    node = ShannonFanoNode(sorted_symbols, sorted_probabilities)

    # Step 3: Assign '0' to left group and '1' to right group
    node.left = shannon_fano_stepwise(sorted_symbols[:index], sorted_probabilities[:index])
    node.right = shannon_fano_stepwise(sorted_symbols[index:], sorted_probabilities[index:])
    return node

def entropy(probabilities):
    return -sum([p * numpy.log2(p) for p in probabilities.values() if p > 0])

def average_code_length(probabilities, shannon_codes):
    return sum([probabilities[symbol] * len(shannon_codes[symbol]) for symbol in probabilities])

def check_probabilities(probabilities):
    total = sum(probabilities.values())
    if not math.isclose(total, 1.0, rel_tol=1e-9):
        raise ValueError(f"Sum of probabilities is {total}, but should be close to 1.")