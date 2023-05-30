#!/usr/bin/env python3
import os
import reports
from run import process_directory
import datetime
import emails

attachment= "/tmp/processed.pdf"
directory_path ='/supplier-data/descriptions'
dict_data =process_directory(directory_path)
table_data=reports.fruit_dict_to_table(dict_data)


title=f"Processed Update on {datetime.date.today()}"





if __name__ == "__main__":
    reports.generate_report(attachment,title, table_data)
    sender="automation@example.com"
    recipient="{}@example.com".format(os.environ.get('USER'))
    subject="Upload Completed - Online Fruit Store"
    body="All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message=emails.generate(sender, recipient, subject, body, attachment)
    emails.send(message)