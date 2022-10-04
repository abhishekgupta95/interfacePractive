import abc


class ParentInterface(abc.ABC):
    @abc.abstractmethod
    def demo(self):
        pass
