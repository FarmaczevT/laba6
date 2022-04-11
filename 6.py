def paste(a:list, b):
    if len(a) % 2 == 0:
        a.insert(len(a)//2, b)
    else:
        a.insert((len(a)//2)+1, b)
    return a

print(paste(["1", "2", "3", "4", "5", "6"], "7"))
