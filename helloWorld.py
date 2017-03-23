# -*- coding: utf-8 -*-
#ex1
print 'hello world!'
print "hello again"
print "I like typing this"
print 'This is fun!'
print 'Yay! Printing!'
print "I'd much rather than 'not' "
print 'i "said" do not touch this'
print 'print again'

#ex2
#A comment ,this is so you can read your program later.
#Anything after the # is igonored by python
print 'I could have code like this' # and the comment after is ignored
# print ' this will not run'
print 'this will run!'

#ex3
print 'I will now coun my chickens:' #输出字符串
print "hens",25+30.0/6,666,333 #使用逗号分隔开不同的输入数据
print "roosters",100 - 25 * 3.0 % 4 #,在输出的时候自动把逗号变成空格
print "Now I will count the eggs:"
print 3 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4 + 6 # 百分号运算优先级大于加减运算
print "Is it true that 3+2<5-7?"
print 3+2<5-7 #加减运算优先级大于逻辑运算
print "what is 3+ 2?",3+2 
print "what is 5 - 7?",5-7
print "oh,that's why it's false"
print "how about some more."
print "Is it greater?",5 > -2 #输出布尔值 True of False
print "Is it greater or equel?",5 >= -2 #输出布尔值
print "Is it less or equel?", 5 <= -2
# 优先级 括号>指数>乘>=除>加>=减 PEMDAS

#ex4
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool = cars_driven * space_in_a_car
average_passengers = passengers / cars_driven
print "There are",cars,"cars available"
print "There are only", drivers,"drivers available"
print "There will be",cars_not_driven,"empty cars today"
print "We can transport",carpool,"people today"
print "We have",passengers,"to carpool today"
print "We need to put about",average_passengers,"in each car."
print "Hey %r There." % "you"

#ex5
name = 'Zed A. shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
print "Let's talk about %r." % name
print "He's %r inches tall." % height
print "He's %r pounds heavy" % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth
# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (age, height, weight, age + height + weight)

#ex6
x = "There are %d types of people" % 10 # %后面的10 对应着字符串内的 %d
binary = "binary" # 给binary变量赋值"binary"
do_not = "don't" # 给do_not变量赋值
y = "Those who know %s and those who %s." % (binary,do_not) # 变量分别给%s 和 %s
print x # 打印x
print y # 打印y
print "I said: %r" % x # 打印 
print "I also said: '%s'." % y #打印
hilarious = False # 给hilarious 赋值一个布尔值
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious
w ="This is the left side of..."
e = "a string with a right side."
print w + e

#ex7
print "Mary had alittle lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10 # what'd that do?
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# watch taht comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

#ex8
formatter = "%r %r %r %r"
print formatter % (1,2,3,4)
print formatter % ("哈哈 ","two","three","four")
print formatter % (True,False,True,False)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
  "I had this thing.",
  "That you could type up right.",
  "But it didn't sing",#如果语句中有出现引号，则外面使用双引号，里面的使用单引号
  "So I said goodning." 
)

#ex9
# Here's some nw strange stuff, remember type it exactly
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print "Here are the days: " , days
print "Here are the months: ", months
print """
There 's something going on here.
"""

#ex10
tabby_cat = "\tI'm tabbed in"
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
\t* i'will do it
\t* hahasb
\t* what can we do?
\v what's this?
\r what's this again?
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
num = 0
while True:
  num += 1
  print num