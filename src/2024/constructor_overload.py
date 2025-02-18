"""
Write a class in your favorite language that maintains a moving average of the most recent N float values. The class should have the following public interface:

MovingAverage(int maxValues) – Constructor.
float MovingAverage::value() – Returns the current moving average value.
void MovingAverage::push(float value) – Includes a new value in the moving average.

Please try to write real code, but don’t worry if you can’t remember some syntax perfectly.
"""
class MovingAverage:
    def __init__(self, maxValues: int):
        self.maxValues = maxValues
        self.values = []
        self.sum = 0

    def value(self) -> float:
        return self.sum / len(self.values) if self.values else 0

    def push(self, value: float) -> None:
        if len(self.values) == self.maxValues:
            self.sum -= self.values.pop(0)
        self.values.append(value)
        self.sum += value

class test():

    def __init__(self):
        self.test = "Hello World"

    def change_test(self, x: int):
        print("int: %d" % x)
    
    def change_test(self, x: float):
        print("float: %f" % x)

t = test()
y = int(1)
t.change_test(y)
t.change_test(1.5)


