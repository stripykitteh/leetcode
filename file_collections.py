'''
Imagine we have a system that stores files, and these files can be grouped into collections. We are interested in knowing where our resources are being taken up.

For this system we would like to generate a report that lists:

The total size of all files stored; and

The top N collections (by file size) where N can be a user-defined value

An example input into your report generator might look like:



file1.txt (size: 100)
file2.txt (size: 200) in collection "collection1"
file3.txt (size: 200) in collection "collection1"
file4.txt (size: 300) in collection "collection2"
file5.txt (size: 10)
'''

class FileCollections:

    def __init__(self, top_coll: int):
        self.top_coll = top_coll

        self.collection = {
            '': {'file1.txt': 100, 'file5.txt': 10},
            'collection1': {'file2.txt': 200, 'file3.txt': 200},
            'collection2': {'file4.txt': 300}
        }

#    def processFile(self, file_str: str) -> None:

        

    def generateReport(self) -> None:

        # total size
        total_size = 0
        # collection_size
        collection_size = {}
        for top_key in self.collection:
            print("key=>", top_key, "value=>", self.collection[top_key])
            if top_key != '':
                collection_size[top_key] = 0
                for key, value in self.collection[top_key]:
                    print("*** key=>", key , "value=>", value)
                    total_size += self.collection[top_key][key]
                    if key != '':
                        collection_size[key] += self.collection[top_key][key]

        # total_size
        print('total_size=>', total_size)

        # top N collections
        sorted_collections = sorted(collection_size.items(), key=lambda x:x[1])        


if __name__ == '__main__':

    obj = FileCollections(2)
    obj.generateReport()                           

