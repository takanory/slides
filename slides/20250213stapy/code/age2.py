age = input("何歳ですか？")
try:
    if int(age) >= 20:
        print("お酒が飲める年齢です")
    else:
        print("お酒は飲めません")
except ValueError:
    print("数値を入力してください")
