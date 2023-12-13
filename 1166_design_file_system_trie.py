from typing import List
from collections import defaultdict

class Tree:
    def __init__(self, val=None, children = defaultdict()):
        
        self.children = {}
        self.val = val

class FileSystem:

    def __init__(self):
        self.root = Tree()
        
    def createPath(self, path: str, value: int) -> bool:
        node = self.root
        if path == "" or path == "/":
            return False 
        paths = path.split('/')
        paths = paths[1:]
        i = 0
        while i < len(paths)-1:
            if paths[i] not in node.children:
                return False
            node = node.children[paths[i]]
            i+=1
        if paths[i] in node.children: 
            return False
        else:
            node.children[paths[i]] = Tree(value)
            
        return True

    def get(self, path: str) -> int:
        node = self.root
        paths = path.split('/')
        paths = paths[1:]
        for path in paths:
            if path not in node.children:
                return -1
            node = node.children[path]
        return node.val
            
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

if __name__ == '__main__':

    obj = FileSystem()
    print(obj.createPath("/a",1))
    print(obj.get("/a"))
