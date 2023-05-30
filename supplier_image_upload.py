import requests
import os

url = "http://localhost/upload/"
def upload_image(image, url):
        with open(image,"rb") as image:
            response = requests.post(url , files={"file":image})
            if response.status_code == 201:
                print("image uploaded successfully")
            else:
                print("Failed to upload")


def image_directory(directory_path):
    images=[]
    home_dir=os.path.expanduser("~")
    directory_path=home_dir+directory_path
    for filename in os.listdir(directory_path):
        if filename.endswith('.jpeg'):
            file_path = os.path.join(directory_path, filename)
            images.append(file_path)
    
    return images

images=image_directory("/supplier_data/images")
for image in images:
     upload_image(image,url)