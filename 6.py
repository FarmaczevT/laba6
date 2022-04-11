def paste(a:list, b):
    if len(a) % 2 == 0:
        a.insert(len(a)//2, b)
    else:
        a.insert((len(a)//2)+1, b)
    return a

def func(a:list, b:int, c):
    try:
        if b != 0 and len(a) > b:
            a.insert(b - 1,c)
            return a
        else:
            return "operation is not possible"

    except:
        return "operation is not possible"

print(paste(["1", "2", "3", "4", "5", "6"], "7"))

c = int(input("Куда вставить? ---> "))
print(func(["djdjdj","1243234","qwerty","asassdffdg"],c,"abcd"))





