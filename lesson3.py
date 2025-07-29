import datetime
name=input('who are you?:  ')
name=name.lower()
dob=input("when is your birthday/(DD/MM/YYYY):  ")
tod=datetime.datetime.today()
#extracting today's year
yr=tod.year
yob=dob[6:]
yob=int(yob)
age=yr-yob
reverse=name[::-1]
print(f"Hi {reverse}  I know you are {age} years old")
