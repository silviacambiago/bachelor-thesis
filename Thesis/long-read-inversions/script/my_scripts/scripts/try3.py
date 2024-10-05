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
plt.figure(figsize=(10, 6))
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
plt.savefig('execution_time_vs_reference_length.png')
plt.show()

# ---- 2. Execution Time vs. Number of Inversions (Bar Plot) ----
short_inv_times = [execution_times['2 Short'][-1], execution_times['4 Short'][-1], execution_times['6 Short'][-1]]
long_inv_times = [execution_times['2 Long'][-1], execution_times['4 Long'][-1], execution_times['6 Long'][-1]]

bar_width = 0.35
index = np.arange(len(num_inversions))

fig, ax = plt.subplots(figsize=(8, 6))
bar1 = ax.bar(index, short_inv_times, bar_width, label='Short Inversions')
bar2 = ax.bar(index + bar_width, long_inv_times, bar_width, label='Long Inversions')

ax.set_xlabel('Number of Inversions')
ax.set_ylabel('Execution Time (s)')
ax.set_title('Execution Time vs. Number of Inversions')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(['2 Inversions', '4 Inversions', '6 Inversions'])
ax.legend()
ax.grid(True, axis='y', linestyle="--")

plt.tight_layout()
plt.savefig('execution_time_vs_num_inversions.png')
plt.show()

# ---- 3. Comparison of Short vs. Long Inversions (Box Plot) ----
data_short = [execution_times['2 Short'], execution_times['4 Short'], execution_times['6 Short']]
data_long = [execution_times['2 Long'], execution_times['4 Long'], execution_times['6 Long']]

fig, ax = plt.subplots(figsize=(10, 6))

# Combine data for each group of inversions
data_combined = data_short + data_long
labels = ['2 Short', '4 Short', '6 Short', '2 Long', '4 Long', '6 Long']

# Create the box plot
ax.boxplot(data_combined, patch_artist=True, labels=labels)
ax.set_ylabel('Execution Time (s)')
ax.set_title('Comparison of Short vs. Long Inversions')

plt.grid(True, axis='y', linestyle="--")
plt.tight_layout()
plt.savefig('short_vs_long_inversions.png')
plt.show()
