import time  # Import the time module

def read_fasta(file_path):
    """
    Reads a sequence from a FASTA file.

    Args:
    file_path (str): The path to the FASTA file.

    Returns:
    str: The sequence extracted from the FASTA file.
    """

    sequence = []
    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith('>'):
                sequence.append(line.strip())
    result = ''.join(sequence)
    return result


def check_reverted_sample_specific(indexes, lengths, sample_specific_strings, target, reference):
    """
    Checks for reverted sequences in the target string based on given sample-specific strings.

    Args:
    indexes (list of int): A list of start indices of sample-specific strings in the target.
    lengths (list of int): A list of lengths corresponding to sample-specific strings.
    sample_specific_strings (list of str): A list of sample-specific strings.
    target (str): The target string to search for reverted sequences.
    reference (str): The reference string for verification.

    Returns:
    list of str: List of reverted sequences found in the target string.
    """
    reverted = []

    # Ask the user to choose the boundaries
    l, r = choose_boundaries(len(sample_specific_strings))

    start_time = time.time()  # Start timing the inversion detection

    for i in range(l, r):
        j = indexes[i]
        k = indexes[i + 1]

        if j == -1 or k == -1:
            continue

        middle = target[j + lengths[i]:k]
        middle = revert_and_complement(middle)

        found, start = check_substring(reference, middle)

        if found:
            left_increment = 1
            while left_increment <= lengths[i] and (j + lengths[i] - left_increment) >= 0 and \
                    target[j + lengths[i] - left_increment] == revert_and_complement(
                    reference[start + len(middle) + left_increment - 1]):
                left_increment += 1

            left_breakpoint = target[j + lengths[i] - left_increment: j + lengths[i] - left_increment + 2]

            right_increment = 0
            while right_increment < (len(reference) - start - len(middle)) and \
                    (k + right_increment) < len(target) and \
                    target[k + right_increment] == revert_and_complement(
                    reference[start - 1 - right_increment]):
                right_increment += 1

            right_breakpoint = target[k + right_increment - 1: k + right_increment + 1]

            print(f"{left_breakpoint} and {right_breakpoint} are breakpoints of an inversion")

            inversion = target[j + lengths[i] - left_increment + 1: k + right_increment]
            reverted.append(inversion)

    end_time = time.time()  # End timing
    print(f"Time taken to execute: {end_time - start_time:.4f} seconds")

    return reverted


def build_sample_specific_data(target, file_path):
    """
    Builds three lists: one of indexes, one of lengths, and one of sample-specific strings from the target and specifics file.

    Args:
    target (str): The target string from which to extract sample-specific strings.
    file_path (str): The path to the specifics file.

    Returns:
    tuple of lists: A tuple containing three lists:
                    - List of start indexes
                    - List of lengths
                    - List of sample-specific strings.
    """

    indexes = []
    lengths = []
    sample_specific_strings = []

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip("\n").split("\t")

            n, s, l = parts[:3]  # Unpack the first three items
            s, l = int(s), int(l)

            # Add start index, length, and sample-specific string to the respective lists
            indexes.append(s)
            lengths.append(l)
            sample_specific_string = target[s:s + l]
            sample_specific_strings.append(sample_specific_string)

    return indexes, lengths, sample_specific_strings


def revert_and_complement(string):
    """
    Reverts and complements a DNA sequence.

    Args:
    string (str): The sequence to be reverted and complemented.

    Returns:
    str: The reverted and complemented sequence.
    """
    complements = {"A": "T", "C": "G", "G": "C", "T": "A"}
    reverse_complement = ""

    for i in range(len(string) - 1, -1, -1):
        base = string[i]
        complement = complements.get(base, base)  # handle unexpected characters
        reverse_complement += complement

    return reverse_complement


def kmp_prefix_function(pattern):
    """
    This function preprocesses the pattern to create the prefix (partial match) table.
    """
    m = len(pattern)
    lps = [0] * m  # Longest prefix suffix (LPS) array
    j = 0  # Length of the previous longest prefix suffix
    i = 1

    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def check_substring(reference, string):
    """
    Knuth-Morris-Pratt string matching algorithm.
    Returns True and the index of the first occurrence if the pattern is found, else returns False and -1.
    """
    n = len(reference)
    m = len(string)

    # Preprocess the pattern to get the longest prefix suffix array
    lps = kmp_prefix_function(string)

    i = 0  # Index for reference
    j = 0  # Index for string (pattern)

    while i < n:
        if string[j] == reference[i]:
            i += 1
            j += 1

        if j == m:
            return True, i - j  # Match found, return starting index of the match
        elif i < n and string[j] != reference[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return False, -1  # No match found


def choose_boundaries(max_length):
    """
    Allows the user to choose the start and end boundaries for the range of sample-specific strings to analyze.

    Args:
    max_length (int): The maximum index (length of the sample-specific strings list) to ensure valid input.

    Returns:
    tuple of int: The start and end indices for the range.
    """
    while True:
        try:
            start = int(input(f"Start index (0 to {max_length - 2}): "))
            end = int(input(f"End index ({start + 1} to {max_length - 1}): "))

            if 0 <= start < end < max_length:
                return start, end
            else:
                print(f"Invalid input. Ensure 0 <= start < end < {max_length}.")
        except ValueError:
            print("Invalid input. Please enter integer values.")


# Test the function
reference_file = "reference.fa"
target_file = "target.fa"
specifics_file = "specifics.txt"

reference = read_fasta(reference_file)
target = read_fasta(target_file)

indexes, lengths, sample_specific_strings = build_sample_specific_data(target, specifics_file)
inverted_sequences = check_reverted_sample_specific(indexes, lengths, sample_specific_strings, target, reference)

print("Inverted Sequences:", inverted_sequences)