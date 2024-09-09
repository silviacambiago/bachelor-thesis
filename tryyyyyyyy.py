import random

def generate_dna_string(length):
    """
    Generates a random DNA string of the specified length.

    Args:
    length (int): The length of the DNA string to generate.

    Returns:
    str: A randomly generated DNA string.
    """
    nucleotides = ['A', 'T', 'C', 'G']
    dna_string = ''.join(random.choice(nucleotides) for _ in range(length))
    return dna_string

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
        complement = complements.get(base, base)
        reverse_complement += complement

    return reverse_complement

def insert_multiple_reverted_complements(dna_string, segments):
    """
    Inserts multiple reverted and complemented segments into the DNA string.

    Args:
    dna_string (str): the original DNA string
    segments (list of tuples): each tuple contains the start and end index of the substring to revert and complement

    Returns:
    str: The DNA string with the specified parts reverted and complemented.
    """
    # Sort segments by start index in descending order to avoid index shifting
    segments = sorted(segments, key=lambda x: x[0], reverse=True)

    # For each segment, revert and complement the specified part
    for start, end in segments:
        substring = dna_string[start:end]
        reverted_complemented = revert_and_complement(substring)
        dna_string = dna_string[:start] + reverted_complemented + dna_string[end:]

    return dna_string

# Example usage
length = 100000  # Length of the DNA string
random_dna = generate_dna_string(length)
print(f"Original DNA string: {random_dna}")

# Define multiple ranges for reverting and complementing parts of the string
segments = [(100, 250), (500, 634)]  # Each tuple is a start and end index

# Insert multiple reverted and complemented segments
modified_dna = insert_multiple_reverted_complements(random_dna, segments)

print(f"DNA string with multiple reverted and complemented segments: {modified_dna}")
