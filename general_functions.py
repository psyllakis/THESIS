<<<<<<< HEAD
import cv2
import numpy as np
import os
from tkinter import filedialog


def get_path():
    """ finding the path """
    path_ori = str(os.path.dirname(__file__))
    path_ori = path_ori.replace("/", "//")
    path_ori += "//"
    return path_ori


def file_opening_selection(filename):
    """
        this function opens the video with the name filename and saves all the frames in a list called sum_of_frame
        :param filename: the name of the video
        :return: sum_of_frames which is a list that contains all the frames of the video
    """
    # definition start
    video = cv2.VideoCapture(filename[0])
    sum_of_frames = []
    num_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    i = 0
    # definition end

    while i < num_frames:
        ret, frame = video.read()
        frame = frame[:, :, 0]
        sum_of_frames.append(frame)
        i = i + 1
    video.release()
    sum_of_frames = np.array(sum_of_frames)

    return sum_of_frames


def import_file(title):
    filename = np.asarray(filedialog.askopenfilenames(title=title))
    print('Selected:', filename)

    return filename


def time_calculation(file):
    split = file.split(" ")
    times = split[1]
    hour = int(times.split("-")[0])
    minutes = int(times.split("-")[1])
    sec = int(times.split("-")[2])

    return sec, hour, minutes


def single_video_opening(file):
    """ opens a video and returns the frames and the time of each frame """
    # definition start
    sum_of_frames = []
    sum_of_time = []
    i = 0
    video = cv2.VideoCapture(file)
    rate = video.get(cv2.CAP_PROP_FPS)
    num_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    # definition end
    sum_s, sum_h, sum_m = time_calculation(file)
    while i < num_frames:
        ret, frame = video.read()
        frame = frame[:, :, 0]
        sum_of_frames.append(frame)
        sum_s = sum_s + 1 / rate
        if sum_s >= 60:
            sum_m = sum_m + 1
            sum_s = sum_s - 60
        if sum_m >= 60:
            sum_h = sum_h + 1
            sum_m = 0
        sec_all = str(round(sum_s, 4)).split(".")
        sec = sec_all[0]
        sec_mi = sec_all[1]
        if sec_mi == "0":
            sec_mi = "0000"
        sum_of_time.append(str(sum_h) + "-" + str(sum_m) + "-" + sec + "-" + sec_mi)
        i = i + 1

    return sum_of_frames, sum_of_time


def remove_files(my_dir):
    """ removes files from a directory """
    if not os.path.exists(my_dir):
        os.makedirs(my_dir)
    file_list = [f for f in os.listdir(my_dir) if f.endswith(".png")]
    for f in file_list:
        os.remove(os.path.join(my_dir, f))


def load_images_from_folder(folder):
    """ this function loads all the images stored in any folder. however we know that with this case we are going
        to use it to load the images of the project we work that are on the sub_folder selected_images and return the
        images and their names which are distinct.
    """
    images = []
    files = []

    for filename in os.listdir(folder):
        files.append(filename)
        img = cv2.imread(os.path.join(folder, filename))
        img = img[:, :, 0]  # gray images
        if img is not None:
            images.append(img)

    return images, files
=======
import cv2
import numpy as np
import os
from tkinter import filedialog


def get_path():
    """ finding the path """
    path_ori = str(os.path.dirname(__file__))
    path_ori = path_ori.replace("/", "//")
    path_ori += "//"
    return path_ori


def file_opening_selection(filename):
    """
        this function opens the video with the name filename and saves all the frames in a list called sum_of_frame
        :param filename: the name of the video
        :return: sum_of_frames which is a list that contains all the frames of the video
    """
    # definition start
    video = cv2.VideoCapture(filename[0])
    sum_of_frames = []
    num_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    i = 0
    # definition end

    while i < num_frames:
        ret, frame = video.read()
        frame = frame[:, :, 0]
        sum_of_frames.append(frame)
        i = i + 1
    video.release()
    sum_of_frames = np.array(sum_of_frames)

    return sum_of_frames


def import_file(title):
    filename = np.asarray(filedialog.askopenfilenames(title=title))
    print('Selected:', filename)

    return filename


def time_calculation(file):
    split = file.split(" ")
    times = split[1]
    hour = int(times.split("-")[0])
    minutes = int(times.split("-")[1])
    sec = int(times.split("-")[2])

    return sec, hour, minutes


def single_video_opening(file):
    """ opens a video and returns the frames and the time of each frame """
    # definition start
    sum_of_frames = []
    sum_of_time = []
    i = 0
    video = cv2.VideoCapture(file)
    rate = video.get(cv2.CAP_PROP_FPS)
    num_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    # definition end
    sum_s, sum_h, sum_m = time_calculation(file)
    while i < num_frames:
        ret, frame = video.read()
        frame = frame[:, :, 0]
        sum_of_frames.append(frame)
        sum_s = sum_s + 1 / rate
        if sum_s >= 60:
            sum_m = sum_m + 1
            sum_s = sum_s - 60
        if sum_m >= 60:
            sum_h = sum_h + 1
            sum_m = 0
        sec_all = str(round(sum_s, 4)).split(".")
        sec = sec_all[0]
        sec_mi = sec_all[1]
        if sec_mi == "0":
            sec_mi = "0000"
        sum_of_time.append(str(sum_h) + "-" + str(sum_m) + "-" + sec + "-" + sec_mi)
        i = i + 1

    return sum_of_frames, sum_of_time


def remove_files(my_dir):
    """ removes files from a directory """
    if not os.path.exists(my_dir):
        os.makedirs(my_dir)
    file_list = [f for f in os.listdir(my_dir) if f.endswith(".png")]
    for f in file_list:
        os.remove(os.path.join(my_dir, f))


def load_images_from_folder(folder):
    """ this function loads all the images stored in any folder. however we know that with this case we are going
        to use it to load the images of the project we work that are on the sub_folder selected_images and return the
        images and their names which are distinct.
    """
    images = []
    files = []

    for filename in os.listdir(folder):
        files.append(filename)
        img = cv2.imread(os.path.join(folder, filename))
        img = img[:, :, 0]  # gray images
        if img is not None:
            images.append(img)

    return images, files
>>>>>>> 5f76680e (Initial commit)
