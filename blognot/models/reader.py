"""
"""


class FileReader:

    def __init__(self, filename):
        self.filename = filename
    
    def read_content(self):
        f = open('files/{}'.format(self.filename))
        return f.read()