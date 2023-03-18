from datetime import timedelta
from datetime import datetime

from name import Name
class Reservation:
    def __init__(self,name,dateAndTime,courtBookingTime):
        self.fullName=name
        self.dateAndTimeStart=dateAndTime
        self.courtBookingTime=courtBookingTime
        self.dateAndTimeEnd=dateAndTime+timedelta(minutes=courtBookingTime)
    def getDateAndTime(self):
        return self.dateAndTimeStart
    def getCourtBookingTime(self):
        return self.courtBookingTime
    def printReservation(self):
        print(self.fullName.getFirstname()+" "+self.fullName.getSurname()+" ",end = '')
        print(datetime.strftime(self.dateAndTimeStart, '%d')+"."+datetime.strftime(self.dateAndTimeStart, '%m')+
              "."+datetime.strftime(self.dateAndTimeStart, '%y')+" "+datetime.strftime(self.dateAndTimeStart, '%H')+":"
              +datetime.strftime(self.dateAndTimeStart, '%M')+" - ",end = '')
        print(datetime.strftime(self.dateAndTimeEnd, '%d')+"."+datetime.strftime(self.dateAndTimeEnd, '%m')+
              "."+datetime.strftime(self.dateAndTimeEnd, '%y')+" "+datetime.strftime(self.dateAndTimeEnd, '%H')+":"
              +datetime.strftime(self.dateAndTimeEnd, '%M'))
