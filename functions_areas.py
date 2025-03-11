import cv2
import os
import functions_default_image

cropping = False
x_start, y_start = 0, 0


def read(name, path):
    """this function reads the file that contains the coordinates of the mucosa , black and white areas"""
    file = open(path + "areas//"+name+".txt", "r")
    x = file.readlines()
    for i in range(len(x)):
        try:
            x[i] = int(x[i].split("\n")[0])
        except ValueError as error:
            print(error)
    file.close()

    return x


def save(path, name, ref_point):
    """
        this function will save the coordinates in a txt file
        :param path: the path that will save the coordinates
        :param name: name of the file that the coordinates will be saved
        :param ref_point: the list that contains the coordinates
    """
    if not os.path.exists(path + "areas"):
        os.makedirs(path + "areas")
    file = open(path + "areas//" + name + ".txt", "w")
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

    def mouse_crop(event, x, y, flags, param):
        """ """
        # grab references to the global variables
        global x_start, y_start, cropping

        # if the left mouse button was DOWN, start RECORDING
        # (x, y) coordinates and indicate that cropping is being
        if event == cv2.EVENT_LBUTTONDBLCLK:
            x_start, y_start = x, y
            cropping = True
            ref_point = [(x_start - 2, y_start - 2), (x_start + 2, y_start + 2)]

            save(path, name, ref_point)

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
