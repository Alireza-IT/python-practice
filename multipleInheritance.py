class Flyer:
    """
    docstring
    """

    def fly(self):
        print("fly")


class Swimmer():
    """
    docstring
    """

    def swim(self):
        print("Person greet")


class FlyingFish(Flyer, Swimmer):
    """
    docstring
    """
    pass


manager = Manager()
manager.greet()
