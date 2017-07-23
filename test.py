import sys

data= open("test1",encoding="utf-8")
a = data.read()
print(a)

#userinfo = a.split("#")

abc = a.split("#")
user_dic = {}
for item in abc:
    item_list = item.split(":")
    user_dic[item_list[0]] = item_list[-1]
    #print(item_list[0])
print(user_dic)


data1= open("user_lock",'r+',encoding="utf-8")
b = data1.read()
lock =[]
lock.append(b)



count = 0
while True:
    username = input("username:")
    if username in user_dic:
        if username in lock:
            print(lock)
            print("用户名：%s已被锁定，不能使用" % username)
            sys.exit()
        else:
            while count < 3:
                password = input("password:")
                if password == user_dic[username]:
                    print("登录成功，欢迎%s" % username)
                    sys.exit()
                else:
                    count += 1
                    if count == 3:
                        print("被锁定，请联系管理员")
                        data1.write(username)
                        sys.exit()
                    else:
                        print("密码错误，请联系输入，还有%s机会" % (3 - count))
                        break
    else:
        print("用户名不存在")






