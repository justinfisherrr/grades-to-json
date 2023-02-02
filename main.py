from pathlib import Path
import json
input_dir = Path.cwd()
gradesPaths = list(input_dir.rglob("grade.txt"))
grades = []

for path in gradesPaths:
    txt = open(path)
    name = txt.readline();
    grade = txt.readline();
    note = ""
    for line in txt:
        note += line
    evaluation = {
        "name" : name,
        "grade": grade,
        "note" : note
    }
    grades.append(evaluation)

json_grades = json.dumps(grades, indent=4)
with open("grades.json", "w") as outfile:
    outfile.write(json_grades)


