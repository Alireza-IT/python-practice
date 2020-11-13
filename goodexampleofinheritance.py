from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    """
    docstring
    """

    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if self.opened:
            raise InvalidOperationError("Stream is already close")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):

    def read(self):
        print("reading from a file")


class NetworkStream(Stream):
    def read(self):
        print("reading from a network")


class MemoryStream(Stream):
    """
    docstring
    """

    def read(self):
        print("reading data from a memory stream.")


stream = Stream()  # becuase of abstract method
memory = MemoryStream()  # it has to implemet the read method otherwiase it dows not work
stream.open()
