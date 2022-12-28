class test:
    def __iter__(self):
        self.a=2
        return self

    def __next__(self):
        x=self.a
        self.a+=2
        return x

a=test()
my_it=iter(a)
next(my_it)
next(my_it)
next(my_it)
print(next(my_it))