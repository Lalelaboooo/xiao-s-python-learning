#!/user/bin/env python3
#for the function exp, log, sqrt int the math liberiry
from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter

#basic printout function test
print("Output #1 : I'm excited to learn python.")

x = 4
y = 5
z = x + y
#format output function test
print("Output #2: Four plus Five equals {0:d}".format(z))

a = [1,2,3,4]
b = ["first","Second","third","fourth"]
c = a + b

print("Output #3: {0},{1},{2}".format(a,b,c))
x = 9

print("Output #4: {0}".format(x))
print("Output #5: {0}".format(3**4))
print("Outpiut #6: {0}".format(int(8.3)/int(2.7)))
print("Output #7: {0:.3f}".format(8.3/2.7))
y = 2.5*4.8

print("Output #8: {0:.1f}".format(y))
r = 8/float(3)

print("Output #8: {0:.2f}".format(r))
print("Output #10: {0:.4f}".format(8.0/3))
print("Output #11: {0:.1f}".format(exp(2)))
print("Output #12: {0:.3f}".format(log(4)))
print("Output #13: {0:.4f}".format(sqrt(81)))

#string test
print("Output #14: {0:s}".format('I\'m enjoying python.'))
print("Output #15: {0:s}".format("This is a long string. Without the backlash\
it would run off of the page on the right in the text editor and be very\
diffcult to read and edit. By using the backlash you can split the long\
string into smaoller string on separate lines so that the whole string is easy\
to view in the text editor."))
print("Output #16: {0:s}".format('''You can use triple single quotes for multi-line comment strings.'''))
print("Outout #17: {0:s}".format("""You can also use triple double quotes for multil-line comment strings."""))

# The operation of the string * and +
string1 = "This is a "
string2 = "short string."
sentence = string1 + string2

print("Output #18: {0:s}".format(sentence))
print("Output #19: {0:s} {1:s}{2:s}".format("She is", "very "*4, "beautiful."))
m = len(sentence)
print("Output #20: {0:d}".format(m))

#function split test
string1 = "My deliverable is due in May"
string1_list1 = string1.split()
string1_list2 = string1.split(" ",2)

print("Output #21: {0}".format(string1_list1))
print("Output #22: FIRST PIECE:{0} SECONDE PIECE:{1} THIRD PIECE:{2}"\
	.format(string1_list2[0],string1_list2[1],string1_list2[2]))

string2 = "Your,deliverable,is,due,in,June"
string2_list = string2.split(',')

print("Output #23: {0}".format(string2_list))
print("Output #24: {0},{1},{2}".format(string2_list[1],string2_list[5],\
	string2_list[-1]))

#function join test
print("Output #25: {0}".format(','.join(string2_list)))

#function strip test
string3 = " remove unwanted characters    from this string.\t\t    \n"
print("Output #26: string3: {0:s}".format(string3))
string3_lstrip = string3.lstrip()	#from left to delete
print("Output #27: lstrip:{0:s}".format(string3_lstrip))
string3_rstrip = string3.rstrip()	#from right to delete 
print("Output #28: rstrip:{0:s}".format(string3_rstrip))
string3_strip = string3.strip()		
print("Output #29: strip:{0:s}".format(string3_strip))

string4 = "$$Here's another string that has unwanted characters.__---++"

print("Output #30: {0:s}".format(string4))

string4 = "$$The unwanted characters have been removed.__---++"
string4_strip = string4.strip('$_-+')

print("Output #31: {0:s}".format(string4_strip))

#function replace test
string5 = "Let's replace the spaces in this sentence with other characters."
string5_replace = string5.replace(" ","!@!")

print("Outout #32 (with !@!): {0:s}".format(string5_replace))

string5_replace = string5.replace(" ",",")

print("Output #33(with commas): {0:s}".format(string5_replace))

#function lower,upper,capitalize
string6 = "Here's WHAT Happens WHEN You Use lower."
print("Output #34: {0:s}".format(string6.lower()))
string7 = "Here's what Happens when You Use UPPER."
print("Output #35: {0:s}".format(string7.upper()))
string5 = "here's WHAT Happens WHEN you use Capitalize."
print("Output #36: {0:s}".format(string5.capitalize()))

string5_list = string5.split()

print("Output #37:(on each word):")
for word in string5_list:
	print("\t\t\t{0:s}".format(word.capitalize()))

#function (re.compile, re.search, re.sub, re.ignorecase, re.I) test
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"The",re.I)
count = 0

for word in string_list:
	if pattern.search(word):
		count += 1
print("Output #38: {0:d}".format(count))

# in the string, outputiing the word which is found
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"(?P<match_word>The)",re.I)

print("Output #39:")
for word in string_list:
	if pattern.search(word):
		print("{0:s}".format(pattern.search(word).group('match_word')))
# using 'a' changs "the" in the string
string = "The quick brown fox jumps over the lazy dog."
string_to_find =r"The"
pattern = re.compile(string_to_find,re.I)

print("Output #40:{:s}".format(pattern.sub("a",string)))

# time function test
#print out today's date form, year, month, day
today = date.today()

print("Output #41: today: {0!s}".format(today))
print("Output #42: {0!s}".format(today.year))
print("Output $43: {0!s}".format(today.month))
print("Output #44: {0!s}".format(today.day))

current_datetime = datetime.today()

print("Output #45:{0!s}".format(current_datetime))

#using datetime to caculate a new date
one_day = timedelta(days=-1)
yesterday = today + one_day

print("Output #46: yesterday: {0!s}".format(yesterday))
eight_hours = timedelta(hours=-8)
print("Output #47: {0!s} {1!s}".format(eight_hours.days, eight_hours.seconds))

#caculate the days between two dates
date_diff = today - yesterday
print("Output #48: {0!s}".format(date_diff))
print("Output #49: {0!s}".format(str(date_diff).split()[0]))

#creating a special form string based on one date object
print("Output #50: {!s}".format(today.strftime('%m/%d/%Y')))
print("Output #51: {!s}".format(today.strftime('%b %d, %Y')))
print("Output #52: {!s}".format(today.strftime('%Y-%m-%d')))
print("Output #53: {!s}".format(today.strftime('%B %d, %Y')))

#based on a string which means date
#creating a datetime object which has a special forms
date1 = today.strftime('%m/%d/%Y')
date2 = today.strftime('%b %d, %Y')
date3 = today.strftime('%Y-%m-%d')
date4 = today.strftime('%B %d, %Y')

#based on 4 different string that has date form
#creating 2 datetime object and 2 date object
print("Output #54: {!s}".format(datetime.strptime(date1, '%m/%d/%Y')))
print("Output #55: {!s}".format(datetime.strptime(date2, '%b %d, %Y')))

#only show the date part
print("Output #56: {!s}".format(datetime.date(datetime.strptime\
	(date3, '%Y-%m-%d'))))
print("Output #57: {!s}".format(datetime.date(datetime.strptime\
	(date4, '%B %d, %Y'))))


#create a list with [ ]
#using len() to caculate the number of a list
#using max() and min() find out the maximum and minimum value
#using count() to caculate the times of one value in the list
a_list = [1, 2, 3]
print("Output #58: {}".format(a_list))
print("Output #59: a_list has {} elemnets.".format(len(a_list)))
print("Output #60: the maximum value in a_list is: {}.".format(max(a_list)))
print("Output #61: the minimum value in a_list is: {}.".format(min(a_list)))

another_list = ['priner', 5, ['star', 'circle',9]]
print("Output #62: {}".format(another_list))
print("Output #63: another_list also has {} elements.".format\
	(len(another_list)))
print("Output #64: 5 is in another_list {} time.".format(another_list.count(5)))

#using index value to visit perticular element
#[0]is the first element,[-1] is the last element
print("Output #65: {}".format(a_list[0]))
print("Output #66: {}".format(a_list[1]))
print("Output #67: {}".format(a_list[2]))
print("Output #68: {}".format(a_list[-1]))
print("Output #69: {}".format(a_list[-2]))
print("Output #70: {}".format(a_list[-3]))
print("Output #71: {}".format(another_list[2]))
print("Output #72: {}".format(another_list[-1]))

#list slice
#using list slice to visit list
#slice from the head, it can omit the first index value
#slice to the end, it can omit the second index value
print("Output #73: {}".format(a_list[0:2]))
print("Output #74: {}".format(another_list[:2]))
print("Output #75: {}".format(a_list[1:3]))
print("Output #76: {}".format(another_list[1:]))

#copy list
#using [;]copy a list
a_new_list = a_list[:]
print("Output #77: {}".format(a_new_list))

#the list of connected
#using + connected two or more list
a_longer_list = a_list + another_list
print("Output #78: {}".format(a_longer_list))

#in and not in
#using in and not in to check out if the element in the list
a = 2 in a_list
print("Output #79: {}".format(a))
if 2 in a_list:
	print("Output #80: 2 is in {}".format(a_list))
b = 6 not in a_list
print("Output #81: {}".format(b))
if 6 not in a_list:
	print("Outout #82: 6 is not in {}".format(a_list))

#add, delete and pop element
#using append () to add an element from the end of the list
#using remove() to delete a perticular element from the list
#using pop() to delete an element form the end of the list
a_list.append(4)
a_list.append(5)
a_list.append(6)
print("Output #83: {}".format(a_list))
a_list.remove(5)
print("Output #84: {}".format(a_list))
a_list.pop()
a_list.pop()
print("Output #85: {}".format(a_list))

#reverse list
#using sort() to sort list, it will modify the list
#if willing to sort list but don't want to modify the list, the way is first copy the list
unordered_list = [3, 5, 1, 7, 2, 8, 4, 9,0,6]
print("Output #88: {}".format(unordered_list))
list_copy = unordered_list[:]
list_copy.sort()
print("Output #89: {}".format(list_copy))
print("Output #90: {}".format(unordered_list))

#sorted 
my_lists = [[1,2,3,4],[4,3,2,1],[2,4,1,3]]
my_lists_sorted_by_index_3 = sorted(my_lists, key = lambda index_value:\
		index_value[3])
print("Output #91: {}".format(my_lists_sorted_by_index_3))

#using  itemgetter() to sort list by two index position
my_lists = [[123,2,2,444], [22,6,6,444], [354,4,4,678], [236,5,5,678],\
	  [578,1,1,290], [461,1,1,290]]
my_lists_sorted_by_index_3_and_0 = sorted(my_lists, key = itemgetter(3,0))
print("Output #92: {}".format(my_lists_sorted_by_index_3_and_0))

#tuple
#create a tuple
#using  ( ) to create tuple
my_tuple = ('x', 'y', 'z')
print("Output #93: {}".format(my_tuple))
print("output #94: my_tuple has {} elements".format(len(my_tuple)))
print("Output #95: {}".format(my_tuple[1]))

longer_tuple = my_tuple + my_tuple
print("Output #96: {}".format(longer_tuple))

#tuple unpacking
#using left value to tuple unpacking
one, two, three = my_tuple
print("Output #97: {0} {1} {2}".format(one, two,three))
var1 = 'red'
var2 = 'robin'
print("Output #98: {} {}".format(var1, var2))

#change value bettwen variables
var1, var2 = var2, var1
print("Output #99: {} {}".format(var1, var2))

#covert tuple into list
#list convert into tuple
my_list = [1, 2, 3]
my_tuple = ('x', 'y' , 'z')
print("Output #100: {}".format(tuple(my_list)))
print("Output #101: {}".format(list(my_tuple)))

#dictionary
#create a dictionary by {}
#using :to split key-value 
#using len() to caculate the amont of the key-value in dictionary 
empty_dict = {}
a_dict = {'one':1, 'two':2, 'three':3}
print("Output #102: {}".format(a_dict))
print("Output #103: a _dict has {!s} elements".format(len(a_dict)))

another_dict = {'x':'printer', 'y':5, 'z':['star', 'circle', 9]}
print("Output #104: {}".format(another_dict))
print("Output #105: another_dict also has {!s} elements"\
		.format(len(another_dict)))

#using key to refer the perticular value of dictionary
print("Output #106: {}".format(a_dict['two']))
print("Output #107: {}".format(another_dict['z']))

#copy 
#using copy() to copy a dictionary
a_new_dict = a_dict.copy()
print("Output #108: {}".format(a_new_dict))

#key, value, item
#using keys(), values() and items()
#one-by-one refer key, value and items
print("Output #109: {}".format(a_dict.keys()))
a_dict_keys = a_dict.keys()
print("Output #110: {}".format(a_dict_keys))
print("Output #111: {}".format(a_dict.values()))
print("Output #112: {}".format(a_dict.items()))

#using in, not in and get
if 'y' in another_dict:
	print("Output #114: y is a key in another_dict: {}."\
			.format(another_dict.keys()))
if 'c' not in another_dict:
	print("Output #115: c is not a key in another_dict: {}."\
			.format(another_dict.keys()))
print("Output #116: {!s}".format(a_dict.get('three')))
print("Output #117: {!s}".format(a_dict.get('four')))
print("Output #118: {!s}".format(a_dict.get('four', 'Not in dict')))





