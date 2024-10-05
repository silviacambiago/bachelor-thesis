def check_reverted_sample_specific(indexes, lengths, sample_specific_strings, target, reference):
    """
    Checks for reverted sequences in the target string based on given sample specific strings.

    Args:
    indexes (list of int): a list of start indices of sample specific strings in the target
    lengths (list of int): a list of lengths corresponding to sample specific strings
    sample_specific_strings (list of str): a list of sample specific strings
    target (str): the target string to search for reverted sequences
    reference (str): the reference string for verification

    Returns:
    list of str: list of reverted sequences found in the target string
    """
    reverted = []

    # Choose boundaries within the list of sample-specific strings
    l, r = choose_boundaries(len(sample_specific_strings))

    # Iterate through each pair of consecutive sample-specific strings within the chosen boundaries
    for i in range(l, r):
        # Find positions of the previous and current strings within the target
        j = indexes[i]
        k = indexes[i + 1]

        # Check if both substrings are found in the target
        if j == -1 or k == -1:
            continue

        segments = generate_segments(j, k, sample_specific_strings[i], sample_specific_strings[i + 1], target)

        # Iterate through segments
        for segment in segments:
            reverse = revert_and_complement(segment)

            # Calculate new target by replacing the segment with its reverse complement
            new_target = target.replace(segment, reverse)
            target_trimmed = new_target[j:k + lengths[i + 1]]

            left_breakpoint = target[find_position(target, segment) - 1:find_position(target, segment) + 1]
            right_breakpoint = target[
                               find_position(target, segment) + len(segment) - 1:find_position(target, segment) + len(
                                   segment) + 1]

            # Check if the inverted sequence exists in the reference
            if check_substring(reference, target_trimmed):
                reverted.append(segment)
                # Print breakpoints of an inversion
                print(f"{left_breakpoint} and {right_breakpoint} are breakpoints of an inversion")

    return reverted

def find_position(text, pattern):
    """
    Finds the position of a pattern within a text using the Karp-Rabin algorithm

    Args:
    text (str): The text to search within
    pattern (str): The pattern to search for

    Returns:
    int: the starting index of the pattern in the text if found, -1 otherwise
    """
    d = 256
    q = 10 ** 9 + 7
    m = len(pattern)
    n = len(text)

    if m > n:
        return -1

    d_raised_to_m_minus_1 = pow(d, m - 1, q)

    p = 0
    h = 0

    # Calculate hash value of the pattern and the first substring of the text
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        h = (d * h + ord(text[i])) % q

    # Slide the pattern over the text and compare hash values
    for i in range(n - m + 1):
        if p == h:
            if text[i:i + m] == pattern:
                return i

        # Update hash value for the next substring
        if i < n - m:
            h = (d * (h - ord(text[i]) * d_raised_to_m_minus_1) + ord(text[i + m])) % q
            h = (h + q) % q  # Ensure h is positive

    return -1

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
                    - List of sample-specific strings
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
    string (str): the sequence to be reverted and complemented

    Returns:
    str: the reverted and complemented sequence
    """
    complements = {"A": "T", "C": "G", "G": "C", "T": "A"}
    reverse_complement = ""

    for i in range(len(string) - 1, -1, -1):
        base = string[i]
        complement = complements.get(base, base)  # handle unexpected characters
        reverse_complement += complement

    return reverse_complement


def check_substring(reference, string):
    """
    Checks if a string is a substring of another string using a suffix array.

    Args:
    reference (str): the string to search within
    string (str): the string to search for

    Returns:
    bool: True if the string is found within the reference string, False otherwise
    """
    suffix_array = sorted([reference[i:] for i in range(len(reference))])

    left, right = 0, len(suffix_array)
    while left < right:
        mid = (left + right) // 2
        if suffix_array[mid] < string:
            left = mid + 1
        else:
            right = mid
    if left < len(suffix_array) and suffix_array[left].startswith(string):
        return True
    return False


def generate_segments(j, k, start, end, target):
    segments = []
    for m in range(1, len(start)):
        for n in range(1, len(end)):
            if j + m <= k and k + n <= len(target):
                segments.append(target[j + m:k + n])
    return segments


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
file_path = "specifics.txt"
target = "ACGTAACCC"
reference = "ACGGTTACCGTTAGC"
indexes, lengths, sample_specific_strings = build_sample_specific_data(target, file_path)

inverted_sequences = check_reverted_sample_specific(indexes, lengths, sample_specific_strings, target, reference)
print("Inverted Sequences:", inverted_sequences)
