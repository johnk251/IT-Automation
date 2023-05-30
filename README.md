###Google IT Automation with python
Each file represent various projects within Google IT Automation with python, ranging from working with CSV files to Regex

##Batch Image Processing with PIL
>The purpose of the batch_image_pil.py script is to perform a series of image operations using the Python Imaging Library (PIL). The script is designed to iterate through each file in a specified folder and apply the following operations to each image:
-Rotate the image 90° clockwise.
-Resize the image from 192x192 to 128x128 pixels.
-Save the modified image to a new folder in JPEG format.


##Process Text Files with Python Dictionaries and Upload to Running Web Service
>The processing_txt_upload_web.py uses the Python OS module to process a directory of text files , Manage information stored in Python dictionaries and uses the Python requests module to upload content to a running Web service.


##Processes Sales data

>The Generating_pdf_from_car_data.py summarizes and processes sales data into different categories imported in JSON format, generatea PDF  and automaticaly sends the PDF by email 


##Capstone Project Problem Statement
>Given a bunch of images and descriptions of each of the new products, Upload the new products to your online store. Images and descriptions should be uploaded separately, using two different web endpoints. Send a report back to the supplier, letting them know what you imported. Since this process is key to your business's success, you need to make sure that it keeps running! So, you’ll also: Run a script on your web server to monitor system health and  Send an email with an alert if the server is ever unhealthy.

In the final project ,
 
 **run.py** :Process the text files from the supplier-data/descriptions directory by  turn the data into a JSON dictionary

 **changeImage.py**:Process the supplier images by  updating  all images from  3000x2000 to 600x400 pixel resolution and  from .TIFF to .JPEG format.

 **supplier_image_upload.py**: Takes the jpeg images from the supplier-data/images directory processed by **changeImage.py**  and uploads them to the web server fruit catalog

 **reports.py**: Contain methods to generate PDF report

 **emails.py**:Contain methods to send emails

 **health_check.py**: Run in the background monitoring some system statistics: CPU usage, disk space, available memory and name resolution.The Python script send an email if there are problems

 **test.py**: used to test different functions

 **report_email.py**: Process supplier fruit description data