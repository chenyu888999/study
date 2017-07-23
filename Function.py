


def read_user():
    data = open("test1", encoding="utf-8")
    a = data.read()
    print(a)

    userinfo = a.split("#")

    abc = a.split("#")

    user_dic = {}
    for item in abc:
        item_list = item.split(":")
        user_dic[item_list[0]] = item_list[-1]
        # print(item_list[0])
    return user_dic


def write_lock():
