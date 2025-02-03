from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("Passed value: ", x)
    @abstractmethod
    def task(self):
        print("I am in abstract method")
class test_class(Absclass):
    def task(self):
        print("I am in test class")
tests = test_class()
tests.task()
tests.print(29)
