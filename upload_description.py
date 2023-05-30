import os
import requests

url="http://34.135.34.76/fruits/"
def process_text_file(file_path,filename):
    with open(file_path, 'r') as file:
        lines = file.readlines()
      
    fruit = lines[0].strip()
    weight = int(lines[1].strip().strip("lbs"))
    decription =lines[2].strip()
    
    return {
        'name': fruit,
        'weight': weight,
        'description':decription ,
       'image_name':filename.replace(".txt",".jpeg") }
      

def process_directory(directory_path):
    all_data=[]
    home_dir=os.path.expanduser("~")
    directory_path=home_dir+directory_path
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory_path, filename)
            fruit_decription = process_text_file(file_path,filename)
            all_data.append(fruit_decription)
    
    return all_data

def upload_decription(decription, url):
    for data in decription:
        response = requests.post(url, json=data)
        if response.status_code == 201:
            print(f" uploaded successfully")
        else:
            print(f"Failed to upload feedback: {data}")


# Set the directory path and URL
home_dir=os.path.expanduser("~")
directory_path ='/supplier-data/descriptions'

# Process text files in the directory
decriptions = process_directory(directory_path)

# Upload the decription data to the website
upload_decription(decriptions, url)
