n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    marks = list(map(float, line))
    student_marks[name] = marks
query_name = input()
student_marks[name]=marks
marks=student_marks[query_name]
average=sum(marks)/len(marks)
print(f"{average:.2f}")