from Student import Student
from Ban import Ban


#Ban_list = [Ban(i) for i in range(1,6)]
Ban_list = []

with open('4_Algorithm.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        students = {}
        info = line.split(' ') # [ ['홍길동', '4', '1\n'], ..., ['이지연', '2', '4'] ]
        name = info[0]
        no = int(info[1])
        id = int(info[2][0])

        student = Student(id, name)

        #Ban_list[no - 1].student_list.append(student)
        if no not in Ban_list:
            Ban_list.append(Ban(no))
        for ban in Ban_list:
            if no == ban.no:
                ban.student_list.append(student)

# 1반, 2반, 3반, ... 순서대로 정렬 for __lt__, __eq__
Ban_list.sort()


for ban in Ban_list:
    print(ban)
    # 반 내에서 1번, 2번, 3번, ... 순서대로 정렬 for __lt__, __eq__
    ban.student_list.sort()
    for student in ban.student_list:
        print(student)
    print("\n")