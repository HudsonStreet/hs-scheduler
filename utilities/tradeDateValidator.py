from datetime import datetime

def is_holiday(date):
    holidays = set(line.strip() for line in open('../2019nonTradeDate.date'))
    is_holiday = date in holidays
    
    return is_holiday
    

def is_tradeday(date):
    weekday = datetime.strptime(date, '%Y-%m-%d').isoweekday()
    if weekday <=5 and not is_holiday(date):
        return True
    else:
        return False