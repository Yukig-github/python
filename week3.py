#3FS1-75 福田湧基

week= input("授業は第何週ですか？: ")
#4
cl = input("クラス名を入力してください: ")
#3FS1
num = input("出席番号を入力してください: ")
#75
name = input("氏名を入力してください: ")
#福田湧基
s = "5月13日、第{}週提出課題、{} {} {} "
text = s.format(week,cl,num,name)
print(text)