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
        print(f"Binary: Subject '{subject.name}' has data " + Colors.OKGREEN + f"{bin(subject.data)}"+ Colors.ENDC)

class OctalViewer:
    def update(self, subject):
        print(f"Octal: Subject '{subject.name}' has data " + Colors.OKGREEN + f"{oct(subject.data)}"+ Colors.ENDC)

class HexaViewer:
    def update(self, subject):
        print(f"Hexadecimal: Subject '{subject.name}' has data " + Colors.OKGREEN + f"{hex(subject.data)}"+ Colors.ENDC)

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

    viewers = {
        'binary': view1,
        'octal': view2,
        'hexadecimal': view3
    }

    while True:
        try:
            print("\nOptions:")
            print(Colors.OKCYAN +"1."+ Colors.ENDC +" Enter a number")
            print(Colors.OKCYAN +"2."+ Colors.ENDC +" Create new object with all viewers attached")
            print(Colors.OKCYAN +"3."+ Colors.ENDC +" Detach all viewers and delete current object")
            print(Colors.OKCYAN +"4."+ Colors.ENDC +" Exit")

            choice = input("Select an option: ").strip()

            if choice == '1':  # Enter a number
                user_input = input("Please enter a number: ").strip()
                try:
                    obj.data = int(user_input)
                except ValueError:
                    print(Colors.WARNING + "Invalid input. Please enter a valid integer." + Colors.ENDC)
            elif choice == '2':  # Create new object
                print("Available option: 'all' to create a new object with all viewers attached.")
                viewer_type = input("Enter the viewer type: ").strip().lower()
                if viewer_type == 'all':
                    obj_name = input("Enter the name for the new object: ").strip()  # Ask user for object's name
                    new_object = Data(obj_name)  # Create new object
                    for viewer in viewers.values():
                        new_object.attach(viewer)
                    print(Colors.OKGREEN + f"New object '{obj_name}' created with all viewers attached." + Colors.ENDC)
                    obj = new_object 
                else:
                    print(Colors.WARNING + "Invalid option. Use 'all' to create a new object." + Colors.ENDC)
            elif choice == '3':  # Detach all viewers and delete object
                if obj.name == 'My Calculator':  # Prevent deletion of default object
                    print(Colors.WARNING + "The default object 'My Calculator' cannot be deleted." + Colors.ENDC)
                else:
                    confirm = input("Are you sure you want to delete this object? (yes/no): ").strip().lower()
                    if confirm == 'yes':
                        print("Detaching all viewers from current object.")
                        for viewer in viewers.values():
                            obj.detach(viewer)
                        obj_name = obj.name  # Store name for confirmation
                        obj = Data('My Calculator')  # Revert to the default object
                        view1 = BinaryViewer()
                        obj.attach(view1)
                        view2 = OctalViewer()
                        obj.attach(view2)
                        view3 = HexaViewer()
                        obj.attach(view3)
                        new_object = None  # Clear the reference to the deleted object
                        print(Colors.OKGREEN + f"All viewers detached and the object '{obj_name}' has been deleted." + Colors.ENDC)
                    else:
                        print(Colors.WARNING + "Deletion canceled." + Colors.ENDC)
            elif choice == '4':  # Exit
                print(Colors.OKGREEN + "Thank you, Goodbye!" + Colors.ENDC)
                break
            else:
                print(Colors.WARNING + "Invalid option. Please try again." + Colors.ENDC)
        except ValueError:
            print(Colors.WARNING + "Invalid input. Please enter a valid integer." + Colors.ENDC)

if __name__ == '__main__':
    main()
