def func(a:list, b:int, c):
    try:
        if b != 0 and len(a) > b:
            a.insert(b - 1,c)
            return a
        else:
            return "operation is not possible"

    except:
        return "operation is not possible"


c = int(input("Куда вставить? ---> "))
print(func(["djdjdj","1243234","qwerty","asassdffdg"],c,"abcd"))