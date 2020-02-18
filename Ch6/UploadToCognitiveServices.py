from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry

from pathlib import Path
ENDPOINT = "https://westus2.api.cognitive.microsoft.com"
training_key = "aa9afbe3879c45d7aa2326c58867187d"
trainer = CustomVisionTrainingClient(training_key, endpoint=ENDPOINT)
projectid="081e259d-c82a-4a49-acc6-27fc1adf8539"

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
        image_list = []

        upload_result = trainer.create_images_from_files(projectid, images=image_list)
        if not upload_result.is_batch_successful:
            print("Image batch upload failed.")
            exit(-1)

        for image in upload_result.images:
            print("Image status: ", image.status)
    
        print ("starting upload")

    
print("uploaded images")