# 1. Implement class iterator for Fibonacci numbers https://en.wikipedia.org/wiki/Fibonacci_number
# Iterator get numbers of first Fibonacci numbers
# Example:
#
# for i in FibonacciNumbers(10):
#     print(i)
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
class FibonacciNumbers:
    def __init__(self, quantity):
        self.qty = quantity
        self.f0 = 0
        self.f1 = 0
        self.fn = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.qty >= 0:
            self.f0 = self.f1
            self.f1 = self.fn
            self.fn = self.f0 + self.f1
            self.qty -= 1
            return self.f0
        else:
            raise StopIteration


for i in FibonacciNumbers(10):
    print(i)


# 2.* Implement generator for Fibonacci numbers

def fibonacci_numbers(quantity):
    f1 = 0
    fn = 1
    while quantity >= 0:
        f0 = f1
        f1 = fn
        fn = f0 + f1
        quantity -= 1
        yield f0


for i in fibonacci_numbers(10):
    print(i)

# 3. Write generator expression that returns square numbers of integers from 0 to 10
generator_ex = (num ** 2 for num in range(11))
for elem in generator_ex:
    print(elem)

# 4. Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.
from abc import abstractmethod, ABC


class Laptop(ABC):

    @abstractmethod
    def Screen(self):
        raise NotImplementedError

    @abstractmethod
    def Keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def Touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def Webcam(self):
        raise NotImplementedError

    @abstractmethod
    def Ports(self):
        raise NotImplementedError

    @abstractmethod
    def Dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):
    def __init__(self, screen, keyboard, touchpad, webCam, ports, dynamics):
        self.screen = screen
        self.keyboard = keyboard
        self.touchpad = touchpad
        self.webcam = webCam
        self.ports = ports
        self.dynamics = dynamics

    def Screen(self):
        print(self.screen)

    def Keyboard(self):
        print(self.keyboard)

    def Touchpad(self):
        print(self.touchpad)

    def Webcam(self):
        print(self.webcam)

    def Ports(self):
        print(self.ports)

    def Dynamics(self):
        print(self.dynamics)


# 5. Create an abstract class for the Car with the next methods: drive, stop, open_door, close_door, turn_on_light,
# turn_off_light, enable_radio, disable_radio, where drive and stop will be predefined with some realization, all others
# should be abstract.
class Car(ABC):
    def drive(self):
        print('I drive a car')

    def stop(self):
        print('I stop a car')

    @abstractmethod
    def open_door(self):
        raise NotImplementedError

    @abstractmethod
    def close_door(self):
        raise NotImplementedError

    @abstractmethod
    def turn_on_light(self):
        raise NotImplementedError

    @abstractmethod
    def turn_off_light(self):
        raise NotImplementedError

    @abstractmethod
    def enable_radio(self):
        raise NotImplementedError

    @abstractmethod
    def disable_radio(self):
        raise NotImplementedError
