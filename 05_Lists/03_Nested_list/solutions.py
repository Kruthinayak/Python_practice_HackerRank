n = int(input())
records = []
for i in range(n):
    name = input()
    grades = float(input())
    records.append([name, grades])
grades = []
for i in range(n):
    grades.append(records[i][1])
grades = set(grades)
lowest = min(grades)
grades.remove(lowest)
second_lowest = min(grades)
names = []
for i in range(n):
    if records[i][1] == second_lowest:
        names.append(records[i][0])
names.sort()
for name in names:
    print(name)