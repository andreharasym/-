while True:
    x = input("enter a or b : ")
    a = input("Ведіть бажане слово або речення ")
    if x == "a":
        l = []
        s = ' '.join(a)
        for i in s:
            if i not in l and i.isalpha():
                print(i + ': ' + str(s.count(i)))
                l.append(i)
    elif x == "b":
        y = a.replace('.', ' ').replace(',', ' ').replace('!', ' ').replace('?', ' ').replace('-', ' ').replace(':',' ')
        words = (list(set(y.split())))
        print(*[word for word in words if len(word) > 3])
    else:
        print("error")


