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

def load_input_paragraphs(path):
    with open(path) as file:
        lines = file.read()
        paragraphs = [paragraph.split(' ') for paragraph in lines.split("\n\n")]

        return paragraphs


def open_nggyu(url ='https://www.youtube.com/watch?v=oHg5SJYRHA0'):
    import webbrowser
    return webbrowser.open(url)
