#집합 (set)
#중복안됨,순서없음
my_set = {5,2,3,3,4}
print(my_set)

java = {"유재석","김태호","양세형"}
python = {"유재석","박명수"}

#교집합 (java와 python 을 모두 할 수있는 개발자)
print(java&python)\
#오로지 set와 set의 교집합만이 값이 출력된다
#합집합
print(java|python)
#차집합 (java - python)
print(java - python)
#python 에 추가
python.add("김태호")
print(python)
#제거
python.remove("김태호")

#자료구조의 변경
#커피숍

menu = {"커피", "우유", "주스"}
print(menu,type(menu))
#자료구조 변경
menu = list(menu)
print(menu,type(menu))