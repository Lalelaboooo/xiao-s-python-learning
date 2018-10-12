#!/urs/bin/env python3

x = ['huyiyang', '26', 'mama']
y = ['hanxiao', '28', 'baba']
z = ['pangbao', '1', 'erzi']

f = x + y + z

print(f)


for i in range(len(f)):
    print("Family members:{!s} {0}".format(i),(f))

