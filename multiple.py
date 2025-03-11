import cv2
import os
import functions_default_image
import analysis_functions
import matplotlib.pyplot as plt
import numpy as np

cropping = False
x_start, y_start = 0, 0
point = 0


def read_mul(path, name):
    """this function reads the file that contains the coordinates of the mucosa , black and white areas"""
    txt_files = []
    x_all = []

    for root, dirs, files in os.walk(path + "areas"):
        for file_i in files:
            if name == "mucosa":
                if "mucosa" in file_i:
                    # append the file name to the list
                    txt_files.append(os.path.join(root, file_i))
                    file = open(path + "areas//" + file_i, "r")
                    x = file.readlines()
                    for i in range(len(x)):
                        try:
                            x[i] = int(x[i].split("\n")[0])
                        except ValueError as error:
                            print(error)
                    x_all.append(x)
                    file.close()
            else:
                if "white" in file_i:
                    # append the file name to the list
                    txt_files.append(os.path.join(root, file_i))
                    file = open(path + "areas//" + file_i, "r")
                    x = file.readlines()
                    for i in range(len(x)):
                        try:
                            x[i] = int(x[i].split("\n")[0])
                        except ValueError as error:
                            print(error)
                    x_all.append(x)
                    file.close()
    #print("number of files:")
    #print(len(x_all))
    return x_all


def save(path, name, ref_point, point):
    """
        this function will save the coordinates in a txt file
        :param path: the path that will save the coordinates
        :param name: name of the file that the coordinates will be saved
        :param ref_point: the list that contains the coordinates
        :param point: num of point
    """
    if not os.path.exists(path + "areas"):
        os.makedirs(path + "areas")
    file = open(path + "areas//" + name + "_" + str(point) + ".txt", "w")
    file.write(str(ref_point[0][1]) + "\n")
    file.write(str(ref_point[1][1]) + "\n")
    file.write(str(ref_point[0][0]) + "\n")
    file.write(str(ref_point[1][0]) + "\n")
    file.close()


def area(name, path):
    """ the player will double click in order to select the requested area on the image that will pop after clicking
        inferior turbinate area button and then save the coordinates. if the user presses "q" the area
        selection will stop.
    """
    image = functions_default_image.default_areas(path)[0]
    size = 2

    def mouse_crop(event, x, y, flags, param):
        # grab references to the global variables
        global x_start, y_start, cropping
        global point
        # if the left mouse button was DOWN, start RECORDING
        # (x, y) coordinates and indicate that cropping is being
        if event == cv2.EVENT_LBUTTONDBLCLK:
            point += 1
            x_start, y_start = x, y
            cropping = True
            ref_point = [(x_start - size, y_start - size), (x_start + size, y_start + size)]

            save(path, name, ref_point, point)

    cv2.namedWindow("image")
    cv2.setMouseCallback("image", mouse_crop)

    while True:
        i = image.copy()
        if not cropping:
            cv2.imshow("image", image)
        elif cropping:
            cv2.rectangle(i, (x_start - 2, y_start - 2), (x_start + 2, y_start + 2), (0, 0, 255), 2)
            cv2.imshow("image", i)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # close all open windows
    cv2.destroyAllWindows()


def method_div_mul(path):
    """When the user clicks the "DIVISION" button the calculation of the intensity of hemoglobin absorption per minute
       (time point) will begin.
       We do that by dividing the two distinct spectral bands (in our case 680 and 873).
       The first time point is the reference time point before the application of the pharmaceutical agent.
    """
    sum_of_all_time, sum_of_all_frames = analysis_functions.extract_sums(1, path)
    sum_of_divided_frames = analysis_functions.divided(sum_of_all_frames)
    sum_of_divided_frames_def, def_time = functions_default_image.default_div(path)
    dimensions_mu_array = read_mul(path, "mucosa")
    averaging_mult(sum_of_divided_frames, sum_of_divided_frames_def, def_time, sum_of_all_time,
                   dimensions_mu_array)


def averaging_mult(sum_of_divided_frames, sum_of_divided_frames_def, def_time, sum_of_time, dimensions_mu_array):
    """Since we want to have 1 point on our graph in the case of more than one image with the same higher P.S.N.R. score
       at the same minute we average the intensities that we found for each frame.
       After the processing a 2d diagram will appear in the screen that will visualize the
       intensity of hemoglobin absorption per minute (time point).
    """
    # declarations start
    average_all_div = []
    average_def_div = []
    time_point = []
    initial = sum_of_time[0].split("-")
    def_per_file_mu = []
    # declarations end
    # for dataset start
    for i in range(len(sum_of_time)):
        per_file_mu = []
        spliced = sum_of_time[i].split("-")
        for num in range(4):
            if len(spliced[num]) == 1:
                spliced[num] = "0" + spliced[num]
        image = sum_of_divided_frames[i]
        time_point.append(analysis_functions.transition(spliced, initial))
        for dimensions_mu in dimensions_mu_array:
            def_img_mu = np.average(sum_of_divided_frames_def[dimensions_mu[0]:dimensions_mu[1],
                                            dimensions_mu[2]:dimensions_mu[3]])
            img_mu = np.average(image[dimensions_mu[0]:dimensions_mu[1], dimensions_mu[2]:dimensions_mu[3]])
            per_file_mu.append(img_mu)
            def_per_file_mu.append(def_img_mu)
            average_all_div.append(np.average(per_file_mu))
    # for dataset end

    # for default image start
    for dimensions_mu in dimensions_mu_array:
        def_img_mu = np.average(sum_of_divided_frames_def[dimensions_mu[0]:dimensions_mu[1],
                                dimensions_mu[2]:dimensions_mu[3]])
        def_per_file_mu.append(def_img_mu)
    average_def_div.append(np.average(def_per_file_mu))

    avg_def = average_def_div  # np.array([average_def_div], dtype=np.float32)
    # for default image end

    avg_intensity, avg_time = analysis_functions.between(time_point, average_all_div, avg_def, def_time)
    # plot start
    plt.plot(avg_time, avg_intensity, "ro-")
    plt.title("Mucosa/white")
    plt.xlabel("Time (min)")
    plt.ylabel("Haemoglobin Oxygenation (a.u.)")
    plt.title("Hemoglobin Oxygenation Dynamic Graph ")
    print(avg_time)
    a = []
    for i in range(len(avg_intensity)):
        a.append(float("{:.2f}".format(avg_intensity[i][0])))
    print(a)
    plt.xlim(-1, 40)
    plt.show()
    # plot end
