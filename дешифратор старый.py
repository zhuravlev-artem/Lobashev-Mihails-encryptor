from math import*

shifr = str(input())
shifr1 = shifr
p = 4225
x = 1
keycode = str()

while p != 0:
    shifr = shifr1
    x += 1
    kb = ceil(log(x, 65))
    if x == 1:
        kb = 1
    text = str()
    while shifr != str():
        ab1 = shifr[:kb]
        ab2 = shifr[:kb]
        shifr = shifr[kb:]
        circle = 0
        kbtexta = str()
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
                circle += 65
            kbtexta = kbtexta + chr(nb1)
        text = text + kbtexta
        #print(shifr,":", nb1, text)
    print(text,kb,x)
    p = p - 1
    
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
    print(nb1, nb2, keyn)
    keycode = keycode + chr(keyn)
print(text, keycode)
    #а а аа а а а  аа  аааа  аа  !
