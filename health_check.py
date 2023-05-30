
#!/usr/bin/env python3
import psutil
import socket
import time
import os
from emails import generate_error_report,send

sender="automation@example.com"
recipient="{}@example.com".format(os.environ.get('USER'))
body = "Please check your system and resolve the issue as soon as possible."
def send_email(subject):
    message=generate_error_report(sender, recipient, subject, body)
    send(message)
# Function to check system statistics
def check_system_statistics():
    # Check CPU usage
    cpu_percent = psutil.cpu_percent()
    if cpu_percent > 80:
        subject = "Error - CPU usage is over 80%"
        send_email(subject)
    # Check available disk space
    disk_usage = psutil.disk_usage("/")
    disk_percent = disk_usage.percent
    if disk_percent > 80:
        subject = "Error - Available disk space is less than 20%"
        send_email(subject)

    # Check available memory
    memory = psutil.virtual_memory()
    available_memory = memory.available / (1024 * 1024)  # Convert to MB
    if available_memory < 500:
        subject = "Error - Available memory is less than 500MB"
        send_email(subject, body)

    # Check hostname resolution
    try:
        hostname = socket.gethostbyname("localhost")
        if hostname != "127.0.0.1":
            subject = "Error - localhost cannot be resolved to 127.0.0.1"
            send_email(subject)
    except socket.gaierror:
        subject = "Error - Failed to resolve hostname localhost"
        send_email(subject)

if __name__ == "__main__":
    check_system_statistics()
