def puh(poem):
    count_list=[]
    count =0
    vowels = "ауоыиэяюёе"
    for i in poem.split(" "):
        for j in i:
            if j in vowels:
                count +=1
        count_list.append(count)
        count=0
    return count_list

def control(list):
    if list.count(list[0]) == len(list):
        return "Парам пам-пам"
    else:
        return "Пам парам"

poem = input("введи стих: ")
print(control(puh(poem)))
# print(control(puh("пара-ра-рам рам-пам-папам па-ра-па-да")))