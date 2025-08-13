import datetime
from datetime import date

# https://www.datacamp.com/tutorial/converting-strings-datetime-objects

my_date1 = date(2023, 3, 1)
my_date2 = date(2024, 5, 12)

# putem sa accesam atributele datei (zi, luna, an)
year = my_date1.year
month = my_date1.month
day = my_date1.day

print(year, month, day)

# putem sa facem diferenta in zile dintre doua date

difference = my_date1 - my_date2
print(type(difference))
print(difference.days)

# putem sa comparam doua date
print(my_date2 > my_date1)

# date_str = my_date2.strftime('%Y-%m-%d')
