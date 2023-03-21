from datetime import timedelta
from datetime import datetime

from name import Name
class Reservation:
    dateAndTimeEnd = None
    courtBookingTime = None
    def __init__(self,name,dateAndTime):
        self.fullName=name
        self.dateAndTimeStart=dateAndTime



    def setCourtTimeAndEndTime(self,minutes):
        self.courtBookingTime=minutes
        self.dateAndTimeEnd=self.dateAndTimeStart+timedelta(minutes=minutes)

    def getDateAndTime(self):
        return self.dateAndTimeStart

    def getDateAndTimeEnd(self):
        return self.dateAndTimeEnd

    def getCourtBookingTime(self):
        return self.courtBookingTime

    def printReservation(self):
        print(self.fullName.getFirstname()+" "+self.fullName.getSurname()+" ",end = '')
        print(datetime.strftime(self.dateAndTimeStart, '%d')+"."+datetime.strftime(self.dateAndTimeStart, '%m')+
              "."+datetime.strftime(self.dateAndTimeStart, '%Y')+" "+datetime.strftime(self.dateAndTimeStart, '%H')+":"
              +datetime.strftime(self.dateAndTimeStart, '%M')+" - ",end = '')
        print(datetime.strftime(self.dateAndTimeEnd, '%d')+"."+datetime.strftime(self.dateAndTimeEnd, '%m')+
              "."+datetime.strftime(self.dateAndTimeEnd, '%Y')+" "+datetime.strftime(self.dateAndTimeEnd, '%H')+":"
              +datetime.strftime(self.dateAndTimeEnd, '%M'))
