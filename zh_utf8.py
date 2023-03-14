def zh_utf8(zh_name):
    zh_encode = list(str(zh_name.encode('utf-8')))
    del zh_encode[0:2]
    del zh_encode[-1]

    return zh_encode

print(zh_utf8("一拳超人"))
