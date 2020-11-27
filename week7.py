#3FS1-75 福田湧基
#給食当番決め
from random import randint

def soup():
	num1 = randint(1,11)
	return num1
def sal():
	num2 = randint(11,21)
	return num2
def okazu():
	num3 = randint(21,31)
	return num3
def rice():
	num4 = randint(31,41)
	return num4



#--------------------
def show() :
	toban1 =soup()
	toban2 =sal()
	toban3 =okazu()
	toban4 =rice()
	print( f"スープ担当{toban1}番、")
	print( f"スープ担当{toban2}番、")
	print( f"スープ担当{toban3}番、")
	print( f"スープ担当{toban4}番、")

print("今週の給食当番を発表します。")
show()
print("今週も頑張りましょう。")


