def file():
    with open("file.txt", 'r') as localfile:
        todos=localfile.readlines()
        return todos
def write(todos):
    with open("file.txt", 'w') as localwrite:
        localwrite.writelines(todos)