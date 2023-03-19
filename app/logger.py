import os


class AppLogger:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(file_name, "w")
        self.file_chunck = "_log"
        self.default_dir = 'SpyderHound/DUMP/'


    def __create_log_file(self):
        if not os.path.exists(self.default_dir):
            os.makedirs(self.default_dir)
        self.file = open(self.default_dir + self.file_name + self.file_chunck, "w")

    def __close_log_file(self):
        self.file.close()

    def write(self, message):
        self.__create_log_file()
        self.file.write(message)
        self.__close_log_file()

    def read(self):
        self.__create_log_file()
        return self.file.read()

    def clear(self):
        self.__create_log_file()
        self.file.truncate(0)
        self.__close_log_file()

    def __del__(self):
        self.__close_log_file()

    def __str__(self):
        return self.read()
