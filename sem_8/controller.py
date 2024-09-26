from menu import *
from random import choice

faculty = ["гриффиндор", "когтевран", "пуффендуй", "слизерин"]
dict = {}

def read_text():
    try:
        with open("student.txt", "r", encoding="utf-8") as f:
            student_list = f.readlines()
            student_list = list(map(lambda x: x.replace("\n", ""), student_list))
    except IOError:
        print("Упс, файл не читается :(")
    return student_list

def print_dict(list):
    global faculty, dict
    for i in range(len(read_text())):
        dict[read_text()[i]] = choice(faculty)
    return dict


def new_student(string: str):
    with open("student.txt", "a", encoding="utf-8") as f:
        f.write("\n")
        f.write(string)




    
