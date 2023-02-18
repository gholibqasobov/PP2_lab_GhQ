import datetime as dt

print(dt.datetime.now() - dt.timedelta(0, 0, dt.datetime.now().microsecond))