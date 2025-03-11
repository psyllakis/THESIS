<<<<<<< HEAD
import functions_crop
import cv2
import numpy as np
import analysis_functions
import os
import functions_areas


def default_get(path):
    # selected image
    filename = os.listdir(path+"saved//")[0]
    selected_img = np.array([cv2.imread(path + "saved//" + filename, 0)])
    cube_selection = functions_crop.pattern(selected_img)
    sorted_table_selection = functions_crop.sorted_cube(cube_selection)
    return sorted_table_selection


def default_div(path):
    """ in this function we do all the necessary modifications to the default saved image in order to be visualised
        in the 2d diagram at time point 0.
    """
    sorted_table_selection = default_get(path)
    all_div = analysis_functions.divided(sorted_table_selection)[0]
    def_time = 0

    return all_div, def_time


def default_areas(path):
    """ in this function we do all the necessary modifications to the default saved image in order to
    """
    sorted_table_selection = default_get(path)

    return sorted_table_selection[0]


def default_3d(path):
    """ in this function we do all the necessary modifications to the default saved image in order to be visualised
        in the 3d diagram at time point 0.
    """
    # declarations start
    sorted_table_selection = default_get(path)
    def_time = 0.0  # we use 0 so that the separation  is going to be clear to the eye
    average_all = []
    dimensions_mu = functions_areas.read("mucosa", path)
    # declarations end

    for i in range(25):
        cropped_img_mu = sorted_table_selection[0][i][dimensions_mu[0]:dimensions_mu[1],
                                                      dimensions_mu[2]:dimensions_mu[3]]
        average_all.append(np.average(cropped_img_mu))
    return average_all, def_time
=======
import functions_crop
import cv2
import numpy as np
import analysis_functions
import os
import functions_areas


def default_get(path):
    # selected image
    filename = os.listdir(path+"saved//")[0]
    selected_img = np.array([cv2.imread(path + "saved//" + filename, 0)])
    cube_selection = functions_crop.pattern(selected_img)
    sorted_table_selection = functions_crop.sorted_cube(cube_selection)
    return sorted_table_selection


def default_div(path):
    """ in this function we do all the necessary modifications to the default saved image in order to be visualised
        in the 2d diagram at time point 0.
    """
    sorted_table_selection = default_get(path)
    all_div = analysis_functions.divided(sorted_table_selection)[0]
    def_time = 0

    return all_div, def_time


def default_areas(path):
    """ in this function we do all the necessary modifications to the default saved image in order to
    """
    sorted_table_selection = default_get(path)

    return sorted_table_selection[0]


def default_3d(path):
    """ in this function we do all the necessary modifications to the default saved image in order to be visualised
        in the 3d diagram at time point 0.
    """
    # declarations start
    sorted_table_selection = default_get(path)
    def_time = 0.0  # we use 0 so that the separation  is going to be clear to the eye
    average_all = []
    dimensions_mu = functions_areas.read("mucosa", path)
    # declarations end

    for i in range(25):
        cropped_img_mu = sorted_table_selection[0][i][dimensions_mu[0]:dimensions_mu[1],
                                                      dimensions_mu[2]:dimensions_mu[3]]
        average_all.append(np.average(cropped_img_mu))
    return average_all, def_time
>>>>>>> 5f76680e (Initial commit)
