#Import the required libraries
import pycocotools.coco as coco
import cv2
import matplotlib.pyplot as plt

'''These libraries are imported to use the COCO dataset API, read and process images using OpenCV,
and display images using Matplotlib.
'''
#Specify the path to the annotations file and create a COCO object:
annotations_file = "C:\\Users\\mohit\\OneDrive\\Desktop\\ObjectDetection\\annotations\\stuff_train2017.json"
coco_data = coco.COCO(annotations_file)

'''The annotations_file variable holds the path to the JSON file containing the COCO dataset annotations. 
The COCO object is created by passing the annotations file path to it.
This object allows us to access various methods and data related to the dataset.
'''

#Get the image IDs and select the second image:
image_ids = coco_data.getImgIds()
#print("HEREE",image_ids)
image_id = image_ids[1] #To change image replace 1 with any other index in image_ids list.

'''The getImgIds() method returns a list of all image IDs in the dataset.
Here, we assign the the desired image ID to the image_id variable for demonstration purposes.
'''

#Image information
image_info = coco_data.loadImgs(image_id)[0]
print(image_info)

'''The loadImgs() method takes an image ID and returns a list of image information dictionaries.
'''

#Define the path to the image file:
image_path = "C:\\Users\\mohit\\OneDrive\\Desktop\\ObjectDetection\\bus\\" + image_info["file_name"]

'''The image_path variable holds the complete path to the image file based on the directory structure and the file name from the image information dictionary.
'''

#Read the image using OpenCV:
image = cv2.imread(image_path)

'''The cv2.imread() function reads the image from the specified file path using OpenCV and assigns it to the image variable. 
OpenCV represents images as NumPy arrays.'''


# Get annotations for the chosen image
annotations_ids = coco_data.getAnnIds(imgIds=image_id)
annotations = coco_data.loadAnns(annotations_ids)

'''The getAnnIds() method takes an image ID and returns a list of annotation IDs associated with that image. 
The loadAnns() method loads the annotations corresponding to the given annotation IDs and returns a list of annotation dictionaries.
Here, we retrieve and store the annotations for the selected image.'''

# Display the image
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

'''The plt.imshow() function is used to display the image using Matplotlib. Since OpenCV reads the image in the BGR color space,
we convert it to the RGB color space using cv2.cvtColor() before passing it to plt.imshow().
'''

# Show the annotations
for annotation in annotations:
    bbox = annotation['bbox']
    category_id = annotation['category_id']
    category_info = coco_data.loadCats(category_id)[0]
    category_name = category_info['name']

    # Draw a blue bounding box around the object
    cv2.rectangle(image, (int(bbox[0]), int(bbox[1])), (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3])), (0, 0, 255), 2)

    # Add a label with the category name
    cv2.putText(image, category_name, (int(bbox[0]), int(bbox[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

'''This loop iterates over each annotation in the annotations list. For each annotation, it retrieves the bounding box coordinates (bbox) and the category ID (category_id).
The loadCats() method is used to load the category information for the given category ID. 
Then, a blue bounding box is drawn around the object using cv2.rectangle(), and a label with the category name is added using cv2.putText().
'''

# Show the modified image with annotated objects
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

'''After drawing the bounding boxes and labels on the image, we display the modified image using plt.imshow().
'''

# Turn off axis labels
plt.axis('off')

'''This removes the x and y axis labels.
'''

# Show the image with annotations
plt.show()
