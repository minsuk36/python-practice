"""for  a in range(-5,6):
    b = abs(a)
    print(" "*b+"*"+"*"*2*(5-b))
"""

"""
    for a in range(0,4):
    for b in range(0,4):
        print("{0}".format(a+b),end=" ")
    print()
    

for a in range(1,7):
    for b in range(1,7):
        print("{0}  {1}".format(a,b))
    print()

sum = set()
for a in [-1,1]:
    for b in [-1,1]:
        for c in [-1,1]:
            d = 1024*2**(a+b+c)
            sum.add(d)

print(sum)            

for a in range(1,11):
    for b in range(1,11):
        for c in range(1,11):
            d = a**c+b**c
            
            
a = "나"
b = 5
while b>=1:
    b-=1
    print("{0}번의 커피".format(b))
    if b == 0:
        print("실패")


absent = [1,4]
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("여기까지.{0}는 죽어라".format(student))
        break
    print("{0},읽어라.".format(student))
"""