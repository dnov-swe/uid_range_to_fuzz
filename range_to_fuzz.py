#!/usr/bin/python3

#A script able for generating a file for e.g. rfid fuzzing with your Flipper Zero
#DON'T DO CRIMES!

import sys

def generate_hex_sequence(prefix, n1, n2):
    sequence = []
    for i in range(n1, n2 + 1):
        formatted_number = f"{prefix}{i:02X}"  # Convert to uppercase hexadecimal
        sequence.append(formatted_number)
    return sequence

def write_sequence_to_file(sequence, filename):
    with open(filename, "w") as file:
        for item in sequence:
            file.write(item + "\n")

def main():
    if len(sys.argv) != 5:
        print("Usage: range_to_fuzz.py prefix starting_number ending_number output_filename")
        return
    p = sys.argv[1]
    n1 = int(sys.argv[2], 16)
    n2 = int(sys.argv[3], 16)
    output_filename = sys.argv[4]

    result = generate_hex_sequence(p, n1, n2)
    write_sequence_to_file(result, output_filename)
    print("Sequence written to", output_filename)

if __name__ == "__main__":
    main()
