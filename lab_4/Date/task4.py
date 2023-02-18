import datetime as dt

str_d1 = input('Enter first date (year/month/day) : ')
str_d2 = input('Enter second date (year/month/day) : ')
d1 = dt.datetime.strptime(str_d1, "%Y/%m/%d")
d2 = dt.datetime.strptime(str_d2, "%Y/%m/%d")
delta = (d1 - d2)
print(delta.days * 24 * 60 * 60)


# 2023/02/18