import csv

def calculate_averages(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            reader = csv.DictReader(infile)
            student_averages = []

            for row in reader:
                # Extract student's name and their grades
                student_name = row['Name']
                grades = [float(row[subject]) for subject in row if subject != 'Name']
                
                # Calculate the average grade
                average_grade = sum(grades) / len(grades)
                student_averages.append({'Name': student_name, 'Average': average_grade})
        
        # Write the results to a new CSV file
        with open(output_filename, 'w', newline='') as outfile:
            fieldnames = ['Name', 'Average']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(student_averages)
        
        print(f"Averages written to {output_filename}")
    
    except FileNotFoundError:
        print(f"The file {input_filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main section
if __name__ == '__main__':
    input_filename = 'grades.csv'    # Replace with your input CSV file path
    output_filename = 'averages.csv' # Replace with your desired output CSV file path
    calculate_averages(input_filename, output_filename)