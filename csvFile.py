from datetime import datetime
import pandas as pd

class csvFile:
    def __init__(self):
        pass

    def saveToCSVFile(reservations,fileName,dateStart,dateEnd):
        name=[]
        startDate=[]
        endDate=[]
        for item in reservations:
            if (dateStart <= item.getDateAndTime()) & (dateEnd >=item.getDateAndTime()):
                name.append(item.fullName.getFirstname()+" "+item.fullName.getSurname())
                sd=datetime.strftime(item.getDateAndTime(), '%d')+"."+datetime.strftime(item.getDateAndTime(), '%m')+\
                  "."+datetime.strftime(item.getDateAndTime(), '%y')+" "+datetime.strftime(item.getDateAndTime(), '%H')+":"\
                  +datetime.strftime(item.getDateAndTime(), '%M')
                startDate.append(sd)
                ed=datetime.strftime(item.getDateAndTimeEnd(), '%d')+"."+datetime.strftime(item.getDateAndTimeEnd(), '%m')+\
                  "."+datetime.strftime(item.getDateAndTimeEnd(), '%y')+" "+datetime.strftime(item.getDateAndTimeEnd(), '%H')+":"\
                  +datetime.strftime(item.getDateAndTimeEnd(), '%M')
                endDate.append(ed)

        dict={'name': name,'start_date': startDate,'end_date':endDate}
        df = pd.DataFrame(dict)
        df.to_csv(fileName+".csv",index=False)