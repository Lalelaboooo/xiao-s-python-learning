#!/usr/bin/env python3
from math import exp, log, sqrt
import re 
from datetime import datetime, date, time, timedelta
print("hello world")
age = 20
name = 'zhangsan'

print('{} is {} years old.'.format(name,age))
#print('age = {} ', end=''.format(age))
#print('a', end=' ')
#print('b', end=' ')

today = date.today()
print("Today is {0!s}".format(today))
print("{0!s}".format(today.year))
print("{0!s}".format(today.month))
print("{0!s}".format(today.day))

current_time = datetime.today()
print("{0!s}".format(current_time))
now = datetime.today()
print("now is: {0!s}".format(now))

today = date.today()
print("today is: {0!s}".format(today))

one_day = timedelta(days = -1)
yesterday = today + one_day
print("yesterday is: {0!s}".format(yesterday))

eight_hours = timedelta(hours=-8)
print("I don't know how it works, let me check the time: {0!s} {1!s}".format(eight_hours.days, eight_hours.seconds))

tomarrow = timedelta(days=+1)
the_day_after_tomarrow = today + tomarrow

print("The_day_after-tomarrow is: {0!s}".format(the_day_after_tomarrow))

print("\"What's your name?\"")
print("\"What's your name?\"")

length = 10
breath = 5
area = length * breath
print("area is: {}".format(area))
print('perimeter is: ',2 * (length + breath))

#if statement
number = 23
guess = int(input('Enter an integer: '))

if guess == number:
	#start form here
	print('Congratulations, you guessed it.')
	print('(but you do not win any prizes!.)')
elif guess < number:
	print('No, it is a little higher than that')
else:
	print('No, it is a little lower than that.')

print('Done')



