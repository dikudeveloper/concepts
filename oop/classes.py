class B(object):

  def first(self):
    print("First method called")

  def second():
    print("Second method called")

# Is the following piece of code valid (Below)? Choose a), or b) or c)
# a)	It isn’t as the object declaration isn’t right
# b)	It isn’t as there isn’t any __init__ method for initializing class members
# c)	Yes


if __name__ == '__main__':
    ob = B()
    B.first(ob)
    ob.first()

