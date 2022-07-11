class ParkingGarage():

    def __init__(self):
        self.tickets = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.parkingSpaces = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.currentTicket = {}

    def takeTicket(self):
        for i in range(len(self.tickets and self.parkingSpaces)):
            self.tickets[i] = self.tickets[i] - 1
            if i == 0:
                print('Sorry, the Parking Garage is full!')
        return

    def payForParking(self):
        amount = input('Enter 1 to pay now: ')
        if amount == 1:
            self.currentTicket['Paid'] = True
            print('ticket has been paid, you have 15 minutes to leave')
        else:
            False                

    def leaveGarage(self):
        amount = input('Enter 1 to pay now: ')
        while True:
            for i in range(len(self.tickets and self.parkingSpaces)):
                self.parkingSpaces[i] = self.parkingSpaces[i] + 1
                if self.currentTicket == True:
                    print('Thank you, have a nice day!')
                else:
                    self.currentTicket == False
                    print(amount)
            return


def main():
    car = ParkingGarage
    print('Welcome to the Parking Garage!\n')
    print('Please take a ticket.')
    printedTicket = input('Enter T to take ticket: ')
    if printedTicket.upper() == "T":
        car.takeTicket(car, tickets = -1, parkingSpaces = -1)
    else:
        print('Error')

main()