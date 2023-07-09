subway = [0,20,30]
print(subway)

subway = ["유재석","조세호","박명수"]
print(subway)

#조세호씨가 몇번째 칸에 타고있는가?
print(subway.index("조세호"))

#하하씨가 다음정류장에서 다음칸에 탐
subway.append("하하")
print(subway)

#정형돈씨를 유재석/ 조세호 사이에 태워봄
subway.insert(1,"정형돈")
print(subway)

#지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)
#같은 이름의 사람이 몇명있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))
#오름차순 정령
numb = [2,1,4,5,3]
numb.sort()
print(numb)
#뒤집기
numb.reverse()
print(numb)
#모두지우기
numb.clear()
print(numb)
#배열합치기 
adde =["가",1,True]
numb.extend(adde)
print(numb)