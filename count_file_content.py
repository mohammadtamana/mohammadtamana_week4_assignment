def count_file_content(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            lines = file.readlines()
        
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)
        
        with open(output_filename, 'w') as output_file:
            output_file.write(f"Number of lines: {num_lines}\n")
            output_file.write(f"Number of words: {num_words}\n")
            output_file.write(f"Number of characters: {num_chars}\n")
        
        print(f"Results written to {output_filename}")
    
    except FileNotFoundError:
        print(f"The file {input_filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
input_filename = 'input.txt'    # Replace with your input file path
output_filename = 'output.txt'  # Replace with your desired output file path
count_file_content(input_filename, output_filename)