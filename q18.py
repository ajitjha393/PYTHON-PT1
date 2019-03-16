# --------------------------------------------
# METHOD - 1 USING abc class and abstractmethod
from abc import ABC, abstractmethod


# As we have to make printer as Interface ,printer class extends ABC
class Printer(ABC):
    @abstractmethod
    def printit(self, text):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class IBM(Printer):  # Implemented the Printer Interface
    def printit(self, text):  # overriding the abstract Method
        print("IBM PRINTER PRINTED => ", text)

    def disconnect(self):  # overriding the abstract Method
        print("Disconnecting IBM printer ....")


class HP(Printer):
    def printit(self, text):
        print("HP PRINTER PRINTED => ", text)

    def disconnect(self):
        print("Disconnecting HP printer ....")


IBM_printer = IBM()
HP_printer = HP()
IBM_printer.printit(input("Enter the text to be printed : "))
IBM_printer.disconnect()
HP_printer.printit(input("Enter the text to be printed : "))
HP_printer.disconnect()
