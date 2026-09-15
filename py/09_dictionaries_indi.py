# Exercise 1 🗂️ Make ONE Project Card
proj1 = {
    "lang": "en",
    "words": 2500,
    "rate": 0.05,
    "status": "pending"
}

print("Language:", proj1["lang"])
print("Cost: RM", proj1["words"]*proj1["rate"])

proj1["status"] = "done" # ✅ Change existing info
print("Updated Status: ", proj1["status"])

# Exercise 2 📋 Make Your Project List
proj2 = {
    "lang": "zh",
    "words": 3200,
    "rate": 0.06,
    "status": "done"
}
proj3 = {
    "lang": "ms",
    "words": 1800,
    "rate": 0.045,
    "status": "active"
}
proj4 = {
    "lang": "ja",
    "words": 4500,
    "rate": 0.08,
    "status": "pending"
}
all_projs = [proj2, proj3, proj4]

# Exercise 3 💰 Calculate Total Revenue
grand_total = 0

for p in all_projs:
    print("total rate in each lang is ", (p["rate"] * p["words"]))          # p[rate] * p[words] is ❌ WRONG!
    grand_total += (p["rate"] * p["words"])                                 # Python thinks rate and words are variable names — but they're NOT! They're LABELS inside your dictionary!

print("The grand total is: ", grand_total)

print("""-----------------------------------------
PDF exercise starts:""")

student_records = {
    "student1": {
        "code": "student_001",
        "name": "John",
        "age": 19,
        "major": "Computer Sci",
        "grades": [85,92,78]
    },
    
    "student2": {
        "code": "student_002",
        "name": "Sarah",
        "age": 20,
        "major": "Biology",
        "grades": [90,88,95]
    }
}


new_student = {
        "code": "student_003",
        "name": "Mike",
        "age": 18,
        "major": "Math",
        "grades": [82,79,91]
        }
student_records["student3"] = new_student

student_records["student1"]["age"] = 20

for s in student_records:
    info = student_records[s]
    print(info["code"],",", info["name"],",",info["major"] )
