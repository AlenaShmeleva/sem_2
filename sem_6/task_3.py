# Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые
# буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы. 

def names(*names_list):
    final_list = {}
    for i in names_list:
        key = i[0].capitalize()
        if key not in final_list:
            final_list[key] = []
        final_list[key].append(i)
    return final_list

names_list = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]
print(names(names_list))