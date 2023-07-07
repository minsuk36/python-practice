sentence = '나는 소년이다.'
print(sentence)
sentence2="파이썬은 쉬워요"
print(sentence2) 
sentence3 = """

나는 소년이고,
파이썬은 쉬워요

"""
print(sentence3)

minseok = "020306-3234567"
print("성별 : "+ minseok[7])
print("연 : "+ minseok[0:2])
print("월일 : "+ minseok[2:6])
print("뒷자리 : "+ minseok[7:])

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].islower())
print(python.replace("is","are"))
nb = python.index("n")
print(nb)
nb = python.index("n",nb +1)
print(nb)
print(python.find("java"))
print(python.count("n"))