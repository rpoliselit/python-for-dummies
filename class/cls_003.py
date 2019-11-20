# Class inheritance

class Device:

    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected =  True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})" # !r makes the self.name being printed between ''.

    def disconnected(self):
        self.connected = False
        print("Disconnected.")

class Printer(Device):

    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages


printer_1 = Device("Printer", "USB")
print(printer_1)
printer_1.disconnected()
print("-"*50)

printer_2 = Printer("Printer", "USB", 500)
printer_2.print(20)
print(printer_2)
printer_2.disconnected()
printer_2.print(40)
