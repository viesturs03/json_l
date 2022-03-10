import json
file = open("students.json")
data = json.load(file)


student_ages = []


for age in data["Students"]:
    student_ages.append(int(age["Age"]))

average_age = sum(student_ages) / len(student_ages)

print(average_age)