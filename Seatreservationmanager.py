## Restaurant Seat Reservation manager


class seatReserveManager:
    def __init__(self, n):
        self.current_seat = 0
        self.empty_seats = []

    def reserve(self):
        if len(self.empty_seats) > 0:
            s = min(self.empty_seats)
            self.empty_seats.remove(s)
            return "Reserved" + str(s)
        self.current_seat += 1

        return "Reserved " + str(self.
            current_seat)
    
    def unreserve(self, seatNumber):
        print("unreserved" + str(seatNumber))
        self.empty_seats.append(seatNumber)

print("welcome to our Restaurant\n")
obj = seatReserveManager(7)
print(obj.reserve())
print(obj.reserve())
print(obj.reserve())
obj.unreserve(2)
obj.unreserve(5)
print(obj.reserve())
print(obj.reserve())



