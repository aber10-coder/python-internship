n=0
n=int(input('Enter the number of students: '))
students=[]
avg=0
sub_count=5
for i in range(0,n):
    marks=[]
    print(f'marks of student {i+1}')
    for j in range(0,5):
        mark=int(input(f"Enter mark for subject {j+1}:"))
        marks.append(mark)
    students.append(marks)
print(students)
for item in students:
    total=0
    for maks in item:
        total+=maks
    avg=total/5
    var=1
    print(f"student {var}")
    var=var+1
    if avg>=90:
        print("A")  
    elif avg>=80 and avg<90:
        print("B")
    elif avg>=70 and avg<80:
        print("C")
    elif avg>=60 and avg<70:
        print("D")
    else:
        print('F')
        
            


