from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry

from pathlib import Path
ENDPOINT = "https://aibenchtest.cognitiveservices.azure.com/"
training_key = "4e5de237206c4d33b1ec8bb93a199f17"
trainer = CustomVisionTrainingClient(training_key, endpoint=ENDPOINT)
projectid="6ea65006-0a20-4518-b916-7eca7f1f197e"

base_image_url = "images/"
image_list = []
pathlist = Path(base_image_url).glob('*.jpg')
x = 0
    
for path in pathlist:
    x= x+ 1
    file_name=str(path)
    print(file_name)
    if x < 59:
        with open(str(path),"rb") as image_contents:
            image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read()))
    else:
        x = 0
        

        upload_result = trainer.create_images_from_files(projectid, images=image_list)
        image_list = []
        if not upload_result.is_batch_successful:
            print("Image batch upload failed.")
            exit(-1)

        for image in upload_result.images:
            print("Image status: ", image.status)
    
        print ("starting upload")

    
print("uploaded images")