"""
Author: Kaan Tekin Öztekin

Description:
    This script computes and visualizes the probability density function (PDF)
    of an exponential random variable for multiple rate parameters λ.

    For λ values {0.3, 1, 3}, the script evaluates:
        f_X(x) = λ e^{-λx}
    over the interval x ∈ [0, 10], and plots all three curves on the same figure
    to illustrate how the rate parameter λ affects the shape of the exponential PDF.

    All plots are saved into the 'outputs/' directory.

Structure:
    - main():
         * Defines λ values and x-range
         * Computes exponential PDFs
         * Plots each PDF with appropriate labels
         * Saves the final figure in outputs/exponential_pdf.png
"""

import numpy as np
import matplotlib.pyplot as plt
import os

def main():
    # define lambda values
    lambda_values = [0.3, 1, 3]

    # define x range
    x = np.linspace(0, 10, 1000)

    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)
    plt.figure(figsize=(8, 5))

    for lam in lambda_values:
        f_x = lam * np.exp(-lam * x)
        plt.plot(x, f_x, label=f"$\\lambda = {lam}$")

    plt.xlabel("x (time)")
    plt.ylabel("f_X(x)")
    plt.title("Exponential PDF for different $\\lambda$")
    plt.grid(True)
    plt.legend()

    output_path = os.path.join(output_dir, "exponential_pdf.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight')

    print(f"Plot has been saved to: {output_path}")
    plt.show()


if __name__ == "__main__":
    main()