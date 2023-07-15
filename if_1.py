'''
weather = "미세먼지"
if weather == "비":
    print("우산챙겨")
elif weather == "미세먼지":
    print("챙겨라 마스크")
else:
    print("가라")
'''
temp = int(input("기온은 어때요?"))
if 30<= temp:
    print("너무 더워요. 나가지마라")
elif 10 <= temp and temp < 30:
    print("괜찮다.")
    