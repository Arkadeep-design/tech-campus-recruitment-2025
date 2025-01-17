import os
import sys

def extract_logs(input_file_path, output_file_path, date):
    """
    it extracts the log entries for specified date
    1) first of all it opens input file path in read view and create a new output_file as write view
    2) then it checks line by line in the input_file, if the log entrie matches with the specified date it appends the entry 
       in the output file And also increases the count of lines
    3) If lines_written is 0, it will print that logs were not found for specified date
    4) Handling FileNotFound Exceptions separately
    """
    try:
        with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
            lines_written = 0

            for line in input_file:
                if line.startswith(date):
                    output_file.write(line)
                    lines_written += 1

            if lines_written == 0:
                print(f"Warning: No logs found for the date {date}.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py <YYYY-MM-DD>")
        sys.exit(1)

    date = sys.argv[1]

    if len(date) != 10 or date[4] != '-' or date[7] != '-':
        print("Error: Invalid date format. Expected YYYY-MM-DD.")
        sys.exit(1)

    input_file_path = 'logs_2024.txt'  # input file in the same directory
    output_directory = '../output'
    output_file_path = os.path.join(output_directory, f'output_{date}.txt')

    # it checks if output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # it extracts the log file
    extract_logs(input_file_path, output_file_path, date)

    print(f"Logs for {date} have been written to: {output_file_path}")
    
if __name__ == "__main__":
    main()
