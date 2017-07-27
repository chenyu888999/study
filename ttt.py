

def ee(name):
    aa = open("D:\study\info", "r", encoding="utf-8")

    tt = aa.read()

    abc = tt.split("\n\n")
    print(abc)
    hh = {}
    for i in abc:
        qqq = i.split(" ")
        # print(qqq)
        hh[qqq[0]] = qqq[-1]
    print(hh)
    name = input(":")
    if name in hh:
        return print(hh[name])




gg = ee("Alex")
print(gg)







