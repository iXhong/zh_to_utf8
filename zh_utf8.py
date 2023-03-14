def zh_utf8(zh_name):

    zh_encode = list(str(zh_name.encode('utf-8')))
    del zh_encode[0:2]
    del zh_encode[-1]

    return zh_encode

def odd_list(num):
    #generate n odd numbers from 1
    n = 0
    odd_num = 0
    odd_list = []

    while len(odd_list) < num:
        odd_num = 2*n+1
        n  = n + 1
        odd_list.append(odd_num)

    return odd_list

# print(zh_utf8("一拳超人"))
print(odd_list(4))
