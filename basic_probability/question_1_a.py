"""
Author: Kaan Tekin Öztekin

Description:
    This script implements Algorithm 1 from the assignment.
    It generates n IID Uniform(0,1) random samples, computes their
    estimated CDF, and compares it with the true CDF F(x) = x.
    The script produces CDF plots for n = 10, 100, and 1000.
    All plots are saved into the 'outputs/' directory.

Structure:
    - generate_uniform_samples(n): Generates Uniform(0,1) random samples.
    - plot_cdf(x_sorted, n): Plots the empirical CDF with proper axis alignment.
    - save_plot(fig, filename): Saves figures into the outputs folder.
    - algorithm1(): Executes the full pipeline for n = {10, 100, 1000}.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Generate n IID Uniform(0,1) random variables
def generate_uniform_samples(n):
    return np.random.uniform(0, 1, n)

# Plot estimated CDF (FINAL)
def plot_cdf(x_sorted, n):
    y = np.arange(1, n + 1) / n
    x_plot = np.concatenate(([0], x_sorted))
    y_plot = np.concatenate(([0], y))
    fig, ax = plt.subplots(figsize=(6, 4))

    ax.step(x_plot, y_plot, where='pre', label=f"Estimated CDF (n={n})")

    ax.plot([0, 1], [0, 1], 'r--', label="True CDF: F(x)=x")
    ax.margins(x=0, y=0)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_xlabel("x")
    ax.set_ylabel("F(x)")
    ax.set_title(f"Estimated CDF for n = {n}")
    ax.legend()
    ax.grid(True)

    return fig

def save_plot(fig, filename):
    os.makedirs("outputs", exist_ok=True)
    filepath = os.path.join("outputs", filename)
    fig.savefig(filepath, dpi=300, bbox_inches="tight")
    plt.close(fig)

# Algorithm 1 - Pseudocode implementation
def algorithm1():
    n_values = [10, 100, 1000]

    for n in n_values:
        samples = generate_uniform_samples(n)
        x_sorted = np.sort(samples)
        fig = plot_cdf(x_sorted, n)
        save_plot(fig, f"cdf_n_{n}.png")

    print("All CDF plots saved in the 'outputs/' directory.")


if __name__ == '__main__':
    algorithm1()