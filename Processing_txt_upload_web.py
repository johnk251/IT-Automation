import os
import requests

def process_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    title = lines[0].strip()
    name = lines[1].strip()
    date = lines[2].strip()
    feedback = lines[3].strip()
    
    return {
        'title': title,
        'name': name,
        'date': date,
        'feedback': feedback
    }

def process_directory(directory_path):
    feedback_data = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory_path, filename)
            feedback = process_text_file(file_path)
            feedback_data.append(feedback)
    
    return feedback_data

def upload_feedback(feedback_data, url):
    for feedback in feedback_data:
        response = requests.post(url + '/feedback', json=feedback)
        if response.status_code == 201:
            print(f"Feedback uploaded successfully: {feedback}")
        else:
            print(f"Failed to upload feedback: {feedback}")

# Set the directory path and URL
corpweb_external_ip=" "
directory_path ='/data/feedback'
url = f"http://{corpweb_external_ip}/feedback"
# Process text files in the directory
feedback_data = process_directory(directory_path)

# Upload the feedback data to the website
upload_feedback(feedback_data, url)
