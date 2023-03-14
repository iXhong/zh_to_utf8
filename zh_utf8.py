'''
This is python script to convert the Chinese to
a utf-8 like encoded style which used in Browser.
change the parameter to use the function
'''

def zh_to_utf8(zh_name):

    zh_encode = list(str(zh_name.encode('utf-8')))
    #convert to standard UTF-8 encode`
    del zh_encode[0:2]
    del zh_encode[-1]
    #delete the first two and last one char

    i = 0
    for char in zh_encode:
        if char == '\\':
            del  zh_encode[i]
        i = i + 1
    #delete "\\"

    n = 0
    for char in zh_encode:
        if char == 'x':
            zh_encode[n] = '%'
        n = n + 1
    #replace "x" with '%

    zh_utf8 = ''.join(zh_encode)
    #convert a list to string without separator ","

    return zh_utf8.title()

zh_name = input("请输入欲转换的中文名称：")

print(zh_to_utf8(zh_name))
