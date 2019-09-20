from TIGr import AbstractSourceReader


class MySourceReader(AbstractSourceReader):
    def __init__(self, parser, file=None):
        super().__init__(parser)
        if file is None:
            file = []
        self.file = file

    def go(self):
        if len(self.file) != 0:  # check if there is a file loaded
            self.read_file(self.file)
        else:  # run demo if there is no file
            self.source.append('D')
            self.source.append('P 3')
            self.source.append('E 50')
            self.source.append('S 50')
            self.source.append('W 50')
            self.source.append('N 50')
            self.source.append('X 250')
            self.source.append('Y 250')
            self.source.append('C 100')
            self.source.append('T 100')
            self.source.append('R 100')
        self.parser.parse(self.source)

    def read_file(self, new_file):  # parsing the instructions from a file string to append the source
        if not isinstance(new_file, list):
            print("Error: Calling read_file without an array")
            pass

        for name in map(str.rstrip, self.file):
            self.source.append(name)
            # print(name)
