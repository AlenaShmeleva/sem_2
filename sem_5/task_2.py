# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах. 

def recode (text = 'text_word.txt'):
    count = 1
    with open(text) as i_f:
        string = i_f.readline()
        with open('text_code_words.txt' , 'a', encoding="utf-8") as f_f:
            for i in range(len(string)-1):
                if string[i] == string[i + 1]:
                    count +=1
                else:
                    f_f.write(str(count))
                    f_f.write(string[i])
                    count = 1
    print("Сжатый файл готов!")

def decode(text = 'text_code_words.txt'):
    with open(text) as d_f:
        string = d_f.readline()
        dec_text = ''
        count = ''
    for i in string:
        if i.isdigit():
            count += i
        else :
            if not count:
                dec_text += i
            else: 
                dec_text += int(count) * i
                count = ''
    return dec_text



print(recode(input("Введите имя файла для сжатия: ")))
print(decode(input("Введите имя файла для восстановления: ")))