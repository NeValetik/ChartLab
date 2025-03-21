from reader.reader import *

class Interpretor:
    @classmethod
    def interpret(tree):
        Reader.read(tree)
        # Somewhere here we'll call Reader.read(filename),
        # which automatically we'll read the type file

        # This method should return img_path (as a temporar (?) solution),
        # if you have troubles with saving it somewhere and loose,
        # add a static attribute and save there
        pass
