import logging

# Set up logging configuration
logging.basicConfig(filename='error_log.txt', 
                    level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def process_data(input_filename):
    try:
        with open(input_filename, 'r') as file:
            lines = file.readlines()
        
        # Attempt to convert lines to integers and compute the sum
        numbers = [int(line.strip()) for line in lines]
        total_sum = sum(numbers)
        print(f"The sum of numbers is: {total_sum}")

    except FileNotFoundError:
        error_message = f"The file '{input_filename}' was not found."
        print(error_message)
        logging.error(error_message)
    
    except ValueError as e:
        error_message = f"Value error occurred: {e}. Ensure the file contains only integers."
        print(error_message)
        logging.error(error_message)

    except Exception as e:
        error_message = f"An unexpected error occurred: {e}"
        print(error_message)
        logging.error(error_message)

# Main section
if __name__ == '__main__':
    input_filename = 'numbers.txt'  # Replace with your input file path
    process_data(input_filename)