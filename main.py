from interfaceTests.ChildFactory import ChildFactory
from interfaceTests.ChildType import ChildType

if __name__ == '__main__':
    c1 = ChildFactory.getProperChild(ChildType.CHILD_1)
    c2 = ChildFactory.getProperChild(ChildType.CHILD_2)
    c3 = ChildFactory.getProperChild(ChildType.CHILD_3)
    c1.demo()
    c2.demo()
    c3.demo()

