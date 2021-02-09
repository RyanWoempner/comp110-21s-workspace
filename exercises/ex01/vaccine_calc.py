"""A vaccination calculator."""

__author__ = "YOUR PID HERE"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
today: datetime = datetime.today()
one_day: timedelta = timedelta(1)
tomorrow: datetime = today + one_day
fortnight: timedelta = timedelta(7 + 7)
future: datetime = today + fortnight

Population: int = int(input("Population: "))
Doses_administered: int = int(input("Doses administered: "))
Doses_per_day: int = int(input("Doses per day: "))
print("Target percent Vaccinated: 80")

Reach_vaccination_point: int = int((((Population*2) - (Doses_administered)) / (Doses_per_day)) * 0.8) 

print(input("We will reach 80% vaccination in " + input(Reach_vaccination_point)))
