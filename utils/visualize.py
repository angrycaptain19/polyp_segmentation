import os
import skimage
import cv2


def save_img(path, img, lib="cv2", overwrite=True):
    if overwrite or not os.path.exists(path):
        print(path)
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        if (lib == "skimage"):
            skimage.io.imsave(path, img)
        elif (lib == "cv2"):
            cv2.imwrite(path, img)
