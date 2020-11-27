#3FS1-75 福田湧基
#ログイン処理と表示

idlist =[]
while True:
	print("()の数字を入力してください（qで終了)")
	do = input("登録(1),ログイン(2) : ")
	print(" ")
	if do == "q" :
		print("finish")
		break
		
	try :
		if do == "1":

			print("登録処理を行います")
			typeid=input("学籍番号を入力してください :")
			print(" ")
			idlist.append(typeid)
			print("登録が完了しました")

		elif do == "2":
			print("ログイン処理を行います")
			loginid=input("登録した学籍番号を入力してください :")
			judege = str(loginid) in idlist
			print(" ")
			
			if judege == True :
				print("ログインが成功しました。")
				print("現在ログインしている人は以下の通りです")
				for idname in idlist:
					print("No. ",idname)
				print(" ")
				
			else :
				print("登録した番号が見当たりません")
				print(" ")
				
	except ValueError:
		print("数値を入力してください")