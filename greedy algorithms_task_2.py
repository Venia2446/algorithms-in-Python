from operator import itemgetter

def find_count(price,v):
    return price/v


def BAG_COUNT(list):
    global PRISE,BAG
    for params in list:
        if params[1] == BAG:
            PRISE = PRISE + (params[1] * params[0])
            return f"{PRISE:.3f}"
        if params[1] > BAG:
            PRISE += params[0] * BAG
            return f"{PRISE:.3f}"
        if params[1] < BAG and len(list) !=1:
            PRISE += params[1]*params[0]
            BAG = BAG - params[1]
        else:
            PRISE += params[1] * params[0]
            return f"{PRISE:.3f}"






N,BAG = input().split()
N = int(N)
BAG = float(BAG)
G_LIST = [[float(i) for i in input().split() ] for n in range(N)]

G_LIST2 = []
for parameters in G_LIST:
    G_LIST2  += [[find_count(parameters[0],parameters[1]),parameters[1]]]
G_LIST2 = sorted(G_LIST2,key = itemgetter(0),reverse= True)

PRISE = float()



print(BAG_COUNT(G_LIST2))