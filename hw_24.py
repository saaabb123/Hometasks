from DateTimeError import DateTimeError

class Date:
    def __init__(self,year,month,day):
        self.validation(year,month,day)
        self.year = year
        self.month = month
        self.day = day
    
    def validation(self,year,month,day):
        if not isinstance(year,int) or year < 0 or year > 9999:
            raise DateTimeError("year", year,"between 0 and 9999")

        if not isinstance(month,int) or month < 1 or month > 12:
            raise DateTimeError("month",month,"between 1 and 12")
    
        if not isinstance(day,int) or day < 1 or day > 31:
            raise DateTimeError("day",day,"between 1 and 31")
    

    def __str__(self):
        return f"{self.year}/{self.month:0>2}/{self.day}"


class DateTime(Date):
    def __init__(self,year,month,day,hour,minute,second):
        super().__init__(year,month,day)
        self.validation_time(hour,minute,second)
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def validation_time(self,hour,minute,second):
        if not isinstance(hour,int) or hour < 0 or hour > 23:
            raise DateTimeError("hour", hour,"between 0 and 23")

        if not isinstance(minute,int) or minute < 0 or minute > 59:
            raise DateTimeError("minute",minute,"between 0 and 59")
    
        if not isinstance(second,int) or second < 0 or second > 59:
            raise DateTimeError("second",second,"between 0 and 59")
    

    def __str__(self):
        return super().__str__() + f"\n{self.hour}:{self.minute}:{self.second}"



try:
    date = Date(2019,2,35)
    print(date)
except DateTimeError as e:
    print(e)

try:
    date_time = DateTime("b",10,30,10,56,35)
    print(date_time)
except DateTimeError as e:
    print(e)