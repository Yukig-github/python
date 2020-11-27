#3FS1-75 福田湧基
#販売個数計算

from random import randint

class All :
	maker ="MOMO"
	count = 0
	
	@classmethod
	def counttime(cls) :
		cls.count += 1
		print(f"本日の販売数{cls.count} 個")
		
	def sell(self, thing ="ドーナツ"):
		buy.counttime()
		self.num = All.count
		self.thing = thing
		self.price = randint(120,200)*0.1

	def calc(self, num):
		self.price += num
		msg = f"先ほどのお客様は{num}円購入しました。"
		print(msg)