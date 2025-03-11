<<<<<<< HEAD
from pathlib import Path
import shutil

""" this .py file is containing functions used to process the projects"""


def write(path, name):
    """ it appends the text file projects.txt which is default and contains all the names of projects that have
        been saved
    """
    file = open(path + "def_images//" + "projects.txt", "a")
    file.write(str(name) + "\n")
    file.close()


def read(path):
    """ it reads the text file and returns in a type of a list all the names of the projects """
    file = open(path + "def_images//" + "projects.txt", "r")
    x = file.readlines()

    for i in range(len(x)):
        x[i] = x[i].split("\n")[0]
    if len(x) == 0:
        x = ["       "]
    else:
        x = x
    file.close()

    return x


def delete_project(path, name):
    """ delete the name of the project from the projects.txt and
        delete the data and the folder of that project
    """
    x = read(path)
    x.remove(str(name))
    file = open(path + "def_images//" + "projects.txt", "w")

    for i in range(len(x)):
        file.write(x[i]+"\n")
    file.close()
    path_ori = (path+"projects//"+name).replace("//", "/")
    dir_path = Path(path_ori+"/")
    try:
        shutil.rmtree(dir_path)
    except OSError as e:
        print("Error: %s : %s" % (dir_path, e.strerror))
        print("if the project folder was not created, there is no error")
=======
from pathlib import Path
import shutil

""" this .py file is containing functions used to process the projects"""


def write(path, name):
    """ it appends the text file projects.txt which is default and contains all the names of projects that have
        been saved
    """
    file = open(path + "def_images//" + "projects.txt", "a")
    file.write(str(name) + "\n")
    file.close()


def read(path):
    """ it reads the text file and returns in a type of a list all the names of the projects """
    file = open(path + "def_images//" + "projects.txt", "r")
    x = file.readlines()

    for i in range(len(x)):
        x[i] = x[i].split("\n")[0]
    if len(x) == 0:
        x = ["       "]
    else:
        x = x
    file.close()

    return x


def delete_project(path, name):
    """ delete the name of the project from the projects.txt and
        delete the data and the folder of that project
    """
    x = read(path)
    x.remove(str(name))
    file = open(path + "def_images//" + "projects.txt", "w")

    for i in range(len(x)):
        file.write(x[i]+"\n")
    file.close()
    path_ori = (path+"projects//"+name).replace("//", "/")
    dir_path = Path(path_ori+"/")
    try:
        shutil.rmtree(dir_path)
    except OSError as e:
        print("Error: %s : %s" % (dir_path, e.strerror))
        print("if the project folder was not created, there is no error")
>>>>>>> 5f76680e (Initial commit)
