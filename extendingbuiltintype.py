class Text(str):
    def duplicate(self):
        return self + self


class Trackable(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list = Trackable()
list.append("1")
