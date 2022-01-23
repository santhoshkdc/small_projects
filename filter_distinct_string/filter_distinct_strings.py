import json
filename_1 = "C:/Users/FR2006TU/OneDrive/Google Data Analytics/course_1.txt"
filename_2 = "C:/Users/FR2006TU/OneDrive/Google Data Analytics/course_2.txt"
new_file = "course_2.txt"
with open(filename_1,"r+") as f1:
    f_obj1 = f1.read()
    list_1 = f_obj1.split("\n")
    for index, i in enumerate(list_1):
        i = i.rstrip()
        if len(i) <= 1:
            del(list_1[index])
with open(filename_2,'r+') as f2:
    f_obj2 = f2.read()
    with open("dummy.json", 'w+') as dummy_json:
        json.dump(f_obj2,dummy_json)

    with open('dummy.json') as dummy_json:
        new = json.load(dummy_json)
    list_2 = new.split("\n")
print(type(list_1[1]))
print(list_1)

for index in range(len(list_2)):
    if str(list_2[index][-1]) != " ":
        list_2[index][-1].replace(" ", "")
    else:
        pass
    if len(i) <= 1:
        del (list_2[index])
print(list_2)

list_3 = []
for elements_b in list_2:
    if elements_b not in list_1:
        list_3.append(elements_b)

list_3 = "\n".join(list_3)
"""with open(f"edited_{new_file}.txt", "w+") as edited_file:
    try:
        edited_file.writelines(list_3)
        print("Successful!")
    except:
        print("Error!")
"""
    #print(list_2)
print(list_1)
print(list_2)