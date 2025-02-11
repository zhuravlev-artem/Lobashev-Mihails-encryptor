
shifr = str(input())
keycode = str(input())
keycode1 = keycode
shifr1 = shifr
text = str()
kb = 0

while keycode != str():
    keycode = keycode[1:]
    kb += 1
if kb == 1:
    while shifr != str():
        keycode = keycode1
        ab1 = shifr[:kb]
        ab2 = shifr[:kb]
        o = ab2
        shifr = shifr[kb:]
        while ab1 != str():
            b1 = ab1[:1]
            ab1 = ab1[1:]
            for i in range(1, 1104):
                if chr(i) == b1:
                    b1 = i
                    if (b1 in range(32, 65)) and (len(list(o)) != 1):
                        ab2 = ab2 + shifr[:1]
                        ab1 = ab1 + shifr[:1]
                        shifr = shifr[1:]
                        print(ab2, 1)
            while ab2 != str():
                bv = 0
                b1 = ab2[:1]
                ab2 = ab2[1:]
                kb1 = keycode[:1]
                keycode = keycode[1:]
                for i in range(1, 1104):
                    if chr(i) == b1:
                        nb1 = i
                        b2 = i
                for n in range(1, 1104):
                    if chr(n) == kb1:
                        kb1 = n
                if nb1 in range(32, 65):
                    bv = 1
                if kb1 in range(1040, 1104) and bv == 0:
                    nb1 = nb1 + (kb1 - 1039)
                    if nb1 > 1103:
                        nb1 -= 64
                text =  text + chr(nb1)
else:
    while shifr != str():
        keycode = keycode1
        ab1 = shifr[:kb]
        ab2 = shifr[:kb]
        o = ab2
        shifr = shifr[kb:]
        while ab1 != str():
            b1 = ab1[:1]
            ab1 = ab1[1:]
            for i in range(1, 1104):
                if chr(i) == b1:
                    b1 = i
                    if (b1 in range(32, 65)):
                        ab2 = ab2 + shifr[:1]
                        ab1 = ab1 + shifr[:1]
                        shifr = shifr[1:]
            while ab2 != str():
                print(keycode, ab2)
                bv = 0
                b1 = ab2[:1]
                ab2 = ab2[1:]
                kb1 = keycode[:1]
                keycode = keycode[1:]
                for i in range(1, 1104):
                    if chr(i) == b1:
                        nb1 = i
                for n in range(1, 1104):
                    if chr(n) == kb1:
                        kb1 = n
                if nb1 in range(32, 65):
                    bv = 1
                    keycode = chr(kb1) + keycode
                if kb1 in range(1040, 1104) and bv == 0:
                    nb1 = nb1 + (kb1 - 1039)
                    if nb1 > 1103:
                        nb1 -= 64
                """if nb1 in range(32, 65):
                    nb1 = nb1 - (kb1 - 1039)  
                    keycode = chr(kb1) + keycode"""
                text =  text + chr(nb1)
print(text)
#АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ !?.,-абвгдеёжзийклмнопрстуфхцчшщъыьэюя
