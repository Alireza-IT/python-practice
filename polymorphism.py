from abc import ABC, abstractmethod


class UIControl(ABC):
    """
    docstring
    """
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    pass


class DropDownList(UIControl):
    pass


def draw(controls):
    for control in controls:
        control.draw()
