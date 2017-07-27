


list = [('iphone',5000),
        ('macbook',12000),
        ('vovi',3000),
        ('oppo',4000),
        ]
shopping_list = []

salary = (input('salary：'))
if salary.isdigit():
    salary = int(salary)
    print(salary)
    while True:
        for index,item in enumerate(list):
            print(index,item)
        choice = input("you are choice:")
        if choice.isdigit():
            choice = int(choice)
            if choice < len(list) and choice >= 0:
                pitem = list[choice]
                if pitem[1] < salary:
                    print("钱足够")
                    shopping_list.append(pitem[0])
                    salary -= pitem[1]
                    print("你的余额还有%s" %(salary))
                else:
                    print("钱不够了")
        elif choice == 'q':
            print("fsdfsdfsdf")
            print(shopping_list)
            exit()

else:
    print("请输入数字")





