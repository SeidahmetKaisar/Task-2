s = 0
while True:
    x = int(input("Ведите первое число:"))
    operator = input("Ведите значение")
    a = int (input("Ведите второе число"))
    s += 1
    if s==3:
        print("У вас лимит приобритите Premyum Vers")
        break
    elif operator == "+":
        print("Еки саннын косндысы",x+a)
    elif operator == "-":
        print("Сандардын азайтылуы",x-a)
    elif operator == "*" :
        print("Сандар көбейтіндісі",x*a)
    elif operator == "/":
        print("Еки саннын болиндиси",x/a)