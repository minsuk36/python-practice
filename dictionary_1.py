cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(6))
#get을 사용할시 자료값이 없더라도 오류가 뜨지 않는다.
print(cabinet.get(6,"사용가능"))
#값이 없을시 "사용가능"값 추가

print(3 in cabinet) # True
#string으로도 가능
studio = {"a-1":"민","b-2":"석"}
print(studio)
print(studio["a-1"])
print(studio["b-2"])
#값 없애기
del studio["a-1"]
print(studio)
#key 값들만 출력
print(studio.keys())
#key , value 쌍으로 출ㄹ력
print(cabinet.items())