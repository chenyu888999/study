import sys
select = ["查询员工工资","修改员工工资","增加新员工记录","退出"]
with open("D:\study\study\info", "r", encoding="utf-8") as data,open("D:\study\study\info_bak.txt", "w") as data2,open("D:\study\study\info", "a", encoding="utf-8")as data3:
    user = data.read()
    user = user.split("\n")
    user_data = {}

    for i in user:
        wages = i.split(" ")
        user_data[wages[0]] = wages[-1]
        #print(user_data)


    while True:
        for index, i in enumerate(select):
            print(index, i)
        choice = input("您的选择是：")
        if choice.isdigit():
            choice = int(choice)
            # if choice < len(select) and choice >= 0:
            if choice == 1:
                # pitem = select[choice]
                # print(pitem)
                select1 = input("请输入要查询的员工姓名（例如：Alex）")
                if select1 in user_data:
                    print("%s的薪水是:" % select1, user_data[select1])

            if choice == 2:
                update = input("请输入要修改的员工姓名和工资，用空格分隔（例如：Alex 10）")
                a = update.split(" ")
                for i in user_data:
                    # print(i)
                    if i == a[0]:
                        user_data[a[0]] = a[1]
                        for key, value in user_data.items():
                            print(key, value)
                            data2.write("%s" % key + " " + "%s\n" % value)
                            data2.flush()

            if choice == 3:
                add = input("请输入要增加的员工姓名和工资，共空格分割（例如：Eric 100000）")
                a = add.split(" ")
                data3.write("%s" % a[0] + " " + "%s\n" % a[1])
                data3.flush()


            if choice == 4:
                sys.exit()








