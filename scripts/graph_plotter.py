import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
reference_lengths = [50000, 100000, 1000000, 10000000]
execution_times = {
    '2 Short': [0.0188, 0.0353, 0.3009, 2.9765],
    '2 Long': [0.0260, 0.0400, 0.3029, 3.0082],
    '4 Short': [0.0407, 0.0828, 0.7305, 7.3140],
    '4 Long': [0.0459, 0.0934, 0.8364, 7.6067],
    '6 Short': [0.0721, 0.1336, 1.2190, 11.8296],
    '6 Long': [0.0758, 0.1396, 1.2535, 12.1238]
}
num_inversions = [2, 4, 6]
execution_times_2_inv = [execution_times['2 Short'], execution_times['2 Long']]
execution_times_4_inv = [execution_times['4 Short'], execution_times['4 Long']]
execution_times_6_inv = [execution_times['6 Short'], execution_times['6 Long']]

# ---- 1. Execution Time vs. Reference Length (Line Plot) ----
plt.figure(figsize=(10, 6), facecolor='none')  # Set facecolor to 'none' for no background
ax = plt.gca()
ax.set_facecolor('none')  # Ensure the axes have no background

for key, values in execution_times.items():
    plt.plot(reference_lengths, values, label=key, marker='o')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Reference Length (log scale)')
plt.ylabel('Execution Time (s, log scale)')
plt.title('Execution Time vs. Reference Length')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.tight_layout()

# Save figure without a background
plt.savefig('execution_time_vs_reference_length.png', transparent=True, facecolor='none')

plt.show()
