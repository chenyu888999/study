select = ["查询员工工资","修改员工工资","增加新员工记录","退出"]
data = open("D:\study\info", "r+", encoding="utf-8")
user = data.read()
user = user.split("\n\n")
user_data = {}

for index,i in enumerate(select):
    print(index,i)
choice = input("您的选择是：")
if choice.isdigit():
    choice = int(choice)
    #if choice < len(select) and choice >= 0:
    if choice == 0:
        #pitem = select[choice]
        #print(pitem)
        select1 = input("请输入要查询的员工姓名（例如：Alex）")

        for i in user:
            wages = i.split(" ")
            user_data[wages[0]] = wages[-1]
        if select1 in user_data:
            print("%s的薪水是:" % select1,user_data[select1] )

    if choice == 1:
        update = input("请输入要修改的员工姓名和工资，用空格分隔（例如：Alex 10）")
