import numpy as np
from PIL import Image, ImageDraw
import cv2
import os
# Open the input image as numpy array, convert to RGB


def load_filenames_from_folder(folder):
    images = []
    files = []
    for filename in os.listdir(folder):
        files.append(filename)
        img = cv2.imread(os.path.join(folder, filename))
        img = img[:, :, 0]
        if img is not None:
            images.append(img)
    return  files


for filename in os.listdir("images"):
    img = Image.open("images//"+filename).convert("RGB")
    npImage = np.array(img)
    h, w = img.size
    # print(h)
    # print(w)
    # Create same size alpha layer with circle
    alpha = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([25, 25, h-25, w-25], 0, 360, fill=255)

    # Convert alpha Image to numpy array
    npAlpha = np.array(alpha)

    # Add alpha layer to RGB
    # grayimg = cv2.cvtColor(npImage, cv2.COLOR_BGR2GRAY)
    # npImage = cv2.equalizeHist(grayimg)

    npImage = np.dstack((npImage, npAlpha))
    # Save with alpha
    Image.fromarray(npImage).save(filename)
