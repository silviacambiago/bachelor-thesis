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
    for start, end in segments:
        substring = dna_string[start:end]
        reverted_complemented = revert_and_complement(substring)
        dna_string = dna_string[:start] + reverted_complemented + dna_string[end:]

    return dna_string

def trim_to_target_length(dna_string, target_length):
    """
    Trims the reference DNA string to the desired target length.

    Args:
    dna_string (str): the original reference DNA string
    target_length (int): the desired length of the target sequence

    Returns:
    str: The trimmed DNA string.
    """
    ref_length = len(dna_string)
    trim_amount = (ref_length - target_length) // 2
    return dna_string[trim_amount:ref_length - trim_amount]

def write_fasta(filename, header, sequence):
    """
    Writes a DNA sequence to a FASTA file.

    Args:
    filename (str): The name of the file to write to.
    header (str): The header for the FASTA file.
    sequence (str): The DNA sequence to write.
    """
    with open(filename, 'w') as fasta_file:
        fasta_file.write(f">{header}\n")
        # Write the sequence in lines of 80 characters
        for i in range(0, len(sequence), 80):
            fasta_file.write(sequence[i:i+80] + '\n')

# Example usage
reference_length = 100000  # Length of the reference DNA string
target_length = 50000      # Length of the target DNA string

# Generate reference DNA
random_dna = generate_dna_string(reference_length)
print("Generated random DNA sequence.")

# Trim reference DNA to match the desired target length
if target_length >= reference_length:
    raise ValueError("Target length must be smaller than the reference length.")

trimmed_target_dna = trim_to_target_length(random_dna, target_length)

# Define multiple ranges for reverting and complementing parts of the trimmed target
segments = [(27000, 33500), (43000, 49500)] # Each tuple is a start and end index

# Insert multiple reverted and complemented segments into the target
modified_target_dna = insert_multiple_reverted_complements(trimmed_target_dna, segments)
print("Target DNA string modified with reverted and complemented segments.")

# Write original and modified sequences to FASTA files
write_fasta("reference.fa", "R", random_dna)
write_fasta("target.fa", "T", modified_target_dna)

print("FASTA files 'reference.fa' and 'target.fa' have been created.")