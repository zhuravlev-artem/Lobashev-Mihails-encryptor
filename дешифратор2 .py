from math import*

shifr = str(input())
shifr1 = shifr
p = 1
x = 1
keycode = str()

while p != 0:
    flag3 = False
    shifr = shifr1
    x += 1
    kb = ceil(log(x, 65))
    if x == 1:
        kb = 1
    text = str()
    text2 = str()
    while shifr != str():
        ab1 = shifr[:kb]
        ab2 = shifr[:kb]
        shifr = shifr[kb:]
        circle = 0
        kbtexta = str()
        kbtexta2 = str()
        while ab1 != str():
            b1 = ab1[:1]
            ab1 = ab1[1:]
            for i in range(1, 1104):
                if chr(i) == b1:
                    nb1 = i
                    if nb1 in range (32, 65):
                        abx = shifr[:1]
                        shifr = shifr[1:]
                        ab1 = ab1 + abx
                        ab2 = ab2 + abx
                        ab3 = ab2
        while ab2 != str():
            nb3 = str(" ")
            b1 = ab2[:1]
            ab2 = ab2[1:]
            for i in range(1, 1104):
                if chr(i) == b1:
                    nb1 = i
            if nb1 in range(1040, 1104):
                if circle == 0:
                    nb1 = nb1 - x  # х-на сколько сместить букву( сколько кругов
                else:
                    nb1 = nb1 - (x // circle)
                while nb1 not in range(1040, 1104):
                    nb1 = nb1 + 64
                if nb1 in range(1040, 1104) or chr(nb1) == chr(32):
                    nb3 = chr(nb1)
                circle += 65
            kbtexta = kbtexta + chr(nb1)
            kbtexta2 = kbtexta2 + nb3
        text = text + kbtexta
        text2 = text2 + kbtexta2
        #print(shifr,":", nb1, text)
    #print(text,text2,x)
    listtext = text2.split()
    in1 = len(listtext)
    print(listtext, text)
    if in1 > 4:
        in1 = 4
    for m in range(0, in1):
        a = listtext[m]
        if flag3 == 1:
            break
        flag = 0
        Lx= open('russian.txt',encoding="utf-8")
        Lx.seek(0)
        for i in range(0, 2000000):
            b = (Lx.readline(30).strip())
            if a == b:
                print(text)
                user = int(input())
                if user == 1:
                    p -= 1
                    flag = 1
            if b == str("ящуру"):
                flag = 2
            if flag == 2:
                flag3 = 0
                break
            if flag == 1:
                flag3 = 1
                break
ab1 = shifr1[:kb]
ab2 = text[:kb]
circle = 0
kbtexta = str()
while ab1 != str():
    b1 = ab1[:1]
    ab1 = ab1[1:]
    b2 = ab2[:1]
    ab2 = ab2[1:]
    for i in range(1, 1104):
        if chr(i) == b1:
            nb1 = i
    for i in range(1, 1104):
        if chr(i) == b2:
            nb2 = i
    keyn = nb1 - nb2 + 1039
    while keyn not in range(1040, 1104):
        keyn = keyn + 64
    keycode = keycode + chr(keyn)
print(text, keycode)
    #а а аа а а а  аа  аааа  аа  !
