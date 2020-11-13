# list or dict or array are container
# build the custom container

class TagCloud:
    def __init__(self):
        self.__tags = {}  # for making the private we use __ in front of the tags

    def add(self, tag):
        # check if there is any tags if no tags plus one
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):  # iterated obj and iter is buitin fun
        # want to you eant to iterate over == self tags and its return one object
        return iter(self.__tags)


cloud = TagCloud()
cloud["python"]  # for this we need getitem magic method
cloud["python"] = 10
len(cloud)
cloud.add("Python")
cloud.add("python")
cloud.add("python")
cloud.add("python")

print(cloud.__tags)  # not accessable
print(cloud.__dict__)  # holds all attribute in this class
