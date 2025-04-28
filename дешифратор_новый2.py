from codecs import*
import encodings
#import locale
#print(locale.getencoding())
encodings.cp1251
#cp1251
#locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')
from math import*
shifr = str(input())
x = 0
lkey = [x]
shifr1 = shifr
p = 1
keycode = str()
flagk = False
Lx= open('russian.txt',encoding="utf-8")
spisn = Lx.readlines()
lkj = []
print(chr(1040))

while lkey[0]  >=  65:
        if lkey[0] >= 65:
                lkey.insert(0, 0)
                lkey[0] = lkey[1] // 65
                lkey[1] = lkey[1] % 65 + 1
while p != 0:
        flagk = 0
        # ключ
        x += 1
        lkj = []
        lkey[-1] = lkey[-1] + 1
        lkey.reverse()
        for i in range(0, len(lkey)):
                if lkey[i] // 65 >= 1 and i != (len(lkey)-1) :
                        lkey[i+1] = lkey[i+1] + lkey[i] // 65
                        lkey[i] = lkey[i] % 65 + 1
        lkey.reverse()
        while lkey[0]  >=  65:
                if lkey[0] >= 65:
                        lkey.insert(0, 1)
                        lkey[1] = lkey[1] % 65 + 1
        #Переделка текста
        lshifr = list(shifr)
        kbkey = len(lkey)
        s = -1
        poz = 0
        while s != len(lshifr)-1:
                s += 1
                #print(s)
                if ord(lshifr[s]) >= 1040 and ord(lshifr[s]) <= 1104:
                        lshifr[s] =  (ord(lshifr[s]) - lkey[poz % kbkey])
                        if lshifr[s] < 1040:
                                lshifr[s] = lshifr[s] + 64
                        lshifr[s] = chr(lshifr[s])
                        poz += 1
        text = "".join(lshifr)
        for i in range(0, len(lkey)):
                lkj.append(chr(lkey[i] + 1039))
        # текст без знаков препинания
        text2 = list(text)
        spisdel = []
        for i in range(0, len(text2)):
                if (ord(text2[i]) < 1040 or ord(text2[i]) > 1104) and ord(text2[i]) != 32 :
                        spisdel.append(i)
        for i in range(0, len(spisdel)):
                text2[spisdel[i]] = "%"
        for i in range(0, len(spisdel)):
                text2.remove("%")
        text2 = "".join(text2)
        #print(lkey)
        print(text, "||", text2, "".join(lkj))
        #print("=======")
        #поиск совпадений со списком слов
        listtext = text2.split()
        in1 = len(listtext)
        #print(listtext, text)
        if in1 > 4:
                in1 = 4
        #разделение текста на слова
        for m in range(0, in1):
                flagpr = True
                spis = spisn
                if flagk == 1:
                        break
                a = listtext[m]
                f1 = list(a)
                spis2 = 1532613
                #проверка отдельных слов почти бинарным поиском
                while spis2 != 0:
                        if flagk == 1:
                                #print(text)
                                end = int(input())
                                if end == 1:
                                        p = 0
                                        break
                                else:
                                        flagk = 2
                                        p = 1
                        #print(len(spis), spis2)
                        slov2 = spis[spis2 // 2]
                        spis2 = spis2 // 2
                        #print(a, slov2)
                        f2 = list(slov2)
                        f2.remove('\n')
                        slov2 = "".join(f2)
                        if len(spis) <= 14 and flagpr == True:
                                flagpr = False
                                p1 = spisn.index(spis[0])
                                for iu in range(p1 - 11, p1 + 11):
                                        f3 = list(spisn[iu])
                                        #print(f3)
                                        if f3[-1] == '\n':
                                                f3.remove('\n')
                                        slov3 = "".join(f3)
                                        #print(a, slov3, list(slov3))
                                        if a == slov3:
                                                flagk = 1
                                                print("=")
                                                break
                        if a != slov2 and flagk == 0:
                                if len(f1)> len(f2):
                                        for ui in range(0, len(f1) - len(f2)):
                                                f2.append(' ')
                                if len(f2)> len(f1):
                                        for ui in range(0, len(f2) - len(f1)):
                                                f1.append(" ")
                                fk = 0
                                for w in range(len(f1)):
                                        if fk == 1:
                                                break
                                        #print(ord(f1[w]), ord(f2[w]), f1, f2)
                                        if ord(f1[w]) > ord(f2[w]):
                                                spis = spis[spis2:]
                                                fk = 1
                                                #print(">")
                                        if ord(f1[w]) < ord(f2[w]):
                                                spis = spis[:spis2]
                                                fk = 1
                                                #print("<")
                                        #print(len(spis),spis2, x)
                        if a == slov2 and flagk == 0 :
                                flagk = 1
                                print("=")
                                p = 0

print("Текст:", text, "Ключ:", "".join(lkj))
    #а а аа а а а  аа  аааа  аа  !"""
