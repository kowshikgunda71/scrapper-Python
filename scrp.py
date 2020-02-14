import os


# seperate folder
def prj_dir(directory):
    if not os.path.exists(directory):
        print('creating a dir' + directory)
        os.makedirs(directory)

