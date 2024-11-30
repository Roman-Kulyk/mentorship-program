import os


# print(os.name)  # Print OS name

# uname = os.uname()  # Get the username data
# print(uname)

# terminal = os.ctermid()  # Get the terminal details
# print(terminal)

# print(os.environ)  # Print the environment variable

# shell = os.getenv('SHELL', '/bin/fish')  # Get the environment variable
# print(shell)  

# cwd = os.getcwd()  # Get the current working directory
# print(f"Current working directory: {cwd}")

# # Create file paths correctly with os.path.join()
# cwd = os.getcwd()  # Get the current working directory
# new_folder = 'new_folder'  # Child folder in current working directory
# path = os.path.join(cwd, new_folder)
# print("Directory '%s'created" % path)

# # Split the pathname path into a pair(head, tail) where tail is that last
# # pathname component and head is everything leading up to that.
# cwd = os.getcwd()
# path = os.path.split(cwd)
# print(path)

# # Create a new directory with os.mkdir()
# cwd = os.getcwd()
# new_folder_name = 'new_folder'  # New folder name
# path = os.path.join(cwd, new_folder_name)
# os.mkdir(path)  # Create the directory
# print("Directory '%s' created" % path)

# # List directories and files with os.listdir()
# path = "/home/roman/mentorship-program"  
# # Get a list of files and folders in the root directory
# dir_list = os.listdir(path)
# print(dir_list)

# # Remove a file with os.remove()
# file_name = 'my_file.txt'
# directory = '/home/roman/mentorship-program/modules/new_folder'
# path = os.path.join(directory, file_name)
# os.remove(path)

# # Remove a directory with os.rmdir()
# Set the directory to delete
file_name = 'my_directory'
# Set the parent directory path
directory = "/home/roman/mentorship-program/modules/new_folder"
path = os.path.join(directory, file_name)  # Create the full path
os.rmdir(path)  # Delete the directory

# # Return a normalized absolutized version of the pathname path.
cwd = os.getcwd()
absolute_path = os.path.abspath(cwd)
print(f"Absolute path is: {absolute_path}")
print(f"Current working directory is: {cwd}")
print(f"Normalized path is: {os.path.normpath(cwd)}")

# Return True if path is an existing regular file.
cwd = os.getcwd()
print(os.path.isfile(cwd))
print(os.path.isdir(cwd))
print(os.path.islink(cwd))
print(cwd)
