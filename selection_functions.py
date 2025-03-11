<<<<<<< HEAD
import os
from skimage import metrics
import numpy as np
import cv2
import functions_crop
import general_functions


def metrics_func(sorted_table, type_cr, f, selected, filter_wave, path):
    """ metric calculation and saving the results """
    metric = []
    if not os.path.exists(path + "metrics"):
        os.makedirs(path + "metrics")
    for i in range(len(sorted_table)):
        metric.append(int(metrics.peak_signal_noise_ratio(selected, sorted_table[i][filter_wave],
                                                          data_range=None)))
    metric = np.array(metric)

    file = open(path + "metrics//" + str(f) + type_cr, "w")
    file.write(str(metric))
    file.close()

    return metric


def metrics_func_quick(sorted_table, selected, filter_wave):
    """ metric calculation and saving the results """
    metric = np.zeros(len(sorted_table), dtype=int)
    small_sum = 0
    for i in range(len(sorted_table)):

        metric[i] = int(metrics.peak_signal_noise_ratio(selected, sorted_table[i][filter_wave],
                        data_range=None))
        small_sum = small_sum + metric[i]
    return metric, small_sum


def save_all(sum_of_all_frames, sum_of_all_time, path):
    """ save the selected frames """
    sum_of_all_frames = np.array(sum_of_all_frames)
    sum_of_all_time = np.array(sum_of_all_time)
    new_path = path + 'selected'
    sorted_table, table1d = functions_crop.table()
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    else:
        general_functions.remove_files(path + "selected//")
    for i in range(len(sum_of_all_frames)):
        for j in range(len(sum_of_all_frames[0])):
            cv2.imwrite(path + "selected//" + sum_of_all_time[i] + "_" +
                        str(sorted_table[j]) + '.png', sum_of_all_frames[i][j])


def pre_process(filename):
    """ the  pre-process of the frames and time so that we can process them and analyze them later on the program """
    sum_of_frames, sum_of_time = general_functions.single_video_opening(filename)
    frames = np.array(sum_of_frames)
    cropped_frames = np.array(functions_crop.initial_crop(frames))
    square_cropped_frames = np.array(functions_crop.square_crop(cropped_frames))
    final_cropped_frames = np.array(functions_crop.final_crop(square_cropped_frames))
    cube = functions_crop.pattern(final_cropped_frames)
    sorted_table = functions_crop.sorted_cube(cube)

    return sorted_table, sum_of_time


def pre_process_select_image(filename):
    """ the  pre-process of the saved_image so that we can process it and analyze its later on the program """
    video = general_functions.file_opening_selection(filename)
    frames = np.array(video)
    cropped_frames = np.array(functions_crop.initial_crop(frames))
    square_cropped_frames = np.array(functions_crop.square_crop(cropped_frames))
    final_cropped_frames = np.array(functions_crop.final_crop(square_cropped_frames))

    return final_cropped_frames
=======
import os
from skimage import metrics
import numpy as np
import cv2
import functions_crop
import general_functions


def metrics_func(sorted_table, type_cr, f, selected, filter_wave, path):
    """ metric calculation and saving the results """
    metric = []
    if not os.path.exists(path + "metrics"):
        os.makedirs(path + "metrics")
    for i in range(len(sorted_table)):
        metric.append(int(metrics.peak_signal_noise_ratio(selected, sorted_table[i][filter_wave],
                                                          data_range=None)))
    metric = np.array(metric)

    file = open(path + "metrics//" + str(f) + type_cr, "w")
    file.write(str(metric))
    file.close()

    return metric


def metrics_func_quick(sorted_table, selected, filter_wave):
    """ metric calculation and saving the results """
    metric = np.zeros(len(sorted_table), dtype=int)
    small_sum = 0
    for i in range(len(sorted_table)):

        metric[i] = int(metrics.peak_signal_noise_ratio(selected, sorted_table[i][filter_wave],
                        data_range=None))
        small_sum = small_sum + metric[i]
    return metric, small_sum


def save_all(sum_of_all_frames, sum_of_all_time, path):
    """ save the selected frames """
    sum_of_all_frames = np.array(sum_of_all_frames)
    sum_of_all_time = np.array(sum_of_all_time)
    new_path = path + 'selected'
    sorted_table, table1d = functions_crop.table()
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    else:
        general_functions.remove_files(path + "selected//")
    for i in range(len(sum_of_all_frames)):
        for j in range(len(sum_of_all_frames[0])):
            cv2.imwrite(path + "selected//" + sum_of_all_time[i] + "_" +
                        str(sorted_table[j]) + '.png', sum_of_all_frames[i][j])


def pre_process(filename):
    """ the  pre-process of the frames and time so that we can process them and analyze them later on the program """
    sum_of_frames, sum_of_time = general_functions.single_video_opening(filename)
    frames = np.array(sum_of_frames)
    cropped_frames = np.array(functions_crop.initial_crop(frames))
    square_cropped_frames = np.array(functions_crop.square_crop(cropped_frames))
    final_cropped_frames = np.array(functions_crop.final_crop(square_cropped_frames))
    cube = functions_crop.pattern(final_cropped_frames)
    sorted_table = functions_crop.sorted_cube(cube)

    return sorted_table, sum_of_time


def pre_process_select_image(filename):
    """ the  pre-process of the saved_image so that we can process it and analyze its later on the program """
    video = general_functions.file_opening_selection(filename)
    frames = np.array(video)
    cropped_frames = np.array(functions_crop.initial_crop(frames))
    square_cropped_frames = np.array(functions_crop.square_crop(cropped_frames))
    final_cropped_frames = np.array(functions_crop.final_crop(square_cropped_frames))

    return final_cropped_frames
>>>>>>> 5f76680e (Initial commit)
