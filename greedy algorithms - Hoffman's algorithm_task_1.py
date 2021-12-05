from operator import itemgetter
import copy
input_data = input()
dict_all = {}
sorted_list = []
bi_list = str()
for data in input_data:
    if data not in dict_all:
        dict_all[data] = 1
    else:
        dict_all[data] = dict_all[data]+1
for key,items in dict_all.items():
    sorted_list += [[key,items]]
sorted_list = sorted(sorted_list, key = itemgetter(1))
answer_list = copy.deepcopy(sorted_list)
if len(answer_list) == 1:
    print(1,answer_list[0][1])
    print(answer_list[0][0]+':',0)
    print('0'*answer_list[0][1])
else:
    while len(sorted_list)!=2:
        NEW_LIST = [sorted_list.pop(0)]+[sorted_list.pop(0)]
        NEW_LIST = [NEW_LIST[0][0]+NEW_LIST[1][0],NEW_LIST[0][1]+NEW_LIST[1][1]]
        sorted_list += [NEW_LIST]
        sorted_list = sorted(sorted_list, key=itemgetter(1))
        answer_list += [NEW_LIST]
    answer_list = sorted(answer_list, key = itemgetter(1))
    for i,x in enumerate(answer_list):
        if i == 0:
            x[1] = 0
        elif i % 2 == 0:
            x[1] = 0
        else:
            x[1] = 1
    for values in dict_all:
        dict_all[values] = str()
    for key in dict_all.keys():
        for item2 in answer_list[::-1]:
            if key in item2[0]:
                dict_all[key]+=str(item2[1])
    for p in input_data:
        bi_list+=dict_all[p]
    print(len(dict_all.keys()),len(bi_list))
    for ite,ke in dict_all.items():
        print(ite+':', ke)
    print(bi_list)



