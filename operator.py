class Plant():
    def __init__(self,name):
        self.type = name
    def __eq__(self, other):
        print("==")
        return self.type is other.type
    def __ne__(self, other):
        print("!=")
        return self.type is not other.type



# your code goes here
# end class Plant

class Fruit(Plant):
    def __init__(self, name, taste):
        self.type = name
        self.taste = taste

    def __eq__(self, other):
        print("==")
        if not hasattr(self, 'taste'):
            return False
        if not hasattr(other, 'taste'):
            return False
        return (self.type is other.type and self.taste is other.taste)
    def __ne__(self, other):
        print("!=")
        if not hasattr(self, 'taste'):
            return True
        if not hasattr(other, 'taste'):
            return True
        return (self.type is not other.type and self.taste is not other.taste)


# your code goes here
# end class Fruit

def main():
    a = Plant("Maple");
    print(a)
    b = Plant("Maple");

    if a == b:
        print("a and b are equal")
    else:
        print("a and b are not equal");
    if a != b:
        print("a and b are not equal")
    else:
        print("a and b are equal")

    c = Fruit("Apple", "sweet")
    print(c)
    d = Fruit("Apple", "sweet")

    if c == d:
        print("c and d are equal")
    else:
        print("c and d are not equal")
    if c != d:
        print("c and d are not equal")
    else:
        print("c and d are equal")

    if a == c:
        print("a and c are equal")
    else:
        print("a and c are not equal")
    if a != c:
        print("a and c are not equal")
    else:
        print("a and c are equal")
    if c == a:
        print("c and a are equal")
    else:
        print("c and a are not equal")
    if c != a:
        print("c and a are not equal")
    else:
        print("c and a are equal")

# end function main

main()

"""
When the the code runs, a result is given like this:
<__main__.Plant object at 0x7fcc6015ddf0>
==
a and b are equal
!=
a and b are equal
<__main__.Fruit object at 0x7fcc6015db80>
==
c and d are equal
!=
c and d are equal
==
a and c are not equal
!=
a and c are not equal
==
c and a are not equal
!=
c and a are not equal
This means that for all cases in (a) (b) (c), the operator of testing equality is ==, inequality is !=
"""
