class ParkingGarage():

    def __init__(self):
        self.tickets=[0,1,2,3,4,5,6,7,8,9,10]
        self.parkingSpaces=[0,1,2,3,4,5,6,7,8,9,10]
        self.currentTicket={}

    def takeTicket(self, tickets, parkingSpaces):
        for i in range(len(self.tickets and self.parkingSpaces)):
            self.tickets[i] = self.tickets[i] - 1
            print(self.tickets)
            if i == 0:
                print ('Sorry, the Parking Garage is full!')
        return
        
    def payForParking(self, currentTicket):
        payment = input('Please pay your ticket')
        pass

    def leaveGarage(self, tickets, parkingSpaces, currentTicket):
        pass


def main():
    car = ParkingGarage

    while True:
        pass

main()