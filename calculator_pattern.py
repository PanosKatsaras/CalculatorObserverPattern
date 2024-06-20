import abc

class AbstractSubject(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def attach(self):
        pass

    @abc.abstractmethod
    def detach(self):
        pass

    @abc.abstractmethod
    def notify(self):
        pass

class Subject(AbstractSubject):

    def __init__(self):
        self.__observers = []

    def attach(self, observer):
        if observer not in self.__observers:
            self.__observers.append(observer)

    def detach(self, observer):
        try:
            self.__observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        for observer in self.__observers:
            observer.update(self)

class Data(Subject):
    
    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self.__data = 0

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        self.__data = value
        self.notify()


class BinaryViewer:
    def update(self, subject):
        print(f"Binary: Subject '{subject.name}' has data {bin(subject.data)}")

class OctalViewer:
    def update(self, subject):
        print(f"Octal: Subject '{subject.name}' has data {oct(subject.data)}")

class HexaViewer:
    def update(self, subject):
        print(f"Hexadecimal: Subject '{subject.name}' has data {hex(subject.data)}")

class Colors:
   
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'  

def main():
    print(Colors.OKGREEN + "WELCOME" + Colors.ENDC)
    obj = Data('My Calculator')   # An object with data = 0 created
    view1 = BinaryViewer()
    obj.attach(view1)
    view2 = OctalViewer()
    obj.attach(view2)
    view3 = HexaViewer()
    obj.attach(view3)

    while True:
            try:
                user_input = input("Please enter a number (or 'exit' to EXIT): ")
                if (user_input == "exit" or user_input == "Exit" or user_input == "EXIT"):
                    print(Colors.OKGREEN + "Thank you and Goodbye!" + Colors.ENDC)
                    break
                obj.data = int(user_input)
            except ValueError:
                print(Colors.WARNING + "Invalid input. Please enter a valid integer." + Colors.ENDC)

if __name__ == ('__main__'):
    main()