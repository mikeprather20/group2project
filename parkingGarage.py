class ParkingGarage():

    def __init__(self):
        self.tickets = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.parkingSpaces = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.currentTicket = {}

    def takeTicket(self, tickets, parkingSpaces):
        for i in range(len(self.tickets and self.parkingSpaces)):
            self.tickets[i] = self.tickets[i] - 1
            print(self.tickets)
            if i == 0:
                print('Sorry, the Parking Garage is full!')
        return

    def payForParking(self, currentTicket):
        amount = input('Enter 1 to pay now: ')
        if amount == 1:
            self.currentTicket['Paid'] = True
            print('ticket has been paid, you have 15 minutes to leave')
        else:
            False
    
                

    def leaveGarage(self, tickets, parkingSpaces, currentTicket):
        for i in range(len(self.tickets and self.parkingSpaces)):
            self.parkingSpaces[i] = self.parkingSpaces[i] + 1

            if self.currentTicket == True:
                print('Thank you, have a nice day!')
            else:
                self.currentTicket == False
                amount = input('Please pay your 1 dollar ticket fee.')


def main():
    car = ParkingGarage

    while True:
        pass


main()
