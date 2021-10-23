text = str(input("Ваш текст"))
variable =input("Виберіть (a або b): ")
if variable =="a" :
    Split = text.split()
    e = ""
    for i in sorted(Split):
        e = e + " " + i
        print(e)
        d = {}
        for char in set(text):
            d[char] = text.count(char)
            print(d)
elif variable == "b" :
     print(sorted(variable))
else:
    print("Неправильий ввід")


