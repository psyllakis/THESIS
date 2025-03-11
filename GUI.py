<<<<<<< HEAD
from tkinter import *
import numpy as np
from PIL import ImageTk, Image
import cv2
import os
from tkinter import ttk
import project_functions
import functions_time
import functions_default_image
import functions_crop
import analysis_functions
import functions_areas
import general_functions
import selection_functions
import time

global project
global projects_dropdown
global path      # original path
global path_def  # specific path for each project
import multiple #


def frame_selection():
    """ this function is used as its name suggests to select the frames that are the closest to the saved image
        it is used an image metric P.S.N.R.
         to compare the images.The comparison is going to be between the wavelength 746  of every cropped image.
        we are going to select the images that have the best P.S.N.R. score in every time point (every minute).
        the score of every image is going to be stored in a text file and the selected images in a sub_folder of the
        initial (project) folder with the name "selected".
    """
    t0 = time.time()
    filter_wave = 4
    general_functions.remove_files(path + "selected//")
    # saved image
    sorted_table_selection = functions_default_image.default_get(path)
    selected = sorted_table_selection[0][filter_wave]
    # rest of the dataset
    filename = general_functions.import_file("select the dataset")
    sum_of_all_time = []
    sum_of_all_frames = []

    if filename[0]:
        for f in range(len(filename)):
            if filename[f].split(".")[-1] == "avi":
                sorted_table, sum_of_time = selection_functions.pre_process(filename[f])
                time_point = functions_time.time_points(sum_of_time)
                # metrics
                metric = selection_functions.metrics_func(sorted_table, ".txt", f, selected, filter_wave, path)
                metric_time, metric_frames = functions_time.per_minute(time_point, metric, sorted_table, sum_of_time)
                for i in range(len(metric_frames)):
                    sum_of_all_time.append(metric_time[i])
                    sum_of_all_frames.append(metric_frames[i])
        # save all
        selection_functions.save_all(sum_of_all_frames, sum_of_all_time, path)
    t1 = time.time()
    t = t1 - t0
    print("time of processing is:  " + str(int(t/60)) + " ΜΙΝ")
    print("frame selection ended")


def auto():
    t0 = time.time()
    filter_wave = 4

    general_functions.remove_files(path + "selected//")
    # rest of the dataset
    sum_of_all_time = []
    sum_of_all_frames = []
    filename_initial = general_functions.import_file("select the default")
    filename_rest = general_functions.import_file("select the dataset")
    list_of_sums = []
    final_cropped_frames = []
    if filename_initial[0]:
        if filename_initial[0].split(".")[-1] == "avi":
            final_cropped_frames = np.array(functions_crop.final_crop(functions_crop.square_crop(
                functions_crop.initial_crop(general_functions.file_opening_selection(filename_initial)))))
            list_of_sums = np.zeros(len(final_cropped_frames), dtype=int)
            for i in range(len(final_cropped_frames)):
                cube_selection = functions_crop.pattern([final_cropped_frames[i]])
                sorted_table_selection = functions_crop.sorted_cube(cube_selection)
                selected = sorted_table_selection[0][filter_wave]
                small_sum = 0
                if filename_rest[0]:
                    for f in range(len(filename_rest)):
                        if filename_rest[f].split(".")[-1] == "avi":
                            sorted_table, sum_of_time = selection_functions.pre_process(filename_rest[f])
                            # metrics
                            metric, small = selection_functions.metrics_func_quick(sorted_table, selected, filter_wave)
                            small_sum = small_sum + small
                list_of_sums[i] = small_sum
    # saved image
    result = np.where(list_of_sums == np.amax(list_of_sums))
    thesis = result[0][0]
    selected_img = final_cropped_frames[thesis]
    if not os.path.exists(path + "saved"):
        os.makedirs(path + "saved")
    general_functions.remove_files(path + "saved")
    cv2.imwrite(path + "saved//" + str(thesis) + "_selected.png", selected_img)

    sorted_table_selection = functions_crop.sorted_cube(functions_crop.pattern([selected_img]))
    selected = sorted_table_selection[0][filter_wave]

    if filename_rest[0]:
        for f in range(len(filename_rest)):
            if filename_rest[f].split(".")[-1] == "avi":
                sorted_table, sum_of_time = selection_functions.pre_process(filename_rest[f])
                time_point = functions_time.time_points(sum_of_time)
                # metrics
                metric = selection_functions.metrics_func(sorted_table, ".txt", f, selected, filter_wave, path)

                metric_time, metric_frames = functions_time.per_minute(time_point, metric, sorted_table, sum_of_time)
                for i in range(len(metric_frames)):
                    sum_of_all_time.append(metric_time[i])
                    sum_of_all_frames.append(metric_frames[i])

        selection_functions.save_all(sum_of_all_frames, sum_of_all_time, path)
    t1 = time.time()
    t = t1 - t0
    print("time of processing is:  " + str(int(t/60)) + " ΜΙΝ")
    print("frame selection ended")


def enable():
    """this function enables all the buttons for the visualisation! """
    Button(root,
           text='HOD Graph',
           compound=LEFT,
           command=lambda: analysis_functions.method_div(path),
           bg="black",
           fg="white",
           ).grid(row=12, column=3, columnspan=3)

    Button(root,
           text='SRD Graph',
           compound=LEFT,
           bg="black",
           fg="white",
           command=lambda: analysis_functions.method_wave(path)
           ).grid(row=14, column=3, columnspan=3)


def multiple_en():  #
    Label(root, text="Multiple selection:").grid(row=18, column=3, columnspan=3)
    Button(root,
           text='inferior turbinate area',
           compound=LEFT,
           bg="black",
           fg="white",
           command=lambda: multiple.area("mucosa", path)
           ).grid(row=19, column=3, columnspan=3)
    Button(root,
           text='HOD Graph',
           compound=LEFT,
           command=lambda: multiple.method_div_mul(path),
           bg="black",
           fg="white",
           ).grid(row=20, column=3, columnspan=3)


def multiple_dis():  #
    Label(root, text="Multiple selection:").grid(row=18, column=3, columnspan=3)
    Button(root,
           text='inferior turbinate area',
           compound=LEFT,
           bg="black",
           fg="white",
           state=DISABLED
           ).grid(row=19, column=3, columnspan=3)
    Button(root,
           text='HOD Graph',
           compound=LEFT,
           bg="black",
           fg="white",
           state=DISABLED
           ).grid(row=20, column=3, columnspan=3)


def enable_areas():
    """it enables the buttons that are used for selecting the area of  mucosa"""
    Button(root,
           text='inferior turbinate area',
           compound=LEFT,
           bg="black",
           fg="white",
           command=lambda: functions_areas.area("mucosa", path)
           ).grid(row=9, column=3, columnspan=3)


def areas_dis():
    """this function disables the buttons that are used for the selection of the areas on the image"""
    Button(root,
           text='inferior turbinate area',
           compound=LEFT,
           bg="black",
           fg="white",
           state=DISABLED
           ).grid(row=9, column=3, columnspan=3)


def disable_vis():
    """this function disables all the buttons that are used for visualisation"""
    Button(root,
           text='HOD Graph',
           compound=LEFT,
           bg="black",
           fg="white",
           state=DISABLED
           ).grid(row=12, column=3, columnspan=3)
    Button(root,
           text='SRD Graph',
           compound=LEFT,
           bg="black",
           fg="white",
           state=DISABLED
           ).grid(row=14, column=3, columnspan=3)


def select_image():
    """ this code runs after the user has selected the first video ,which is also the default video(without the
        pharmaceutical agent). it enables the user to press the buttons on the top right side of the GUI(3 buttons and
        a bar) and it loads all the frames of that video and shows it to the user so that he or she can select the image
        that he or she thinks is an image that can be the representative in order to be compared with the rest of the
        dataset.
        with the buttons and bar the user can navigate through the images.
        after the user selects the image with the "select" button the frame that was shown is saved!
    """
    # definitions start
    all_frames = []
    all_frames_np = []
    # definitions end

    def back(image_number):
        """ the function of the << button"""

        if (image_number >= 0) and (image_number <= len(all_frames)):
            Label(image=all_frames[image_number]).grid(row=0, column=0, columnspan=3, rowspan=25)
            horizontal.set(image_number + 1)
        else:
            print("error")
        Label(root, text=("image " + str(image_number + 1) + " of " + str(len(all_frames))), bd=1,
              relief=SUNKEN, anchor=E).grid(row=2, column=3, columnspan=4)
        Button(root, text=">>", command=lambda: forward(image_number + 1)).grid(row=0, column=5)
        if image_number - 1 == 0:
            Button(root, text="<<", state=DISABLED).grid(row=0, column=3, pady=10)
        else:
            Button(root, text="<<", command=lambda: back(image_number - 1)).grid(row=0, column=3, pady=10)

    def select():
        state_of_i = horizontal.get() - 1
        """ the function of the select button"""

        if not os.path.exists(path + "saved"):
            os.makedirs(path + "saved")
        general_functions.remove_files(path + "saved")
        selected = all_frames_np[state_of_i]
        cv2.imwrite(path + "saved//" + str(state_of_i) + "selected.png", selected)
        Button(root,
               text='click after you selected the default image',
               command=frame_selection,
               compound=LEFT,
               bg="black",
               fg="white",
               ).grid(row=6, column=3, columnspan=3)

    def forward(image_number):
        """ the function of the >> button"""
        if (image_number >= 0) and (image_number <= len(all_frames)):
            Label(image=all_frames[image_number]).grid(row=0, column=0, columnspan=3, rowspan=25)
            horizontal.set(image_number + 1)
        else:
            print("error")
        Label(root, text=("image " + str(image_number + 1) + " of " + str(len(all_frames))), bd=1,
              relief=SUNKEN, anchor=E).grid(row=2, column=3, columnspan=4)
        Button(root, text="<<", command=lambda: back(image_number - 1)).grid(row=0, column=3, pady=10)
        if image_number + 1 == len(all_frames):
            Button(root, text=">>", state=DISABLED).grid(row=0, column=5)
        else:
            Button(root, text=">>", command=lambda: forward(image_number + 1)).grid(row=0, column=5)

    def slide(var):
        """ the function of the bar """
        state_of_i = horizontal.get() - 1
        Label(root, text=("image " + str(state_of_i + 1) + " of " + str(len(all_frames))), bd=1,
              relief=SUNKEN, anchor=E).grid(row=2, column=3, columnspan=4)
        Label(image=all_frames[state_of_i]).grid(row=0, column=0, columnspan=3, rowspan=25)

        if state_of_i == 0:
            Button(root, text="<<", state=DISABLED).grid(row=0, column=3, pady=10)
        else:
            Button(root, text="<<", command=lambda: back(state_of_i - 1)).grid(row=0, column=3, pady=10)

        if state_of_i + 1 == len(all_frames):
            Button(root, text=">>", state=DISABLED).grid(row=0, column=5)
        else:
            Button(root, text=">>", command=lambda: forward(state_of_i + 1)).grid(row=0, column=5)

    filename = general_functions.import_file("select the first video")
    if filename[0]:
        if filename[0].split(".")[-1] == "avi":
            video = general_functions.file_opening_selection(filename)
            frames = np.array(video)
            cropped_frames = np.array(functions_crop.initial_crop(frames))
            square_cropped_frames = np.array(functions_crop.square_crop(cropped_frames))
            final_cropped_frames = np.array(functions_crop.final_crop(square_cropped_frames))
            all_frames_np = final_cropped_frames

            # GUI START
            for i in range(len(final_cropped_frames)):
                all_frames.append(ImageTk.PhotoImage(Image.fromarray(final_cropped_frames[i])))
            my_label = Label(image=all_frames[0])
            my_label.grid(row=0, column=0, columnspan=3, rowspan=25)
            status_image = Label(root, text=("image " + str(1) + " of " + str(len(all_frames))), bd=1,
                                 relief=SUNKEN, anchor=E)
            button_forward = Button(root, text=">>", command=lambda: forward(1))
            button_select = Button(root, text="select", command=select)
            button_back = Button(root, text="<<", state=DISABLED)
            horizontal = Scale(root, from_=1, to=len(all_frames), orient=HORIZONTAL, command=slide)

            button_forward.grid(row=0, column=5)
            button_back.grid(row=0, column=3, pady=10)
            horizontal.grid(row=1, column=3, columnspan=4, sticky=W + E)
            status_image.grid(row=2, column=3, columnspan=4)
            my_label.grid(row=0, column=0, columnspan=3, rowspan=25)
            button_select.grid(row=0, column=4)
            # GUI END


def project_selection(event):
    """The user selects what folder or data wants to visualise.
       The user selects between the folders where the saved data are stored(after the analysis).
       it calls some functions in order for the user to select and visualise what he wants.
    """
    global path
    for i in range(len(project)):
        if projects_dropdown.get() == project[i]:
            path = path_def + "projects//"+projects_dropdown.get()+"//"
            enable()
            enable_areas()
            multiple_en()  #


def take_entry():
    """takes a str from the user that is going to be used for the name of the folder that the data are going to
       be saved!
       In other words it changes the path global variable.
    """
    global path
    global project
    global projects_dropdown

    user_input.get()
    project_functions.write(path_def, user_input.get())
    project = project_functions.read(path_def)
    dropdown_list()
    path = path_def + "projects//" + user_input.get()+"//"


def take_entry_to_delete():
    global path
    global project
    global projects_dropdown

    user_input.get()
    project_functions.delete_project(path_def, user_input.get())

    project = project_functions.read(path_def)
    dropdown_list()
    path = path_def + "projects/" + user_input.get()+"/"


def dropdown_list():
    global projects_dropdown

    projects_dropdown = ttk.Combobox(root, values=project)
    projects_dropdown.current(0)
    projects_dropdown.bind("<<ComboboxSelected>>", project_selection)
    projects_dropdown.grid(row=8, column=3, columnspan=3)


def default_gui():
    Label(root, image=my_img1).grid(row=0, column=0, columnspan=3, rowspan=25)
    Button(root, text=">>", state=DISABLED).grid(row=0, column=5)
    Button(root, text="select", state=DISABLED).grid(row=0, column=4)
    Button(root, state=DISABLED, text="<<").grid(row=0, column=3, pady=10)
    Label(root, text="Enter the name of the project:").grid(row=3, column=3, columnspan=3)
    Button(root,
           text='select the first video',
           command=select_image,
           compound=LEFT,
           bg="black",
           fg="white",
           ).grid(row=5, column=3, columnspan=3)
    Button(root,
           text='click after you selected the default image',
           compound=LEFT,
           bg="black",
           fg="white",
           state=DISABLED
           ).grid(row=6, column=3, columnspan=3)
    Button(root,
           text='AUTO',
           command=auto,
           bg="black",
           fg="white",
           compound=LEFT).grid(row=7, column=3, columnspan=3)


if __name__ == "__main__":
    # PATH START
    path = general_functions.get_path()
    path_def = path
    project = project_functions.read(path_def)
    # PATH END

    # default GUI START
    root = Tk()
    root.title("THESIS")
    root.wm_iconbitmap('def_images//image.ico')
    my_img = ImageTk.PhotoImage(Image.open("def_images/image.png"))
    my_img1 = ImageTk.PhotoImage(Image.open("def_images/image_def.png"))
    # default GUI END

    # initial buttons that change once the user interacts with the app START
    dropdown_list()
    user_input = StringVar(root)
    Entry(root, textvariable=user_input).grid(row=4, column=3, columnspan=2)
    Button(root, text='Enter', command=take_entry).grid(row=4, column=5, columnspan=1)
    Button(root, text='Delete', command=take_entry_to_delete).grid(row=4, column=6, columnspan=1)
    default_gui()
    disable_vis()
    areas_dis()
    multiple_dis()
    # initial buttons that change once the user interacts with the app END
    root.mainloop()
=======
from tkinter import *
import numpy as np
from PIL import ImageTk, Image
import cv2
import os
from tkinter import ttk
import project_functions
import functions_time
import functions_default_image
import functions_crop
import analysis_functions
import functions_areas
import general_functions
import selection_functions
import time

global project
global projects_dropdown
global path      # original path
global path_def  # specific path for each project
import multiple #


def frame_selection():
    """ this function is used as its name suggests to select the frames that are the closest to the saved image
        it is used an image metric P.S.N.R.
         to compare the images.The comparison is going to be between the wavelength 746  of every cropped image.
        we are going to select the images that have the best P.S.N.R. score in every time point (every minute).
        the score of every image is going to be stored in a text file and the selected images in a sub_folder of the
        initial (project) folder with the name "selected".
    """
    t0 = time.time()
    filter_wave = 4
    general_functions.remove_files(path + "selected//")
    # saved image
    sorted_table_selection = functions_default_image.default_get(path)
    selected = sorted_table_selection[0][filter_wave]
    # rest of the dataset
    filename = general_functions.import_file("select the dataset")
    sum_of_all_time = []
    sum_of_all_frames = []

    if filename[0]:
        for f in range(len(filename)):
            if filename[f].split(".")[-1] == "avi":
                sorted_table, sum_of_time = selection_functions.pre_process(filename[f])
                time_point = functions_time.time_points(sum_of_time)
                # metrics
                metric = selection_functions.metrics_func(sorted_table, ".txt", f, selected, filter_wave, path)
                metric_time, metric_frames = functions_time.per_minute(time_point, metric, sorted_table, sum_of_time)
                for i in range(len(metric_frames)):
                    sum_of_all_time.append(metric_time[i])
                    sum_of_all_frames.append(metric_frames[i])
        # save all
        selection_functions.save_all(sum_of_all_frames, sum_of_all_time, path)
    t1 = time.time()
    t = t1 - t0
    print("time of processing is:  " + str(int(t/60)) + " ΜΙΝ")
    print("frame selection ended")


def auto():
    t0 = time.time()
    filter_wave = 4

    general_functions.remove_files(path + "selected//")
    # rest of the dataset
    sum_of_all_time = []
    sum_of_all_frames = []
    filename_initial = general_functions.import_file("select the default")
    filename_rest = general_functions.import_file("select the dataset")
    list_of_sums = []
    final_cropped_frames = []
    if filename_initial[0]:
        if filename_initial[0].split(".")[-1] == "avi":
            final_cropped_frames = np.array(functions_crop.final_crop(functions_crop.square_crop(
                functions_crop.initial_crop(general_functions.file_opening_selection(filename_initial)))))
            list_of_sums = np.zeros(len(final_cropped_frames), dtype=int)
            for i in range(len(final_cropped_frames)):
                cube_selection = functions_crop.pattern([final_cropped_frames[i]])
                sorted_table_selection = functions_crop.sorted_cube(cube_selection)
                selected = sorted_table_selection[0][filter_wave]
                small_sum = 0
                if filename_rest[0]:
                    for f in range(len(filename_rest)):
                        if filename_rest[f].split(".")[-1] == "avi":
                            sorted_table, sum_of_time = selection_functions.pre_process(filename_rest[f])
                            # metrics
                            metric, small = selection_functions.metrics_func_quick(sorted_table, selected, filter_wave)
                            small_sum = small_sum + small
                list_of_sums[i] = small_sum
    # saved image
    result = np.where(list_of_sums == np.amax(list_of_sums))
    thesis = result[0][0]
    selected_img = final_cropped_frames[thesis]
    if not os.path.exists(path + "saved"):
        os.makedirs(path + "saved")
    general_functions.remove_files(path + "saved")
    cv2.imwrite(path + "saved//" + str(thesis) + "_selected.png", selected_img)

    sorted_table_selection = functions_crop.sorted_cube(functions_crop.pattern([selected_img]))
    selected = sorted_table_selection[0][filter_wave]

    if filename_rest[0]:
        for f in range(len(filename_rest)):
            if filename_rest[f].split(".")[-1] == "avi":
                sorted_table, sum_of_time = selection_functions.pre_process(filename_rest[f])
                time_point = functions_time.time_points(sum_of_time)
                # metrics
                metric = selection_functions.metrics_func(sorted_table, ".txt", f, selected, filter_wave, path)

                metric_time, metric_frames = functions_time.per_minute(time_point, metric, sorted_table, sum_of_time)
                for i in range(len(metric_frames)):
                    sum_of_all_time.append(metric_time[i])
                    sum_of_all_frames.append(metric_frames[i])

        selection_functions.save_all(sum_of_all_frames, sum_of_all_time, path)
    t1 = time.time()
    t = t1 - t0
    print("time of processing is:  " + str(int(t/60)) + " ΜΙΝ")
    print("frame selection ended")


def enable():
    """this function enables all the buttons for the visualisation! """
    Button(root,
           text='HOD Graph',
           compound=LEFT,
           command=lambda: analysis_functions.method_div(path),
           bg="black",
           fg="white",
           ).grid(row=12, column=3, columnspan=3)

    Button(root,
           text='SRD Graph',
           compound=LEFT,
           bg="black",
           fg="white",
           command=lambda: analysis_functions.method_wave(path)
           ).grid(row=14, column=3, columnspan=3)


def multiple_en():  #
    Label(root, text="Multiple selection:").grid(row=18, column=3, columnspan=3)
    Button(root,
           text='inferior turbinate area',
           compound=LEFT,
           bg="black",
           fg="white",
           command=lambda: multiple.area("mucosa", path)
           ).grid(row=19, column=3, columnspan=3)
    Button(root,
           text='HOD Graph',
           compound=LEFT,
           command=lambda: multiple.method_div_mul(path),
           bg="black",
           fg="white",
           ).grid(row=20, column=3, columnspan=3)


def multiple_dis():  #
    Label(root, text="Multiple selection:").grid(row=18, column=3, columnspan=3)
    Button(root,
           text='inferior turbinate area',
           compound=LEFT,
           bg="black",
           fg="white",
           state=DISABLED
           ).grid(row=19, column=3, columnspan=3)
    Button(root,
           text='HOD Graph',
           compound=LEFT,
           bg="black",
           fg="white",
           state=DISABLED
           ).grid(row=20, column=3, columnspan=3)


def enable_areas():
    """it enables the buttons that are used for selecting the area of  mucosa"""
    Button(root,
           text='inferior turbinate area',
           compound=LEFT,
           bg="black",
           fg="white",
           command=lambda: functions_areas.area("mucosa", path)
           ).grid(row=9, column=3, columnspan=3)


def areas_dis():
    """this function disables the buttons that are used for the selection of the areas on the image"""
    Button(root,
           text='inferior turbinate area',
           compound=LEFT,
           bg="black",
           fg="white",
           state=DISABLED
           ).grid(row=9, column=3, columnspan=3)


def disable_vis():
    """this function disables all the buttons that are used for visualisation"""
    Button(root,
           text='HOD Graph',
           compound=LEFT,
           bg="black",
           fg="white",
           state=DISABLED
           ).grid(row=12, column=3, columnspan=3)
    Button(root,
           text='SRD Graph',
           compound=LEFT,
           bg="black",
           fg="white",
           state=DISABLED
           ).grid(row=14, column=3, columnspan=3)


def select_image():
    """ this code runs after the user has selected the first video ,which is also the default video(without the
        pharmaceutical agent). it enables the user to press the buttons on the top right side of the GUI(3 buttons and
        a bar) and it loads all the frames of that video and shows it to the user so that he or she can select the image
        that he or she thinks is an image that can be the representative in order to be compared with the rest of the
        dataset.
        with the buttons and bar the user can navigate through the images.
        after the user selects the image with the "select" button the frame that was shown is saved!
    """
    # definitions start
    all_frames = []
    all_frames_np = []
    # definitions end

    def back(image_number):
        """ the function of the << button"""

        if (image_number >= 0) and (image_number <= len(all_frames)):
            Label(image=all_frames[image_number]).grid(row=0, column=0, columnspan=3, rowspan=25)
            horizontal.set(image_number + 1)
        else:
            print("error")
        Label(root, text=("image " + str(image_number + 1) + " of " + str(len(all_frames))), bd=1,
              relief=SUNKEN, anchor=E).grid(row=2, column=3, columnspan=4)
        Button(root, text=">>", command=lambda: forward(image_number + 1)).grid(row=0, column=5)
        if image_number - 1 == 0:
            Button(root, text="<<", state=DISABLED).grid(row=0, column=3, pady=10)
        else:
            Button(root, text="<<", command=lambda: back(image_number - 1)).grid(row=0, column=3, pady=10)

    def select():
        state_of_i = horizontal.get() - 1
        """ the function of the select button"""

        if not os.path.exists(path + "saved"):
            os.makedirs(path + "saved")
        general_functions.remove_files(path + "saved")
        selected = all_frames_np[state_of_i]
        cv2.imwrite(path + "saved//" + str(state_of_i) + "selected.png", selected)
        Button(root,
               text='click after you selected the default image',
               command=frame_selection,
               compound=LEFT,
               bg="black",
               fg="white",
               ).grid(row=6, column=3, columnspan=3)

    def forward(image_number):
        """ the function of the >> button"""
        if (image_number >= 0) and (image_number <= len(all_frames)):
            Label(image=all_frames[image_number]).grid(row=0, column=0, columnspan=3, rowspan=25)
            horizontal.set(image_number + 1)
        else:
            print("error")
        Label(root, text=("image " + str(image_number + 1) + " of " + str(len(all_frames))), bd=1,
              relief=SUNKEN, anchor=E).grid(row=2, column=3, columnspan=4)
        Button(root, text="<<", command=lambda: back(image_number - 1)).grid(row=0, column=3, pady=10)
        if image_number + 1 == len(all_frames):
            Button(root, text=">>", state=DISABLED).grid(row=0, column=5)
        else:
            Button(root, text=">>", command=lambda: forward(image_number + 1)).grid(row=0, column=5)

    def slide(var):
        """ the function of the bar """
        state_of_i = horizontal.get() - 1
        Label(root, text=("image " + str(state_of_i + 1) + " of " + str(len(all_frames))), bd=1,
              relief=SUNKEN, anchor=E).grid(row=2, column=3, columnspan=4)
        Label(image=all_frames[state_of_i]).grid(row=0, column=0, columnspan=3, rowspan=25)

        if state_of_i == 0:
            Button(root, text="<<", state=DISABLED).grid(row=0, column=3, pady=10)
        else:
            Button(root, text="<<", command=lambda: back(state_of_i - 1)).grid(row=0, column=3, pady=10)

        if state_of_i + 1 == len(all_frames):
            Button(root, text=">>", state=DISABLED).grid(row=0, column=5)
        else:
            Button(root, text=">>", command=lambda: forward(state_of_i + 1)).grid(row=0, column=5)

    filename = general_functions.import_file("select the first video")
    if filename[0]:
        if filename[0].split(".")[-1] == "avi":
            video = general_functions.file_opening_selection(filename)
            frames = np.array(video)
            cropped_frames = np.array(functions_crop.initial_crop(frames))
            square_cropped_frames = np.array(functions_crop.square_crop(cropped_frames))
            final_cropped_frames = np.array(functions_crop.final_crop(square_cropped_frames))
            all_frames_np = final_cropped_frames

            # GUI START
            for i in range(len(final_cropped_frames)):
                all_frames.append(ImageTk.PhotoImage(Image.fromarray(final_cropped_frames[i])))
            my_label = Label(image=all_frames[0])
            my_label.grid(row=0, column=0, columnspan=3, rowspan=25)
            status_image = Label(root, text=("image " + str(1) + " of " + str(len(all_frames))), bd=1,
                                 relief=SUNKEN, anchor=E)
            button_forward = Button(root, text=">>", command=lambda: forward(1))
            button_select = Button(root, text="select", command=select)
            button_back = Button(root, text="<<", state=DISABLED)
            horizontal = Scale(root, from_=1, to=len(all_frames), orient=HORIZONTAL, command=slide)

            button_forward.grid(row=0, column=5)
            button_back.grid(row=0, column=3, pady=10)
            horizontal.grid(row=1, column=3, columnspan=4, sticky=W + E)
            status_image.grid(row=2, column=3, columnspan=4)
            my_label.grid(row=0, column=0, columnspan=3, rowspan=25)
            button_select.grid(row=0, column=4)
            # GUI END


def project_selection(event):
    """The user selects what folder or data wants to visualise.
       The user selects between the folders where the saved data are stored(after the analysis).
       it calls some functions in order for the user to select and visualise what he wants.
    """
    global path
    for i in range(len(project)):
        if projects_dropdown.get() == project[i]:
            path = path_def + "projects//"+projects_dropdown.get()+"//"
            enable()
            enable_areas()
            multiple_en()  #


def take_entry():
    """takes a str from the user that is going to be used for the name of the folder that the data are going to
       be saved!
       In other words it changes the path global variable.
    """
    global path
    global project
    global projects_dropdown

    user_input.get()
    project_functions.write(path_def, user_input.get())
    project = project_functions.read(path_def)
    dropdown_list()
    path = path_def + "projects//" + user_input.get()+"//"


def take_entry_to_delete():
    global path
    global project
    global projects_dropdown

    user_input.get()
    project_functions.delete_project(path_def, user_input.get())

    project = project_functions.read(path_def)
    dropdown_list()
    path = path_def + "projects/" + user_input.get()+"/"


def dropdown_list():
    global projects_dropdown

    projects_dropdown = ttk.Combobox(root, values=project)
    projects_dropdown.current(0)
    projects_dropdown.bind("<<ComboboxSelected>>", project_selection)
    projects_dropdown.grid(row=8, column=3, columnspan=3)


def default_gui():
    Label(root, image=my_img1).grid(row=0, column=0, columnspan=3, rowspan=25)
    Button(root, text=">>", state=DISABLED).grid(row=0, column=5)
    Button(root, text="select", state=DISABLED).grid(row=0, column=4)
    Button(root, state=DISABLED, text="<<").grid(row=0, column=3, pady=10)
    Label(root, text="Enter the name of the project:").grid(row=3, column=3, columnspan=3)
    Button(root,
           text='select the first video',
           command=select_image,
           compound=LEFT,
           bg="black",
           fg="white",
           ).grid(row=5, column=3, columnspan=3)
    Button(root,
           text='click after you selected the default image',
           compound=LEFT,
           bg="black",
           fg="white",
           state=DISABLED
           ).grid(row=6, column=3, columnspan=3)
    Button(root,
           text='AUTO',
           command=auto,
           bg="black",
           fg="white",
           compound=LEFT).grid(row=7, column=3, columnspan=3)


if __name__ == "__main__":
    # PATH START
    path = general_functions.get_path()
    path_def = path
    project = project_functions.read(path_def)
    # PATH END

    # default GUI START
    root = Tk()
    root.title("THESIS")
    root.wm_iconbitmap('def_images//image.ico')
    my_img = ImageTk.PhotoImage(Image.open("def_images/image.png"))
    my_img1 = ImageTk.PhotoImage(Image.open("def_images/image_def.png"))
    # default GUI END

    # initial buttons that change once the user interacts with the app START
    dropdown_list()
    user_input = StringVar(root)
    Entry(root, textvariable=user_input).grid(row=4, column=3, columnspan=2)
    Button(root, text='Enter', command=take_entry).grid(row=4, column=5, columnspan=1)
    Button(root, text='Delete', command=take_entry_to_delete).grid(row=4, column=6, columnspan=1)
    default_gui()
    disable_vis()
    areas_dis()
    multiple_dis()
    # initial buttons that change once the user interacts with the app END
    root.mainloop()
>>>>>>> 5f76680e (Initial commit)
