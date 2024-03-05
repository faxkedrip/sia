import os
import sys
import re

if len(sys.argv) != 5:
    print("Usage: copy.py [input_directory] [output_directory] [input_extension] [increase_value]")
    sys.exit(1)

input_dir = sys.argv[1]
output_dir = sys.argv[2]
input_extension = sys.argv[3]
increase_value = sys.argv[4]

number_pattern = re.compile(r"\d+")

for filename in os.listdir(input_dir):
    if filename.endswith("." +input_extension):
        output_filename = os.path.join(output_dir, os.path.splitext(filename)[0] + "_processed.txt")

        with open(os.path.join(input_dir, filename), "r") as input_file:
            processed_data = []
            for line in input_file:
                numbers = number_pattern.findall(line)
                for number in numbers:
                    processed_data.append(int(number) + int(increase_value))

        with open(output_filename, "w") as output_file:
            for data in processed_data:
                output_file.write(str(data) + "\n")

        print(f"Input file '{filename}' processed and saved to '{output_filename}'")