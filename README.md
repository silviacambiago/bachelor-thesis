
# Bachelor Thesis: Detecting Genome Inversions Using Sample-Specific Strings

[![Thesis Repository](https://img.shields.io/badge/GitHub-silviacambiago/bachelor--thesis-blue)](https://github.com/silviacambiago/bachelor-thesis/tree/main)

This repository contains the code and resources for my bachelor thesis on developing an algorithm to detect genomic inversions. The thesis addresses the computational problem of identifying inversions in DNA sequences, specifically in scenarios involving inverted duplications. This README provides an overview of the project, core components, and instructions on how to use the code.

---

## Project Overview

### Problem Statement
Inversions are mutations that occur when a DNA segment is reversed in orientation relative to a reference genome. The **Detecting-Inversions** problem in my thesis involves identifying these segments, referred to as **inversion breakpoints**, in a target sequence. By detecting inversions, this research contributes to understanding complex genomic variations and mutations.

### Algorithm
The algorithm developed for this project is optimized for handling DNA sequences, leveraging efficient pattern-matching techniques tailored for bioinformatics applications:
- **Suffix Array & LCP Array**: Initially explored for substring searching but later replaced with a **Knuth-Morris-Pratt (KMP)** approach, given its suitability for small DNA alphabets.
- **KMP Pattern Matching**: Utilized to locate specific segments, ensuring efficient inversion detection without redundant storage of middle segments.
- **Time Complexity**: The algorithm runs with a complexity of θ(r + n * m), where `r` is the reference length, `n` is the number of sample-specific strings, and `m` is the average length of the middle segment.

---

## Repository Structure

- **`input_duplications.py`**: Script for generating synthetic DNA samples with inserted inversions.
  - Parameters include reference length, target length, and indexes defining the inversion segment.
- **`main_algorithm.py`**: Contains the primary algorithm for detecting inversions within the generated sequences.
- **`utils/`**: Utility functions for sequence manipulation, sequence trimming, and sample generation.

---

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/silviacambiago/bachelor-thesis.git
   cd bachelor-thesis
   ```

2. **Generate Sample Data**:
   Use `input_duplications.py` to create a target sequence with inversions based on a given reference. Modify parameters as needed:
   ```bash
   python input_duplications.py --ref_length <REFERENCE_LENGTH> --target_length <TARGET_LENGTH> --start_idx <START_INDEX> --end_idx <END_INDEX>
   ```

3. **Run the Detection Algorithm**:
   Run `main_algorithm.py` to detect inversion breakpoints in the generated sequence:
   ```bash
   python main_algorithm.py --input_file <INPUT_FILE>
   ```

### Example Usage
To generate a sample and run the detection algorithm, you might use:
```bash
python input_duplications.py --ref_length 1000 --target_length 1500 --start_idx 200 --end_idx 400
python main_algorithm.py --input_file generated_sample.txt
```

---

## Key Concepts

- **Inversion**: A segment of DNA reversed in direction compared to the reference genome.
- **Inversion Breakpoint**: The boundary point where an inversion starts or ends, marking the transition between matching and inverted sequences.
- **KMP Algorithm**: Utilized to efficiently search for reversed segments within the reference sequence, optimizing for DNA's limited alphabet (A, C, T, G).

---

## Results and Conclusion

The algorithm successfully identifies inversion breakpoints in synthetic DNA samples, including cases with inverted duplications. The implementation showcases computational efficiency in detecting inversions, with applications for bioinformatics research and genomic studies.

---

## Future Work

Potential enhancements include extending the algorithm to handle larger, more complex genomes and integrating it with real-world genome datasets for broader applications in genetic variation studies.

---

## License

This project is licensed under the GNU General Public License. See the [LICENSE](LICENSE) file for details.

---

For more details, please refer to the full thesis document available in the repository.
