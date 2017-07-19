data= open("test1",encoding="utf-8")
a = data.read()
print(a)

userinfo = a.split("#")

abc = a.split("#")

print(abc)


user_dic = {}
for item in abc:
    item_list = item.split(":")
    print(item_list)
    user_dic[item_list[0]] = item_list[-1]
    #print(item_list[0])
print(user_dic)

'''username = input("username:")
username = input("password:")'''

"fsdfsdfsdf"

