def tuplas():
    tup = [('Chile', 67000), ('Brasil', 860000), ('Argentina', 120000), ('Mexico', 230000)]
    dic = {}
    for x in tup:
        dic[x[0]] = x[1]
    print(sorted(dic, key=lambda i: int(dic[i]), reverse=True))
