"""
Author: Kaan Tekin Öztekin

Description:
    This script implements the Markov queue simulation described in the assignment.
    At each time step, one customer is serviced (removed from the queue), while new
    arrivals follow a Poisson distribution with rate λ = 0.85. The queue length is
    updated over N = 10,000 time units and the empirical queue length distribution
    is visualized using a histogram.

    The script models the queue as a discrete-time Markov process:
        queue_length(t+1) = max(queue_length(t) - 1, 0) + Poisson(λ)

    All generated figures are saved in the 'outputs/' directory.

Structure:
    - run_simulation(lambda_rate, N, queue_length):
         Simulates the Markov queue and returns the list of queue lengths.
    - plot_distribution(data):
         Plots and saves the histogram of the queue length distribution.
    - main():
         Defines parameters, runs the simulation, and generates the plot.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

def run_simulation(lambda_rate, N, queue_length):

    queue_length_distribution = []

    for i in range(N):
        arrivals = np.random.poisson(lambda_rate)    # New arrivals
        queue_length = max(queue_length - 1, 0)      # Service
        queue_length += arrivals                     # Update
        queue_length_distribution.append(queue_length)

    return queue_length_distribution


def plot_distribution(data):
    os.makedirs("outputs", exist_ok=True)

    plt.hist(data, bins=30, edgecolor='black')
    plt.title("Queue Length Distribution (λ = 0.85)")
    plt.xlabel("Queue Length")
    plt.ylabel("Frequency")
    plt.grid(True)

    plt.xlim(left=0)
    plt.ylim(bottom=0)

    output_path = "outputs/queue_length_distribution.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.show()
    print(f"Histogram saved to: {output_path}")


def main():
    lambda_rate = 0.85
    N = 10000
    queue_length = 0

    queue_data = run_simulation(lambda_rate, N, queue_length)
    plot_distribution(queue_data)


if __name__ == "__main__":
    main()