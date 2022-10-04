from interfaceTests.Child3 import Child3
from interfaceTests.ChildType import ChildType
from interfaceTests.child1 import Child1
from interfaceTests.child2 import Child2


class ChildFactory:

    @staticmethod
    def getProperChild(childType):
        if childType == ChildType.CHILD_1:
            return Child1()
        if childType == ChildType.CHILD_2:
            return Child2()
        if childType == ChildType.CHILD_3:
            return Child3()
        return None
