

class Plant():
    def __init__(self,name):
        self.type = name
    def __eq__(self, other):
        print("Plant ==")
        print(self)
        if type(self) is not type(other):
            return False
        return self.type is other.type
    def __ne__(self, other):
        print("Plant !=")
        print(self)
        if type(self) is not type(other):
            return False
        return self.type is not other.type


class Fruit(Plant):
    def __init__(self, name, taste):
        Plant.__init__(self,name)
        self.taste = taste

    def __eq__(self, other):
        print("Fruit ==")
        print(self)
        if type(self) is not type(other):
            return False
        return (self.type is other.type and self.taste is other.taste)
    def __ne__(self, other):
        print("Fruit !=")
        print(self)
        '''if not hasattr(self, 'taste'):
            return True
        if not hasattr(other, 'taste'):
            return True'''
        if type(self) is not type(other):
            return False
        return (self.type is not other.type and self.taste is not other.taste)


# your code goes here
# end class Plant


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
<__main__.Plant object at 0x7fadd81fefd0>
Plant==
<__main__.Plant object at 0x7fadd81fefd0>
a and b are equal
Plant!=
<__main__.Plant object at 0x7fadd81fefd0>
a and b are equal
<__main__.Fruit object at 0x7fadd81fed00>
Fruit==
<__main__.Fruit object at 0x7fadd81fed00>
c and d are equal
Fruit!=
<__main__.Fruit object at 0x7fadd81fed00>
c and d are equal
Fruit==
<__main__.Fruit object at 0x7fadd81fed00>
a and c are not equal
Fruit!=
<__main__.Fruit object at 0x7fadd81fed00>
a and c are equal
Fruit==
<__main__.Fruit object at 0x7fadd81fed00>
c and a are not equal
Fruit!=
<__main__.Fruit object at 0x7fadd81fed00>
c and a are equal

This means that:
In case (a) the operator of the first instance is invoked. For example, when comparing a == b (Plant vs Plant), a's __eq__ is invoked.
In case (b) the operator of the instance of the subclass is invoked. For exmaple, when comparing c == a (Fruit vs Plant) c's __eq__ is invoked.
In case (c) the operator of the instance of the subclass is invoked. For exmaple, when comparing a == c (Fruit vs Plant) c's __eq__ is invoked.



"""
