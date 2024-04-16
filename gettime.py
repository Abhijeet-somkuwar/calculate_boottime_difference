import argparse
import re

def parse_log_file(log_file):
    start_times = []
    end_times = []

    # Regular expression pattern to extract time in nanoseconds
    pattern = r'\d+'

    with open(log_file, 'r') as file:
        for line in file:
            if 'Start time' in line:                   #can change 'Start time' with the required Str to get there corresponding one or more digits (pattern)
                match = re.findall(pattern, line)
                if match:
                    start_times.append(int(match[0]))
            elif 'End time' in line:                   #can change 'End time' with the required Str to get there corresponding one or more digits (pattern)
                match = re.findall(pattern, line)
                if match:
                    end_times.append(int(match[0]))

    return start_times, end_times


def calculate_time_differences(start_times, end_times):
    time_differences = [end - start for start, end in zip(start_times, end_times)]
    return time_differences

def format_time_difference(time_ns):
    time_ms = time_ns / 10**6
    time_sec = time_ns / 10**9
    return time_ns, time_ms, time_sec

def main():
    parser = argparse.ArgumentParser(description='Calculate time differences from a log file.')
    parser.add_argument('log_file', type=str, help='Path to the log file')

    args = parser.parse_args()

    log_file = args.log_file

    # Check if the file path is correct
    try:
        with open(log_file, 'r') as file:
            # Check if the file is empty
            if file.read().strip() == '':
                print("Error: The provided file is empty.")
                return

    except FileNotFoundError:
        print("Error: The provided file not found.")
        return

    start_times, end_times = parse_log_file(log_file)

    # Check if the log file contains "Start time" and "End time"
    if not start_times or not end_times:
        print("Error: The provided file does not contain 'Start time' or 'End time' entries.")
        return

    time_differences = calculate_time_differences(start_times, end_times)

    print("Time differences:")
    for time_diff in time_differences:
        ns, ms, sec = format_time_difference(time_diff)
        print(f"  Difference: {ns} ns, {ms} ms, {sec} sec")

if __name__ == "__main__":
    main()
