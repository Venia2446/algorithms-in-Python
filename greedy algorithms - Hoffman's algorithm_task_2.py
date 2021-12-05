a = [int(i) for i in input().split()]
b = [[q for q in input().split(': ')] for z in range(a[0])]
c = input()
new_list = str()
dict_all = {}
answer_list = str()
for item_1 in b:
    if item_1[1] not in dict_all:
        dict_all[item_1[1]] = item_1[0]
    else:
        None
find_code = str()
for item_2 in c:
    find_code+=item_2
    if find_code in dict_all:
        answer_list+=dict_all[find_code]
        find_code=str()
print(answer_list)

