class Demo:
    def __init__(self):
        self.a = 1
        self.__b = 1

    def display(self):
        return self.__b


if __name__ == '__main__':
    obj = Demo()
    # print(obj.__b)
    print(obj.display())


# What's the output of the following Code? Choose between a,b,c,d
# a)	The program has an error because there isn’t any function to return self.b
# b)	The program has an error because b is private and display(self) is returning a private member
# c)	The program has an error because b is private and hence can’t be printed
# d)	The program runs fine and 1 is printed
