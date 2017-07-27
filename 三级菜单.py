locate = {
    "湖北":{
        "武汉":{
            "汉口":["中百仓储","沃尔玛"],
            "武昌":["小辉超市","万科城"]

        },
        "恩施":{
            "建始":["湖北民院","人民医院"],
            "宜昌":["巴东河","三峡"]
        }
    },
    "北京":{
        "朝阳":{
            "望京":["奔驰","陌陌"],
            "国贸":["HP","CICC"]
        }
    }
}

flag = False

while not flag:
    for i in locate:
        print(i)
    choice = input("请选择进入1：")
    if choice in locate:
        while not flag:
            for i2 in locate[choice]:
                print("\t",i2)

            choice2 = input("请选择进入2：")
            if choice2 in locate[choice]:
                while not flag:
                    for i3 in locate[choice][choice2]:
                        print("\t",i3)

                    choice3 = input("请选择进入3：")
                    if choice3 in locate[choice][choice2]:
                        for i4 in locate[choice][choice2][choice3]:
                            print("\t",i4)

                        choice4 = input("最后一层，请按b返回：")
                        if choice4 == "b":
                            pass
                        elif choice4 == "q":
                            flag = True

                    if choice3 == "b":
                        break
                    elif choice3 == "q":
                        flag = True
            if choice2 =="b":
                break
            elif choice2 == "q":
                flag = True
    elif choice == "q":
        flag = True





