import re
import csv

# Initialize dictionaries
error_dict = {}
user_dict = {}

# Parse through syslog.log file
with open('syslog.log', 'r') as file:
    for line in file:
        # Check if the log entry matches INFO or ERROR format
        if re.search(r'INFO', line):
            # Extract username from the log entry
            username = re.search(r"\((.*?)\)", line).group(1)
            print(username)
            # Update user_dict with INFO entry
            if username in user_dict:
                user_dict[username][0] += 1
            else:
                user_dict[username] = [1, 0]
        elif re.search(r"ERROR", line):
            # Extract error message from the log entry
            error = re.search(r"ERROR ([\w\s']+)", line).group(1)
            print(error)
            # Update error_dict with ERROR entry
            if error in error_dict:
                error_dict[error] += 1
            else:
                error_dict[error] = 1

# Sort dictionaries
sorted_error_dict = sorted(error_dict.items(), key=lambda x: x[1], reverse=True)
sorted_user_dict = sorted(user_dict.items())

# Create error_message.csv
with open('error_message.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Error", "Count"])
    writer.writerows(sorted_error_dict)

# Create user_statistics.csv
with open('user_statistics.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Username", "INFO", "ERROR"])
    for username, counts in sorted_user_dict:
        writer.writerow([username, counts[0], counts[1]])
