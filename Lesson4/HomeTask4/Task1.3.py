# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
first_number = "2x^2+2x^3+4x+10"
second_number = "6x^3+4x^2+12x+9"
numbers_1 = first_number.split("+")
numbers_2 = second_number.split("+")
print(numbers_1)
print(numbers_2)
int_list_1 = []
int_list_2 = []
for i in range(1):
    for item in numbers_1:
        if "^" in item:
            s_1 = item.split("x^")
            temp1 = s_1[0]
            print(temp1)
            temp1 = int(temp1)
            ave = int(s_1[1])
            int_list_1.append((temp1, ave))
        else:
            if "x" in item:
                s_2 = item.split("x")
                temp1 = s_2[0]
                if temp1 == "":
                    temp1 = 1
                print(temp1)
                temp1 = int(temp1)
                ave = 1
                int_list_1.append((temp1, ave))
            else:
                temp1 = int(item)
                ave = 0
                print(temp1)
                int_list_1.append((temp1, ave))
    ##############################################################
    for item2 in numbers_2:
        if "^" in item2:
            s_2 = item2.split("x^")
            temp2 = s_2[0]
            print(temp2)
            temp2 = int(temp2)
            ave2 = int(s_2[1])
            int_list_2.append((temp2, ave2))
        else:
            if "x" in item2:
                s_2 = item2.split("x")
                temp2 = s_2[0]
                if temp2 == "":
                    temp2 = 1
                print(temp2)
                temp2 = int(temp2)
                ave2 = 1
                int_list_2.append((temp2, ave2))
            else:
                temp2 = int(item2)
                ave2 = 0
                print(temp2)
                int_list_2.append((temp2, ave2))

print(int_list_1)
print(int_list_2)
result = ""
for i in range(len(numbers_1)):
    for j in range(len(numbers_2)):
        if int_list_1[i][1] == int_list_2[j][1]:
            if int_list_1[i][1] > 1 and int_list_2[j][1] > 1:
                result += str(int_list_1[i][0] + int_list_2[j][0]) + "x^" + str(int_list_1[i][1]) + "+"

            elif int_list_1[i][1] == 0:
                result += str(int_list_1[i][0] + int_list_2[j][0])
            elif int_list_1[i][1] == 1:
                result += str(int_list_1[i][0] + int_list_2[j][0]) + "x+"
print(result)
