import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from scipy.ndimage import shift
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.neighbors import KNeighborsClassifier
import pickle
import sys
import csv
import cv2

from PIL import Image
#import tikinter as tk
import csv
from io import BytesIO

def predict(blob):
    loaded_model = pickle.load(open('C:\\Users\\kenny\\Downloads\\models\\classification1_model.sav', 'rb'))

    bytes_obj = bytes(blob)
    # Create a BytesIO object using the bytes object
    bytes_io = BytesIO(bytes_obj)

    # Use PIL to open the image from the BytesIO object
    img_file = Image.open(bytes_io)
    original_image = np.array(img_file)

    # Extract the alpha channel as a NumPy array
    image = img_file
    alpha = np.array(image.split()[-1])

    # Create a binary mask of the non-white pixels
    mask = alpha != 255

    # Create a new alpha channel with transparency for the non-white pixels
    new_alpha = np.zeros_like(alpha)
    new_alpha[mask] = 255

    # Replace the old alpha channel with the new one
    image.putalpha(Image.fromarray(new_alpha))

    # Save the resulting image
    image.save("output_image.png")
    # get original image parameters...
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode

    img_file = image.resize([28,28])

    # Make image Greyscale
    img_file = img_file.convert('L')
    #img_grey.save('result.png')
    img_file.show()

    # Save Greyscale values
    value = np.asarray(img_file.getdata(), dtype=int).reshape(1, -1)
    #value = pd.DataFrame(value)
    #value = value.values.reshape(28, 28, 1)

    '''img_array = np.zeros((value.shape[1], 4), dtype=np.uint8)
    img_array[:, :3] = value.T[:, :3]
    img_array[:, 3] = 255

    # Create mask of non-white pixels
    non_white_mask = np.any(img_array[:, :3] != [255, 255, 255], axis=-1)

    mask = img_array != 255
    # Create an RGBA image with alpha channel set to 0 for the background and 255 for the foreground
   
    # Set alpha channel to one for non-white pixels
    img_array[non_white_mask, 3] = 0'''

    y_predict = loaded_model.predict(value)

    clothing_dict = {0:"t-shirt", 1:"trouser", 2:"pullover", 3:"dress", 4:"coat", 5:"sandal", 6:"shirt", 7:"sneaker", 8:"bag", 9:"ankle boot"}

    prediction = clothing_dict[y_predict[0]]
    print(prediction)
    
    results_dir = './classification1_results/'
    prediction_dir = prediction

    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    if not os.path.exists(results_dir + prediction_dir):
        os.makedirs(results_dir + prediction_dir)

    cv2.imwrite(results_dir + prediction_dir + '/' + prediction + '.jpg', original_image)

    return prediction
def get_img():
    folder_path = 'C:/Users/kenny/OneDrive/Desktop/fasion-segmentation-repo/venv/templates/images' # replace with the path to your folder
    file_paths = [os.path.relpath(os.path.join(folder_path, f)) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    print(file_paths)
    return file_paths