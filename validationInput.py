

def validationName():
    check=False
    fullName=None
    while(check!=True):
        fullName=input()
        if(len(fullName.split())==2):
            check=True
        else:
            print("Incorrect data. Enter your first name and surname.")
    return fullName.split()

def validationDateAndTime():
    check=False
    dateStart=None
    timeStart=None
    while(check!=True):
        dateAndTimeStart = input().split()
        if(len(dateAndTimeStart)==2):
            dateStart = dateAndTimeStart[0].split(".")
            timeStart = dateAndTimeStart[1].split(":")
            if(len(dateStart)==3 and len(timeStart)==2):
                check = True
            else:
                print("Incorrect format of date. Enter correct date. {DD.MM.YYYY HH:MM}")
    return dateStart,timeStart

def validationDate():
    check=False
    dateStart=None

    while(check!=True):
        dateStart = input().split(".")

        if(len(dateStart)==3 ):
            check = True
        else:
            print("Incorrect format of date. Enter correct date. {DD.MM.YYYY}")
    return dateStart

def validationFilenameAndExtension():
    check=False
    inputData=None
    while(check!=True):
        inputData = input().split()
        if(len(inputData)==2):
            if(inputData[1]=="csv"):
                check = True
            else:
                print("Sorry but now only csv format is available. Enter filename and extension again.")
    return inputData


