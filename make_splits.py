from collections import defaultdict
from math import floor
from os import walk, makedirs
from os.path import join, isdir, abspath, split, exists
from shutil import move, copy, rmtree
from tqdm import tqdm


def make_splits(k=10):
    """Returns a dict of k stratified random splits on the folder names (e.g. {1: {'GB01a', 'GB122b', ..., k: {...}}})
    Deterministic as the data is not shuffled."""

    with open('./corpus/original/truth.txt', 'r') as f:
        content = f.readlines()
    truthPairs = [line.strip().split() for line in content]

    # Split into two lists for the classes
    same = [pair[0] for pair in truthPairs if pair[1] == 'Y']
    diff = [pair[0] for pair in truthPairs if pair[1] == 'N']
    same_range = range(floor(len(same)/k))
    diff_range = range(floor(len(diff)/k))

    # Make k splits
    splits = {}
    for i in range(k):  # make k lists
        for _ in same_range:
            splits[same.pop(0)] = i
        for _ in diff_range:
            splits[diff.pop(0)] = i
        #splits[i].extend([same.pop(0) for _ in same_range])
        #splits[i].extend([diff.pop(0) for _ in diff_range])

    # Append rest of the items
    # The used dataset has len(same) = 132, len(diff) = 130
    # Might not be the best because it starts at the first split for both classes 
    # again and might skew the class ratios arbitrarily (esp. for small splits)
    for i in range(len(same)):
        splits[same.pop(0)] = i
        #splits[i].append(same.pop(0))
    for i in range(len(diff)):
        splits[diff.pop(0)] = i
        #splits[i].append(diff.pop(0))

    return splits

def split_dataset(k=10):
    splits = make_splits(k)
    # Go  through dataset folder
    # For each split i copy the corresponding folder to ./corpus/split/original/i/GBXXXX

    # Later: Write wrapper around unmasking framework that fuses all but the test split and evaluates the algorithm