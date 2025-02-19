n = int(input())
stud = list(map(int, input().split()))
stud = sorted(stud)

min_stu = stud[0:n]
max_stu = sorted(stud[n:len(stud)], reverse=True)

result = [min_stu[i] + max_stu[i] for i in range(n)]
print(min(result))

    