import json
stud=[
    {"id":1,
     "name":"Abdu"
     },
     {
         "id":2,
         "name":"aber"
     },
     {
         "id":3,
         "name":"Ayas"
     },
     {
        "id":4,
         "name":"Dev"
     },
     {
         "id":5,
         "name":"fadhi"
     }
]
with open("students.json","w") as f:
    json.dump(stud,f,indent=2)

print("Verification-   ")
with open("students.json","r") as f:
    print(f.read())

with open("students.json","r") as f:
    data=json.load(f)

for item in data:
    print(f"Name: {item["name"]}")
    print(f"ID: {item["id"]}")



