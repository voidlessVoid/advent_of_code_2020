def path_to_dir(filename):
    import os
    return os.path.relpath(filename)

def load_input_to_list(path):
    with open(path) as file:
        content = file.readlines()
        try:
            content = [int(x.strip()) for x in content]
        except:
            content = [str(x.strip()) for x in content]

    return content
