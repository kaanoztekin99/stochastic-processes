import numpy as np
import matplotlib.pyplot as plt
import os

# Generate n IID Uniform(0,1) random variables
def generate_uniform_samples(n):
    return np.random.uniform(0, 1, n)

# Plot estimated CDF (FINAL)
def plot_cdf(x_sorted, n):
    y = np.arange(1, n + 1) / n

    # Add (0,0) so the curve starts at the real origin
    x_plot = np.concatenate(([0], x_sorted))
    y_plot = np.concatenate(([0], y))

    fig, ax = plt.subplots(figsize=(6, 4))

    # Step plot starting exactly at origin
    ax.step(x_plot, y_plot, where='pre', label=f"Estimated CDF (n={n})")

    # True CDF
    ax.plot([0, 1], [0, 1], 'r--', label="True CDF: F(x)=x")

    # --- CRITICAL PART: Fix axis to make corner EXACT ---
    # No padding
    ax.margins(x=0, y=0)
    # Force axes to start at zero exactly
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    # Move bottom and left axes to real origin
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    # Hide the top and right borders
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    # Make ticks visible on the axes
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_xlabel("x")
    ax.set_ylabel("F(x)")
    ax.set_title(f"Estimated CDF for n = {n}")
    ax.legend()
    ax.grid(True)

    return fig

# Save plot into output folder
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