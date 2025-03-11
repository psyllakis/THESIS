<<<<<<< HEAD
import matplotlib.pyplot as plt
import numpy as np
import cv2
import functions_default_image
import general_functions
import functions_crop
import functions_areas


def divided(sum_of_all_frames):
    """ After the frame selection, with each selected frame we are going to divide the wavelength 683 with the
        wavelength 873.
        This division  is going to be the oxygenated hemoglobin distribution map.
    """
    all_div = np.zeros([len(sum_of_all_frames)], dtype=type((cv2.divide(np.float32(sum_of_all_frames[0][0]),
                                                                        np.float32(sum_of_all_frames[0][14]))) * 100))
    for i in range(len(sum_of_all_frames)):
        all_div[i] = (cv2.divide(np.float32(sum_of_all_frames[i][0]), np.float32(sum_of_all_frames[i][14]))) * 100
        # 680 873
        # divided_1 = (cv2.divide(np.float32(sum_of_all_frames[i][4]), np.float32(sum_of_all_frames[i][11]))) * 100
        # 840 and 746

    return all_div


def transition(spliced, initial):
    """ it returns time in a format of real minutes"."seconds microseconds.
        minutes are from 0 to 60, but we now that our measurements lasts 30 to 40 minutes.
    """
    minutes = int(spliced[1])
    minutes_initial = int(initial[1])
    minutes_real = minutes - minutes_initial

    if minutes_real < 0:
        minutes_real = 60 + minutes_real
    elif minutes == minutes_initial:
        minutes_real = 60
    return float(str(minutes_real) + "." + spliced[2] + spliced[3])


def extract_sums(temp, path):
    """ it averages the images and the time so that we have 1 point """
    # declarations start
    sum_of_all_frames = []
    sum_of_time = []
    sorted_table = functions_crop.table()[0]
    # declarations end

    # 1 if we use the default frame selection
    # otherwise if we use the algo that does frame selection based on the cropped images
    if temp == 1:
        images, filename = general_functions.load_images_from_folder(path + "selected//")
    else:
        images, filename = general_functions.load_images_from_folder(path + "selected_cropped//")
    # the method is going to be the same we just change the folder from which the images are going to be loaded
    for i in range(0, len(images), 25):
        sum_of_time.append(filename[i].split("_")[0])
        print(filename)
        sum_of_frames = []
        for j in range(len(sorted_table)):
            sum_of_frames.append(images[j+i])
        sum_of_all_frames.append(sum_of_frames)
    sum_of_all_frames = np.array(sum_of_all_frames)
    sum_of_all_time = np.array(sum_of_time)
    return sum_of_all_time, sum_of_all_frames


def averaging(sum_of_divided_frames, sum_of_divided_frames_def, def_time, sum_of_time, dimensions_mu):
    """Since we want to have 1 point on our graph in the case of more than one image with the same higher P.S.N.R. score
       at the same minute we average the intensities that we found for each frame.
       After the processing a 2d diagram will appear in the screen that will visualize the
       intensity of hemoglobin absorption per minute (time point).
    """
    # declarations start
    average_all_mu = []
    time_point = []
    initial = sum_of_time[0].split("-")
    # declarations end

    for i in range(len(sum_of_time)):
        spliced = sum_of_time[i].split("-")
        for num in range(4):
            if len(spliced[num]) == 1:
                spliced[num] = "0" + spliced[num]
        time_point.append(transition(spliced, initial))
        image = sum_of_divided_frames[i]
        cropped_img_mu = np.average(image[dimensions_mu[0]:dimensions_mu[1], dimensions_mu[2]:dimensions_mu[3]])
        average_all_mu.append(cropped_img_mu)

    def_cropped_img_mu = np.average(sum_of_divided_frames_def[dimensions_mu[0]:dimensions_mu[1],
                                                      dimensions_mu[2]:dimensions_mu[3]])
    def_average_all_muc = def_cropped_img_mu
    avg_def_muc = np.array([def_average_all_muc], dtype=np.float32)
    avg_intensity, avg_time = between(time_point, average_all_mu, avg_def_muc, def_time)
    plt.plot(avg_time, avg_intensity, "ro-")
    print(avg_time)
    a = []
    for i in range(len(avg_intensity)):
        a.append(float("{:.2f}".format(avg_intensity[i][0])))
    print(a)
    plt.xlabel("Time (min)")
    plt.xlim(-1, 40)
    plt.ylabel("Haemoglobin Oxygenation (a.u.)")
    plt.title("Hemoglobin Oxygenation Dynamic Graph ")
    plt.show()


def method_div(path):
    """When the user clicks the "HOD Graph" button the calculation of the intensity of hemoglobin absorption per minute
       (time point) will begin.
       We do that by dividing the two distinct spectral bands (in our case 680 and 873).
       The first time point is the reference time point before the application of the pharmaceutical agent.
    """
    sum_of_all_time, sum_of_all_frames = extract_sums(1, path)
    sum_of_divided_frames = divided(sum_of_all_frames)
    sum_of_divided_frames_def, def_time = functions_default_image.default_div(path)
    dimensions_mu = functions_areas.read("mucosa", path)
    averaging(sum_of_divided_frames, sum_of_divided_frames_def, def_time, sum_of_all_time, dimensions_mu)


def method_wave(path):
    """ 3-dimentional graph
        In each of the three graphs we normalize the intensity by dividing them with the
        same value that we found for the default image.
    """
    sum_of_all_time, sum_of_all_frames = extract_sums(1, path)
    sorted_selection, time_selection = functions_default_image.default_3d(path)
    average1 = []
    average2 = []
    # for int and time start
    intensity = []
    time_point_all = []
    for i in range(25):
        wave = []
        for j in range(len(sum_of_all_frames)):
            wave.append(sum_of_all_frames[j][i])
        int_v, time_point = averaging_wave(wave, sum_of_all_time, path)
        intensity.append(int_v)
        time_point_all.append(time_point)

    intensity = np.array(intensity)
    time_point = np.array(time_point_all)
    sorted_selection = np.array(sorted_selection)

    for i in range(25):
        avg1, avg2 = between(time_point[i], intensity[i], sorted_selection[i], np.float64(time_selection))
        average1.append(avg1)
        average2.append(avg2)
    intensity = np.array(average1, dtype=object)
    time_point = np.array(average2)
    # for int and time end

    # sorted table start
    sorted_table, none = functions_crop.table()
    sort = []
    for i in range(25):
        x = []
        for j in range(len(average1[0])):
            x.append(sorted_table[i])
        sort.append(x)
    sorted_table = np.array(sort)
    # sorted table end

    # plot start
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for j in range(len(sorted_table[0])):
        plt.plot(sorted_table[:, j], time_point[:, j], intensity[:, j]/intensity[:, 0], "g")
    ax.set_xlabel('Wavelength')
    ax.set_ylabel('Time (minutes)')
    ax.set_zlabel('Intensity')
    plt.title('Spectral Reflectivity Dynamics Graph ')
    plt.show()
    # plot end


def between(time_point, average, avg_def, def_time):
    """ averaging of time and intensity per minute in case we have more than one images with the same P.S.N.R. score"""
    # declarations start
    new_time_point = []
    new_average = []
    time_point = np.array(time_point)
    average = np.array(average)
    all_pos = []
    average1 = []
    average2 = []
    # declarations end

    for i in range(34):
        b = time_point[time_point <= i + 1]
        c = time_point[time_point >= i]
        d = np.intersect1d(b, c)
        if len(d) != 0:
            new_time_point.append(d)
            pos = []
            for p in range(len(d)):
                result = list(np.where(time_point == d[p]))

                pos.append(result[0])
            all_pos.append(pos)
    for i in range(len(all_pos)):
        average_small = []
        for j in range(len(all_pos[i])):
            average_small.append(average[all_pos[i][j]])
        new_average.append(average_small)

    # initiate with default image start
    average1.append(avg_def)
    average2.append(def_time)
    # initiate with default image end

    for i in range(len(new_average)):
        avg = sum(new_average[i]) / len(new_average[i])
        avg2 = sum(new_time_point[i]) / len(new_time_point[i])
        average1.append(avg)
        average2.append(avg2)
    return average1, average2


def averaging_wave(sum_of_wave_frames, sum_of_time, path):
    """ algorithm that can produce  3-dimentional graph"""
    # declarations start
    average_all = []
    time_point = []
    initial = sum_of_time[0].split("-")
    dimensions_mu = functions_areas.read("mucosa", path)
    # declarations end

    for i in range(len(sum_of_time)):
        spliced = sum_of_time[i].split("-")
        for num in range(4):
            if len(spliced[num]) == 1:
                spliced[num] = "0" + spliced[num]
        time_point.append(transition(spliced, initial))
        image = sum_of_wave_frames[i]
        cropped_img_mu = image[dimensions_mu[0]:dimensions_mu[1], dimensions_mu[2]:dimensions_mu[3]]
        average_all.append(np.average(cropped_img_mu))
    return average_all, time_point
=======
import matplotlib.pyplot as plt
import numpy as np
import cv2
import functions_default_image
import general_functions
import functions_crop
import functions_areas


def divided(sum_of_all_frames):
    """ After the frame selection, with each selected frame we are going to divide the wavelength 683 with the
        wavelength 873.
        This division  is going to be the oxygenated hemoglobin distribution map.
    """
    all_div = np.zeros([len(sum_of_all_frames)], dtype=type((cv2.divide(np.float32(sum_of_all_frames[0][0]),
                                                                        np.float32(sum_of_all_frames[0][14]))) * 100))
    for i in range(len(sum_of_all_frames)):
        all_div[i] = (cv2.divide(np.float32(sum_of_all_frames[i][0]), np.float32(sum_of_all_frames[i][14]))) * 100
        # 680 873
        # divided_1 = (cv2.divide(np.float32(sum_of_all_frames[i][4]), np.float32(sum_of_all_frames[i][11]))) * 100
        # 840 and 746

    return all_div


def transition(spliced, initial):
    """ it returns time in a format of real minutes"."seconds microseconds.
        minutes are from 0 to 60, but we now that our measurements lasts 30 to 40 minutes.
    """
    minutes = int(spliced[1])
    minutes_initial = int(initial[1])
    minutes_real = minutes - minutes_initial

    if minutes_real < 0:
        minutes_real = 60 + minutes_real
    elif minutes == minutes_initial:
        minutes_real = 60
    return float(str(minutes_real) + "." + spliced[2] + spliced[3])


def extract_sums(temp, path):
    """ it averages the images and the time so that we have 1 point """
    # declarations start
    sum_of_all_frames = []
    sum_of_time = []
    sorted_table = functions_crop.table()[0]
    # declarations end

    # 1 if we use the default frame selection
    # otherwise if we use the algo that does frame selection based on the cropped images
    if temp == 1:
        images, filename = general_functions.load_images_from_folder(path + "selected//")
    else:
        images, filename = general_functions.load_images_from_folder(path + "selected_cropped//")
    # the method is going to be the same we just change the folder from which the images are going to be loaded
    for i in range(0, len(images), 25):
        sum_of_time.append(filename[i].split("_")[0])
        print(filename)
        sum_of_frames = []
        for j in range(len(sorted_table)):
            sum_of_frames.append(images[j+i])
        sum_of_all_frames.append(sum_of_frames)
    sum_of_all_frames = np.array(sum_of_all_frames)
    sum_of_all_time = np.array(sum_of_time)
    return sum_of_all_time, sum_of_all_frames


def averaging(sum_of_divided_frames, sum_of_divided_frames_def, def_time, sum_of_time, dimensions_mu):
    """Since we want to have 1 point on our graph in the case of more than one image with the same higher P.S.N.R. score
       at the same minute we average the intensities that we found for each frame.
       After the processing a 2d diagram will appear in the screen that will visualize the
       intensity of hemoglobin absorption per minute (time point).
    """
    # declarations start
    average_all_mu = []
    time_point = []
    initial = sum_of_time[0].split("-")
    # declarations end

    for i in range(len(sum_of_time)):
        spliced = sum_of_time[i].split("-")
        for num in range(4):
            if len(spliced[num]) == 1:
                spliced[num] = "0" + spliced[num]
        time_point.append(transition(spliced, initial))
        image = sum_of_divided_frames[i]
        cropped_img_mu = np.average(image[dimensions_mu[0]:dimensions_mu[1], dimensions_mu[2]:dimensions_mu[3]])
        average_all_mu.append(cropped_img_mu)

    def_cropped_img_mu = np.average(sum_of_divided_frames_def[dimensions_mu[0]:dimensions_mu[1],
                                                      dimensions_mu[2]:dimensions_mu[3]])
    def_average_all_muc = def_cropped_img_mu
    avg_def_muc = np.array([def_average_all_muc], dtype=np.float32)
    avg_intensity, avg_time = between(time_point, average_all_mu, avg_def_muc, def_time)
    plt.plot(avg_time, avg_intensity, "ro-")
    print(avg_time)
    a = []
    for i in range(len(avg_intensity)):
        a.append(float("{:.2f}".format(avg_intensity[i][0])))
    print(a)
    plt.xlabel("Time (min)")
    plt.xlim(-1, 40)
    plt.ylabel("Haemoglobin Oxygenation (a.u.)")
    plt.title("Hemoglobin Oxygenation Dynamic Graph ")
    plt.show()


def method_div(path):
    """When the user clicks the "HOD Graph" button the calculation of the intensity of hemoglobin absorption per minute
       (time point) will begin.
       We do that by dividing the two distinct spectral bands (in our case 680 and 873).
       The first time point is the reference time point before the application of the pharmaceutical agent.
    """
    sum_of_all_time, sum_of_all_frames = extract_sums(1, path)
    sum_of_divided_frames = divided(sum_of_all_frames)
    sum_of_divided_frames_def, def_time = functions_default_image.default_div(path)
    dimensions_mu = functions_areas.read("mucosa", path)
    averaging(sum_of_divided_frames, sum_of_divided_frames_def, def_time, sum_of_all_time, dimensions_mu)


def method_wave(path):
    """ 3-dimentional graph
        In each of the three graphs we normalize the intensity by dividing them with the
        same value that we found for the default image.
    """
    sum_of_all_time, sum_of_all_frames = extract_sums(1, path)
    sorted_selection, time_selection = functions_default_image.default_3d(path)
    average1 = []
    average2 = []
    # for int and time start
    intensity = []
    time_point_all = []
    for i in range(25):
        wave = []
        for j in range(len(sum_of_all_frames)):
            wave.append(sum_of_all_frames[j][i])
        int_v, time_point = averaging_wave(wave, sum_of_all_time, path)
        intensity.append(int_v)
        time_point_all.append(time_point)

    intensity = np.array(intensity)
    time_point = np.array(time_point_all)
    sorted_selection = np.array(sorted_selection)

    for i in range(25):
        avg1, avg2 = between(time_point[i], intensity[i], sorted_selection[i], np.float64(time_selection))
        average1.append(avg1)
        average2.append(avg2)
    intensity = np.array(average1, dtype=object)
    time_point = np.array(average2)
    # for int and time end

    # sorted table start
    sorted_table, none = functions_crop.table()
    sort = []
    for i in range(25):
        x = []
        for j in range(len(average1[0])):
            x.append(sorted_table[i])
        sort.append(x)
    sorted_table = np.array(sort)
    # sorted table end

    # plot start
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for j in range(len(sorted_table[0])):
        plt.plot(sorted_table[:, j], time_point[:, j], intensity[:, j]/intensity[:, 0], "g")
    ax.set_xlabel('Wavelength')
    ax.set_ylabel('Time (minutes)')
    ax.set_zlabel('Intensity')
    plt.title('Spectral Reflectivity Dynamics Graph ')
    plt.show()
    # plot end


def between(time_point, average, avg_def, def_time):
    """ averaging of time and intensity per minute in case we have more than one images with the same P.S.N.R. score"""
    # declarations start
    new_time_point = []
    new_average = []
    time_point = np.array(time_point)
    average = np.array(average)
    all_pos = []
    average1 = []
    average2 = []
    # declarations end

    for i in range(34):
        b = time_point[time_point <= i + 1]
        c = time_point[time_point >= i]
        d = np.intersect1d(b, c)
        if len(d) != 0:
            new_time_point.append(d)
            pos = []
            for p in range(len(d)):
                result = list(np.where(time_point == d[p]))

                pos.append(result[0])
            all_pos.append(pos)
    for i in range(len(all_pos)):
        average_small = []
        for j in range(len(all_pos[i])):
            average_small.append(average[all_pos[i][j]])
        new_average.append(average_small)

    # initiate with default image start
    average1.append(avg_def)
    average2.append(def_time)
    # initiate with default image end

    for i in range(len(new_average)):
        avg = sum(new_average[i]) / len(new_average[i])
        avg2 = sum(new_time_point[i]) / len(new_time_point[i])
        average1.append(avg)
        average2.append(avg2)
    return average1, average2


def averaging_wave(sum_of_wave_frames, sum_of_time, path):
    """ algorithm that can produce  3-dimentional graph"""
    # declarations start
    average_all = []
    time_point = []
    initial = sum_of_time[0].split("-")
    dimensions_mu = functions_areas.read("mucosa", path)
    # declarations end

    for i in range(len(sum_of_time)):
        spliced = sum_of_time[i].split("-")
        for num in range(4):
            if len(spliced[num]) == 1:
                spliced[num] = "0" + spliced[num]
        time_point.append(transition(spliced, initial))
        image = sum_of_wave_frames[i]
        cropped_img_mu = image[dimensions_mu[0]:dimensions_mu[1], dimensions_mu[2]:dimensions_mu[3]]
        average_all.append(np.average(cropped_img_mu))
    return average_all, time_point
>>>>>>> 5f76680e (Initial commit)
