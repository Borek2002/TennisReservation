import datetime
from reservation import Reservation
from name import Name


class ReservationManager:
    def __init__(self):
        self.command = None
        self.reservations = []

    def startProgram(self):
        print("Welcome to the court reservation system.")
        print("Write below command to move on. Commands:")
        print(
            "Commands: \n - Make a reservation \n - Cancel a reservation \n - Print schedule \n - Save schedule to a file \n - Exit")
        self.command = input()
        while (self.command != "Exit"):
            if (self.command == "Make a reservation"):
                self.makeReservation()
            elif (self.command == "Cancel a reservation"):
                self.cancelReservation()
            elif (self.command == "Print schedule"):
                self.printSchedule(datetime.datetime(2022, 2, 6, 15, 15),datetime.datetime(2022, 2, 15, 15, 15))
            elif (self.command == "Save schedule to a file"):
                print("save")
            else:
                print("Invalid command")
            print(
                "Commands: \n - Make a reservation \n - Cancel a reservation \n - Print schedule \n - Save schedule to a file \n - Exit")
            self.command = input()
        print("See You")

    def makeReservation(self):
        newReservation1 = Reservation(Name("d", "b"), datetime.datetime(2022, 2, 13, 15, 15), 60)
        newReservation2 = Reservation(Name("d", "b"), datetime.datetime(2022, 2, 7, 15, 15), 60)
        newReservation3 = Reservation(Name("d", "b"), datetime.datetime(2022, 2, 14, 15, 15), 60)
        self.addReservation(newReservation1)
        self.addReservation(newReservation2)
        self.addReservation(newReservation3)
        print("What's your Name?")
        fullname = input().split()
        print("When would you like to book? {DD.MM.YYYY HH:MM}")
        dateAndTimeStart = input().split()
        dateStart = dateAndTimeStart[0].split(".")
        timeStart = dateAndTimeStart[1].split(":")
        newReservation = Reservation(Name(fullname[0], fullname[1]),
                                     datetime.datetime(int(dateStart[2]), int(dateStart[1]), int(dateStart[0]), int(timeStart[0]),
                                                       int(timeStart[1])), 60)
        reservationOutput = self.checkReservation(newReservation)
        if (reservationOutput == 0):
            self.addReservation(newReservation)
            print("Successful reservation")
        elif (reservationOutput == 1):
            print("You can't reserve tennise court more than 2 times a week")
        elif (reservationOutput == 2):
            print("The given date is not available")
        elif (reservationOutput == 3):
            print("It's to late to reserve court")

    def addReservation(self, reservation):
        i = 0
        while (i != len(self.reservations)):
            if reservation.getDateAndTime() < self.reservations[i].getDateAndTime():
                self.reservations.insert(i, reservation)
                break
            i += 1
        if (i == len(self.reservations)):
            self.reservations.append(reservation)

    def checkReservation(self, reservation):
        exception = self.check2ReservationInWeek(reservation)
        if (exception == 1):
            return exception
        exception = self.availableGivenDate(reservation)
        if (exception == 2):
            return exception
        exception = self.lessThan1Hour(reservation)
        if (exception == 3):
            return exception

    def check2ReservationInWeek(self, reservation):
        for i in range(len(self.reservations)):
            counterReservations = 0
            if ((reservation.fullName.getSurname() == self.reservations[i].fullName.getSurname()) &
                    (reservation.fullName.getFirstname() == self.reservations[i].fullName.getFirstname())):
                counterReservations += 1
            for j in range(i + 1, len(self.reservations)):
                difference = self.reservations[i].getDateAndTime().weekday() - self.reservations[
                    j].getDateAndTime().weekday()
                if (difference >= 0):
                    if ((self.reservations[i].getDateAndTime() <= reservation.getDateAndTime()) &
                            (self.reservations[j].getDateAndTime() >= reservation.getDateAndTime()) & (
                                    difference <= 7)):
                        if ((reservation.fullName.getSurname() == self.reservations[j].fullName.getSurname()) &
                                (reservation.fullName.getFirstname() == self.reservations[j].fullName.getFirstname())):
                            counterReservations += 1
                    if (counterReservations >= 2):
                        return 1
                    else:
                        break
        return 0

    def availableGivenDate(self, reservation):
        for item in self.reservations:
            if item.getDateAndTime() == reservation.getDateAndTime():
                return 2
        return 0

    def lessThan1Hour(self, reservation):
        currentdate = datetime.datetime.now()
        odd = reservation.getDateAndTime() - currentdate
        if (odd.seconds < 3600):  # 3600 minutes in 1 hour
            return 3
        return 0

    def cancelReservation(self):
        print("What's your Name?")
        fullname = input().split()
        print("Enter the date you want cancel {DD.MM.YYYY HH:MM}")
        dateAndTime = input().split()
        date = dateAndTime[0].split(".")
        time = dateAndTime[1].split(":")
        cancelReservation = Reservation(Name(fullname[0], fullname[1]),
                                     datetime.datetime(int(date[2]), int(date[1]), int(date[0]), int(time[0]),
                                                       int(time[1])), 60)
        exepction = self.findReservationToCancel(cancelReservation)
        if (exepction == 1):
            print("You don't have reservation at this time")
            return
        exepction = self.lessThan1Hour(cancelReservation)
        if (exepction == 3):
            print("It's to late to cancel a reservation")
            return
        if(exepction==0):
            print("You canceled your reservation")

    def findReservationToCancel(self, reservation):
        for i in range(len(self.reservations)):
            if (self.reservations[i].getDateAndTime() == reservation.getDateAndTime()) & \
                    (self.reservations[i].fullName.getFirstname() == reservation.fullName.getFirstname()) \
                    & (self.reservations[i].fullName.getSurname() == reservation.fullName.getSurname()):
                self.reservations.pop(i)
                return 0
        return 1

    def printSchedule(self,dateStart,dateEnd):
        for i in range(len(self.reservations)):
            if ((dateStart <= self.reservations[i].getDateAndTime()) &
                    (dateEnd >= self.reservations[i].getDateAndTime())):
                self.reservations[i].printReservation()

    def deleteOldReservation(self):
        currentdate = datetime.datetime.now()
        for i in range(len(self.reservations)):
            if self.reservations[i].getDateAndTime()<currentdate:
                self.reservations.pop(i)


