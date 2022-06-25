#LINK: https://www.hackerrank.com/challenges/calendar-module
#Language: Python
#Difficulty: Easy


import calendar

mm, dd, yyyy=map(int, input().split())

weekday = calendar.weekday(yyyy, mm, dd)

print((calendar.day_name[weekday]).upper())
