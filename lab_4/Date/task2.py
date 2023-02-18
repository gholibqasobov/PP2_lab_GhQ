import datetime as dt

print('yesterday: ', dt.date.today() - dt.timedelta(1))
print('today: ', dt.date.today())
print('tomorrow: ', dt.date.today() + dt.timedelta(1))