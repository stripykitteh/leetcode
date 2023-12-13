from typing import List

class FileSystem:

    def __init__(self):
        self.paths = {}
        self.paths[""] = 1

    def createPath(self, path: str, value: int) -> bool:

        # check if the path exists
        if path in self.paths:
            return False
        
        # check the path syntax is legal
        dirs_list = path.split("/")
        if dirs_list[0]:
            return False # top level is not empty
        for subdir in range(1,len(dirs_list)):
            if not dirs_list[subdir].islower():
                return False # sub directory contains non-lower case

        # check if the parent path exists
        if not path.rpartition("/")[0] in self.paths:
            return False

        # all tests passed
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        
        if path in self.paths:
            return self.paths[path]
        else:
            return -1

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

if __name__ == '__main__':

    obj = FileSystem()
    print(obj.createPath("/a",1))
    print(obj.get("/a"))
