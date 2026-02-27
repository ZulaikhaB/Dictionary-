# Dictionary of students (id-> details)
students_data = {
    "id1": {"name":"Sara", "class": "v", "subject_intergration": "english, math, science"},
    "id2": {"name":"David", "class": "v", "subject_intergration": "english, math, science"},
    "id3": {"name":"Sara", "class": "v", "subject_intergration": "english, math, science"},
    "id4": {"name":"Surya", "class": "v", "subject_intergration": "english, math, science"},
}

result = {}
seen = set()

for student_id, details in students_data.items():
    unique_key = (details["name"], details["class"],details["subject_intergration"])
    if unique_key not in seen:
        seen.add(unique_key)
        result[student_id] = details

# print output line by line 
for k, v in result.items():
    print(k, ":", v)