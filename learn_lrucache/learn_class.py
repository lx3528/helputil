class test:
    def __init__(self):
        self.d=[1,2,3]
        self.c=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.c <len(self.d):
            self.c+=1
            return self.d[self.c]
        else:
            raise StopIteration

a = test()

for i in a:
    print(i)
