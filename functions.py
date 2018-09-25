import os
from speech_recognizer import output


pwd = os.system('pwd')
# The following will show all the commands you can do in the current directory
def show_list(output):
    simple_list1 = "long"
    simple_list2 = "my location"
    if "list" in output:
        pwd
        os.system('ls')
    elif simple_list1 and "list" in output:
        pwd
        os.system('ls -l')
    elif simple_list2 in output:
        pwd
        os.system('pwd')
    else:
        return output

"""This is going to be a strange objective.  Not sure how I will go about doing this one but if I want to go
to a specific folder in a directory I just want to say the name of it and it will take me there at that moment."""
def folder_locator(output):
    documents = "documents"
    root_directory = "root"
    if documents in output:
        os.chdir("/home/notorious/Documents")
        pwd
        os.system('ls')
    elif root_directory in output:
        os.chdir("/")
        pwd
    else:
        return output

def file_locator(output):
    file_finder1 = "find"
    file_finder2 = "file"
    if file_finder1 and file_finder2 in output:
        def find(name, path):
            for root, dirs, files in os.walk(path):
                if name in files:
                    print(os.path.join(root, name))
                    return os.path.join(root, name)

        path = '/'
        file = input('What is the file called?')
        find(file, path)
    else:
        return output


def product(output):
    if show_list(output):
        show_list(output)
    elif folder_locator(output):
        folder_locator(output)
    elif file_locator(output):
        file_locator(output)
    else:
        return output