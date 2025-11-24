"""
Author: Kaan Tekin Öztekin

Description:
    This script computes the probability that a specific pattern of six
    consecutive flips "HHHHH T" (5 Heads followed by 1 Tail) appears at
    least once within a sequence of 10 independent fair coin tosses.

    The code divides all valid occurrences into three cases:
        1. Start-run:   Pattern appears at positions 1–6.
        2. Middle-run:  Pattern appears starting at positions 2–5.
        3. End-run:     Pattern appears at positions 5–10.

    For each case, the number of free bits is computed.
    The total number of valid sequences is summed and then divided by
    the total possible sequences (2^10) to obtain the final probability.

Structure:
    - main():
         * Computes number of valid sequences for each case.
         * Computes total valid sequences.
         * Computes probability using 2^10 total outcomes.
         * Prints formatted results.
"""


def main():
    p = 0.5
    # --- START RUN ---
    # Pattern: HHHHHTxxxx  (positions 1–5 = H, position 6 = T)
    # Free bits: 4 positions -> 2^4 possible sequences
    count_start = 2**4

    # --- END RUN ---
    # Pattern: xxxxTHHHHH  (position 5 = T, positions 6–10 = H)
    # Free bits: 4 positions -> 2^4 possible sequences
    count_end = 2**4

    # --- MIDDLE RUNS ---
    # Patterns:
    # i = 2 : xTHHHHHTxxx
    # i = 3 : xxTHHHHHTxx
    # i = 4 : xxxTHHHHHTx
    # i = 5 : xxxxTHHHHHT
    #
    # Each has 3 free bits -> 2^3 possible sequences
    # 4 possible start positions -> multiply by 4
    count_middle = 4 * (2**3)
    valid_sequences = count_start + count_middle + count_end
    total_sequences = 2**10
    probability = valid_sequences / total_sequences

    print("Valid sequences (start) :", count_start)
    print("Valid sequences (middle):", count_middle)
    print("Valid sequences (end)   :", count_end)
    print("-------------------------------------------")
    print("Total valid sequences   :", valid_sequences)
    print("Total possible sequences:", total_sequences)
    print("Final probability       :", probability)

if __name__ == "__main__":
    main()