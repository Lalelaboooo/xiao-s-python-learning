#!/user/bin/env python3
#for the function exp, log, sqrt int the math liberiry
from math import exp, log, sqrt
import re
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
pattern = re.compile("The",re.I)
count = 0
for word in string_list:
	if pattern.search(word):
		count += 1
print("Output #38: {0:d}".format(count))


