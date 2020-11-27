#3FS1-75 福田湧基
#注文システム

print("メニュー: シュークリーム/あんぱん/パスタ")
num= input("何を注文しますか？　：")

menu = {"シュークリーム":110, "あんぱん":100, "パスタ":850}

try :
	value = menu[num]
	print(f"{num}の値段は{value}円です")
	
except KeyError :
	print(f"{num}はメニューにありません")
	
except Exception as error :
	print(error)





