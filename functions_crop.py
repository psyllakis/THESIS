import numpy as np


# CROPPING START
def initial_crop(sum_of_frames):
    sum_cropped = []
    for num in range(len(sum_of_frames)):
        temp = sum_of_frames[num]
        temp2 = np.delete(temp, [0, 1, 2], 0)  # rows
        temp = np.delete(temp2, [-3, -2, -1], 1)  # cols
        sum_cropped.append(temp)

    return sum_cropped


def square_crop(sum_of_frames):
    """ make the image dimensions square nxn """
    # definition start
    sum_of_frames = np.array(sum_of_frames)
    y = len(sum_of_frames[0])
    z = len(sum_of_frames[0][0])
    sum_cropped = []
    sum_cropped2 = []
    # definition end

    if z > y:
        times = int((z-y)/10)
        for num in range(len(sum_of_frames)):
            temp = sum_of_frames[num]

            for i in range(times):
                temp2 = np.delete(temp, [0, 1, 2, 3, 4, -5, -4, -3, -2, -1], 1)
                temp = temp2
            sum_cropped.append(temp)
        return sum_cropped

    elif z < y:
        times = int((y-z)/10)
        for num in range(len(sum_of_frames)):
            temp = sum_cropped[num]
            for i in range(times):
                temp2 = np.delete(temp, [0, 1, 2, 3, 4, -5, -4, -3, -2, -1], 0)
                temp = temp2
            sum_cropped2.append(temp)

        return sum_cropped2
    else:
        return sum_of_frames


def final_crop(sum_of_frames):
    sum_of_frames = np.array(sum_of_frames)
    z = len(sum_of_frames[0][0])
    sum_cropped = []
    times = int(z/50)
    for num in range(len(sum_of_frames)):
        temp = np.array(sum_of_frames[num])
        for i in range(times):
            temp2 = np.delete(temp, [0, 1, 2, 3, 4, -5, -4, -3, -2, -1], 1)
            temp = np.delete(temp2, [0, 1, 2, 3, 4, -5, -4, -3, -2, -1], 0)
        sum_cropped.append(temp)

    return sum_cropped
# CROPPING END


# PATTERN START
def pattern(sum_of_frames):
    """ this function creates the cube """
    cube = []
    for num in range(len(sum_of_frames)):
        frame = np.array(sum_of_frames[num])
        cube_of_frame = []
        for i in range(5):
            for j in range(5):
                cube_of_frame.append(frame[i::5, j::5])
        cube.append(cube_of_frame)
    big_cube_of_frames = np.array(cube)

    return big_cube_of_frames


def table():
    table_wave = np.array([[900, 909, 892, 882, 683],
                           [809, 821, 797, 784, 693],
                           [759, 772, 746, 732, 708],
                           [943, 949, 935, 927, 975],
                           [861, 873, 852, 840, 955]])
    table1d = table_wave.flatten()
    table_sort = np.sort(table1d)
    return table_sort, table1d


def sorted_cube(cube):
    """ this function sorts the cube in ascending order """

    table_sort, table1d = table()
    posit = []
    for i in range(25):
        result = np.where(table1d == table_sort[i])
        for j in range(len(result)):
            posit.append(result[0][j])
    sorted_array = []

    for i in range(len(cube)):
        z = []
        for j in range(len(cube[0])):
            z.append(cube[i][posit[j]])
        sorted_array.append(z)
    sorted_array = np.array(sorted_array)

    return sorted_array
# PATTERN END
