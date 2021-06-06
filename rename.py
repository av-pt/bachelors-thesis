from os import walk
from os.path import join, isdir, abspath
from shutil import move

base_directory = "./corpus/gutenberg_test" # Directory in which we need to modify the dir names
base_directory = abspath(base_directory) # To make the base_directory an absolute path
# Above is needed for shutil.move to work

all_child_directories = next(walk(base_directory))[1]
for child_dir in all_child_directories:
    new_name = child_dir[:-1] + "b"
    if not isdir(join(base_directory, new_name)): 
    # shutil.move cannot move if the existing directory already exists
        move(join(base_directory, child_dir), join(base_directory, new_name))

# Steps:
# Appended 'a' to training samples and 'b' to test samples to make them distinct. Manually (search & replace) changed filenames in truth and meta files