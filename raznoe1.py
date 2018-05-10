'''
# Числа, кратные 3 или 5
nSumma = 0

for number in range(1000):
    if number % 3 == 0 or number % 5 == 0:
        nSumma = nSumma + number
print(nSumma)

nSumma = 2
n1 = 1
n2 = 2
n3 = 0

while n3 <= 4000000:
    n3 = n1 + n2
    if n3 % 2 == 0:
        nSumma = nSumma + n3
    n1 = n2
    n2 = n3
print(nSumma)
# Четные числа Фибоначчи



# Наибольший простой делитель

nChislo = 600851475143

def prostoe (n):
    n1 = 0
    if n % 2 != 0 and n % 5 != 0 and n % 7 == 0 and n % 11 == 0 and n % 13 == 0 and n % 17 == 0:
        n1 = n//2+1
        while n1 > 2:
            if n%n1!=0:
                n1 = prostoe(n1)
            else:
                n1 = n1 - 1
    return(n1)


for number in range(nChislo // 2 +1, 0, -1):
    if prostoe(number) > 0:
        print(prostoe)


# Наибольший простой делитель2
lSpisok = [2]
#nChislo = 600851475143
nChislo = 600851475143
nChislo1 = nChislo

def addSimple(n):
    flag1 = 0
    n1 = n +1
    while flag1 ==0:
        for number in range(len(lSpisok)):
            if n1%lSpisok[number] == 0:
                n1 = n1+1
                break
            else:
                if number == len(lSpisok)-1:
                    lSpisok.append(n1)
                    return

nProstoe = 1
while nProstoe < nChislo/2:
    addSimple(nProstoe)
    nProstoe = lSpisok[len(lSpisok)-1]

flag2 = 0
nItog = 0
sdvig = 0
while flag2 == 0:
    for number in range(len(lSpisok)):
        if nChislo1/(round(nChislo1//lSpisok[sdvig] + 0.5)) == 1:
            nItog = lSpisok[sdvig]
            print(str(nChislo1) +"/" + str(nItog) + " = " + str(nChislo1/nItog))
            flag2 = 1
        else:
            if number == len(lSpisok)-1:
                addSimple(lSpisok[number])
                sdvig = sdvig + 1

# 5 Наименьшее кратное 232792560

flag = 0
nItog = 2

while flag == 0:
    flag = 1
    for i in range(20):
        if nItog % (i+1) !=0:
            flag = 0
            break
    nItog = nItog + 1
print(nItog-1)



# 6 Разность между суммой квадратов и квадратом суммы 25164150

nItog = 0

nSumma1 = 0
nSumma2 = 0

for n in range(101):
    nSumma1 = nSumma1 + n*n
    nSumma2 = nSumma2 + n
nSumma2 = nSumma2 * nSumma2
nItog = nSumma2 - nSumma1

print(nItog)


# 7 10001-ое простое число

def addSimple(n):
    flag1 = 0
    n1 = n +1
    while flag1 ==0:
        for number in range(len(lSpisok)):
            if n1%lSpisok[number] == 0:
                n1 = n1+1
                break
            else:
                if number == len(lSpisok)-1:
                    lSpisok.append(n1)
                    return

nProstoe = 1
lSpisok = [2]
for n in range(10001):
    addSimple(nProstoe)

print(lSpisok[9999])
print(lSpisok[10000])
print(lSpisok[10001])


# 7 v2 Решето 10001-ое простое число 104743
lSpisok = [2]

nChislo = 600851475143
nChislo = nChislo//2
flag1 = 1
for n in range(3, nChislo, 1):
    for n1 in range(len(lSpisok)-1):
        if (n)%lSpisok[n1] == 0:
            flag1 = 0
    if flag1 == 1:
        lSpisok.append(n)
    flag1 = 1
print(lSpisok[10000])


# Наибольшее произведение в последовательности (13 последовательных цифр)
#9 × 9 × 8 × 9 = 5832

#73167176531330624919225119674426574742355349194934
#96983520312774506326239578318016984801869478851843
#85861560789112949495459501737958331952853208805511
#12540698747158523863050715693290963295227443043557
#66896648950445244523161731856403098711121722383113
#62229893423380308135336276614282806444486645238749
#30358907296290491560440772390713810515859307960866
#70172427121883998797908792274921901699720888093776
#65727333001053367881220235421809751254540594752243
#52584907711670556013604839586446706324415722155397
#53697817977846174064955149290862569321978468622482
#83972241375657056057490261407972968652414535100474
#82166370484403199890008895243450658541227588666881
#16427171479924442928230863465674813919123162824586
#17866458359124566529476545682848912883142607690042
#24219022671055626321111109370544217506941658960408
#07198403850962455444362981230987879927244284909188
#84580156166097919133875499200524063689912560717606
#05886116467109405077541002256983155200055935729725
#71636269561882670428252483600823257530420752963450

cString = ""
cString = cString +"73167176531330624919225119674426574742355349194934"
cString = cString +"96983520312774506326239578318016984801869478851843"
cString = cString +"85861560789112949495459501737958331952853208805511"
cString = cString +"12540698747158523863050715693290963295227443043557"
cString = cString +"66896648950445244523161731856403098711121722383113"
cString = cString +"62229893423380308135336276614282806444486645238749"
cString = cString +"30358907296290491560440772390713810515859307960866"
cString = cString +"70172427121883998797908792274921901699720888093776"
cString = cString +"65727333001053367881220235421809751254540594752243"
cString = cString +"52584907711670556013604839586446706324415722155397"
cString = cString +"53697817977846174064955149290862569321978468622482"
cString = cString +"83972241375657056057490261407972968652414535100474"
cString = cString +"82166370484403199890008895243450658541227588666881"
cString = cString +"16427171479924442928230863465674813919123162824586"
cString = cString +"17866458359124566529476545682848912883142607690042"
cString = cString +"24219022671055626321111109370544217506941658960408"
cString = cString +"07198403850962455444362981230987879927244284909188"
cString = cString +"84580156166097919133875499200524063689912560717606"
cString = cString +"05886116467109405077541002256983155200055935729725"
cString = cString +"71636269561882670428252483600823257530420752963450"

print (str(len(cString)))

nMax = 0
nChislo = 0
for n in range(1,1000-12):
    nChislo = int(cString[0+n]) * int(cString[1+n]) * int(cString[2+n]) * int(cString[3+n]) * int(cString[4+n]) * int(cString[5+n]) * int(cString[6+n]) * int(cString[7+n]) * int(cString[8+n]) * int(cString[9+n]) * int(cString[10+n]) * int(cString[11+n]) * int(cString[12+n])
    if nChislo > nMax:
        nMax = nChislo

print(str(nMax))


# 7 v2 Решето 10001-ое простое число 104743
lSpisok = [3]

nChislo = 600851475143
nChislo1 = nChislo//69 +1
flag1 = 1
for n in range(3, nChislo1, 2):
    for n1 in range(len(lSpisok)-1):
        if (n)%lSpisok[n1] == 0:
            flag1 = 0
    if flag1 == 1:
        lSpisok.append(n)
    flag1 = 1
print(lSpisok[10000])



def isPrime(nTest, nChislo):

   d = 3
   while d * d <= n and n % d != 0:
       d += 2
   return d * d > n

nChislo1 = 600851475143
nChislo2 = 8462696833

while nChislo2 > 7000000000:
    if nChislo2 % 3 == 0 or nChislo2 % 5 == 0 or nChislo2 % 7 == 0 or nChislo2 % 11 == 0:
        nChislo2 = nChislo2 - 2
    else:
        if nChislo2


def isPrime(n):

   d = 3
   while d * d <= n and n % d != 0:
       d += 2
   return d * d > n

nChislo2 = 600851475143
nChislo = 8462696833
for n in range(71, nChislo, 2):
    if nChislo2%n == 0:
        print(str(n)+ " " + str(nChislo2/n) + " " +str(isPrime(nChislo2%n)))

# 9 Особая тройка Пифагора 31875000
from math import sqrt
nA = 0
nB = 0
nC = 0
for nC in range(1000,2,-1):
    nSummaKv = nC**2
    nA = 2
    for nA in range(2,nC-nA):
        nBkv = nSummaKv - nA**2
        nB = sqrt(nBkv)
        if nB == nB//1: #Корень В - целое число
            if nA + nB + nC == 1000:
                if nA**2 + nB**2 == nC**2:
                    print(str(nA) + " " + str(nB) + " " + str(nC))
                    exit()


# 10 Сложение простых чисел: Найдите сумму всех простых чисел меньше двух миллионов
lSpisok = [2]

nChislo = 600851475143
nChislo1 = nChislo//69 +1
flag1 = 1
nSumma = 2

for n in range(3, nChislo1, 2):
    for n1 in range(len(lSpisok)-1):
        if (n)%lSpisok[n1] == 0:
            flag1 = 0
    if flag1 == 1:
        lSpisok.append(n)
        if n < 2000000:
            nSumma = nSumma + n
    flag1 = 1
print(nSumma)



lSpisok = ["08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08"]
lSpisok.append("49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00")
lSpisok.append("81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65")
lSpisok.append("52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91")
lSpisok.append("22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80")
lSpisok.append("24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50")
lSpisok.append("32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70")
lSpisok.append("67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21")
lSpisok.append("24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72")
lSpisok.append("21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95")
lSpisok.append("78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92")
lSpisok.append("16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57")
lSpisok.append("86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58")
lSpisok.append("19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40")
lSpisok.append("04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66")
lSpisok.append("88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69")
lSpisok.append("04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36")
lSpisok.append("20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16")
lSpisok.append("20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54")
lSpisok.append("01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48")

n = 20
aMatrica = [[0] * n for i in range (len(lSpisok))]

n = 0
for nRow in range(len(lSpisok)):
    cStroka = lSpisok[nRow]
    for nCol in range(20):
        nCurPoz = nCol*3
        aMatrica[nRow][nCol] = int(cStroka[nCurPoz:(nCurPoz + 2)])

nMax = 0

for nRow in range(17):
    for nCol in range(17):
        n1 = aMatrica[nRow][nCol]
        n2 = aMatrica[nRow+1][nCol+1]
        n3 = aMatrica[nRow+2][nCol+2]
        n4 = aMatrica[nRow+3][nCol+3]
        nProizv = n1*n2*n3*n4
        #print (str(n1) + " * " + str(n2) + " * " + str(n3) + " * " + str(n4) + " = " + str(nProizv))
        if nProizv > nMax:
            nMax = nProizv

for nRow in range(17):
    for nCol in range(17,0,-1):
        n1 = aMatrica[nRow][nCol]
        n2 = aMatrica[nRow + 1][nCol - 1]
        n3 = aMatrica[nRow + 2][nCol - 2]
        n4 = aMatrica[nRow + 3][nCol - 3]
        nProizv = n1 * n2 * n3 * n4
        print(str(n1) + " * " + str(n2) + " * " + str(n3) + " * " + str(n4) + " = " + str(nProizv))
        if nProizv > nMax:
            nMax = nProizv

for nRow in range(20):
    for nCol in range(17):
        n1 = aMatrica[nRow][nCol]
        n2 = aMatrica[nRow][nCol + 1]
        n3 = aMatrica[nRow][nCol + 2]
        n4 = aMatrica[nRow][nCol + 3]
        nProizv = n1 * n2 * n3 * n4
        #print(str(n1) + " * " + str(n2) + " * " + str(n3) + " * " + str(n4) + " = " + str(nProizv))
        if nProizv > nMax:
            nMax = nProizv
for nRow in range(17):
    for nCol in range(20):
        n1 = aMatrica[nRow][nCol]
        n2 = aMatrica[nRow + 1][nCol]
        n3 = aMatrica[nRow + 2][nCol]
        n4 = aMatrica[nRow + 3][nCol]
        nProizv = n1 * n2 * n3 * n4
        #print(str(n1) + " * " + str(n2) + " * " + str(n3) + " * " + str(n4) + " = " + str(nProizv))
        if nProizv > nMax:
            nMax = nProizv
print(nMax)


flag = 0
n = 7700
nMax = 0
nSumma = 0
for nChislo in range(1, n+1):
    nSumma = nSumma + nChislo

while flag == 0:
    n = n+1
    nSumma = nSumma + n

#    for nChislo in range(1, n+1):
#        nSumma = nSumma + nChislo
    nKolvo = 1
    if nSumma%2 == 0:
        for nDelitel in range(2, nSumma//2+1):
            if nDelitel > 10000 and nKolvo < 200:
                break
            if nSumma % nDelitel == 0:
                nKolvo = nKolvo + 1
        if nKolvo > nMax:
            nMax = nKolvo
        if nKolvo >= 500:
            print("ИТОГ: " + str(nSumma) + " : " + str(nKolvo))
            nFlag = 1
            break
            #print(str(nSumma) + " : " + str(nKolvo))



import math

def isPrime(n):
    s = str(n)
    if n == 1 or n == 2 or n == 3 or n == 5 or n == 7 or n == 11 or n == 13 or n == 17 or n == 19:
        return (True)
    elif n == 4 or n == 6 or n == 8 or n == 9:
        return (False)
    elif n%2 == 0 or n%3 == 0 or n%5 == 0 or n%7 == 0 or n%11 ==0:
        return (False)
    elif s[-1] == 2 or s[-1] == 4 or s[-1] == 6 or s[-1] == 8 or s[-1] == 0:
        return (False)
    else:
        d = 3
        while d * d <= n and n % d != 0:
           d += 2
        if d * d > n:
            lItog = True
        else:
            lItog = False
        return(lItog)

def kol_del(nChislo):
    aProsto = [1]
    aSlozhno = []
    nMax = math.floor(math.sqrt(nChislo)) + 1
    if nChislo%2 ==0:
        nStep = 1
        nStart = 2
    else:
        nStep = 2
        nStart = 3

    for nCounter in range(nStart, nMax+1, nStep):
        if nChislo % nCounter == 0:
            nDelitel2 = nChislo/nCounter
            aSlozhno.append(nDelitel2)
            if nCounter not in (aSlozhno):
                if isPrime(nCounter):
                    flag = 0
                    for n3 in range(2, len(aProsto)-1):
                        if nCounter%n3 == 0:
                            flag = 1
                            break
                    if flag == 0:
                        aProsto.append(nCounter)
                    for n in range(1, len(aProsto)-1):
                        nPr = nCounter*aProsto[n]
                        if nPr <= nMax:
                            aSlozhno.append(nCounter*aProsto[n])
                        else:
                            break
                else:
                    aSlozhno.append(nCounter)


    return(len(aSlozhno) + len(aProsto)+1)




flag = 0
nChislo = 7000
nSumma  = 0
for n in range(1, nChislo+1):
    nSumma += n

while flag == 0:
    nChislo += 1
    nSumma += nChislo
    if nSumma%2 ==0 and nSumma%3 == 0 and nSumma%5 ==0:
        nKol = kol_del(nSumma)
        #print(nSumma, nKol)
        if nKol >= 400:
            print("ИТОГ: " + str(nSumma) + " : " + str(nKol))
        else:
            if nKol>600:
                flag = 1

nMax = 0
nItogo = 0
for n in range(13, 1000000, 1):
    nCounter = 0
    nTest = n


    while nTest != 1:
        if nTest%2 == 0:
            nTest = nTest/2
        else:
            nTest = nTest*3+1
        nCounter +=1
    if nCounter == 524:
        nMax = nCounter
        nItogo = n
        print(str(n) + ' количество: ' + str(nMax))
print('ИТОГО: ' + str(nItogo) + ' количество: ' + str(nMax))


# Путь через пирамиду (максимальная сумма пути)

lSpisok = ['75']
lSpisok.append('95 64')
lSpisok.append('17 47 82')
lSpisok.append('18 35 87 10')
lSpisok.append('20 04 82 47 65')
lSpisok.append('19 01 23 75 03 34')
lSpisok.append('88 02 77 73 07 63 67')
lSpisok.append('99 65 04 28 06 16 70 92')
lSpisok.append('41 41 26 56 83 40 80 70 33')
lSpisok.append('41 48 72 33 47 32 37 16 94 29')
lSpisok.append('53 71 44 65 25 43 91 52 97 51 14')
lSpisok.append('70 11 33 28 77 73 17 78 39 68 17 57')
lSpisok.append('91 71 52 38 17 14 91 43 58 50 27 29 48')
lSpisok.append('63 66 04 68 89 53 67 30 73 16 69 87 40 31')
lSpisok.append('04 62 98 27 23 09 70 98 73 93 38 53 60 04 23')

n = 15
aMatrica = [[0] * n for i in range(len(lSpisok))]
aSumma = [[0] * n for i in range(len(lSpisok))]
aSumma [0] [0] = 75
n = 0
for nRow in range(15):
    cStroka = lSpisok[nRow]
    for nCol in range(len(cStroka) // 3 + 1):
        nCurPoz = nCol * 3
        cZnach = cStroka[nCurPoz:(nCurPoz + 2)]
        if cZnach == '':
            cZnach = '0'
            print(nRow, nCol)
        aMatrica[nRow][nCol] = int(cZnach)
nRow = 0
nCol = 0
nSumma = 0

for nRow in range(14):
    for nCol in range(14):
        nSumma = aSumma[nRow][nCol] + aMatrica[nRow + 1][nCol]
        if  nSumma > aSumma[nRow + 1][nCol]:
            aSumma[nRow + 1][nCol] = nSumma

        nSumma = aSumma[nRow][nCol] + aMatrica[nRow + 1][nCol+1]
        if nSumma > aSumma[nRow + 1][nCol + 1]:
            aSumma[nRow + 1][nCol + 1] = nSumma

print(aSumma)


# Считаем воскресенья
aMonths = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
nSumma = 367-31
nKolvo = 0

for nYear in range(1901, 2001):
    for nMes in range (0, 12):
        if nMes == 2 and nYear%4 ==0:
            nSumma += 29
        else:
            nSumma += aMonths[nMes]
        if nSumma % 7 ==0:
            nKolvo += 1
    print(nYear, nKolvo)
print(nKolvo)


# считаем факториал 100!

import math
print(math.factorial(100))

nMax = 100
nMin = 2
nFaktorial = 1

aProsto= [2]

for n in range(2,nMax+1):
    if n not in aProsto:
        nFlag = 0
        for k in range(len(aProsto)):
            if n%aProsto[k] == 0:
                nFlag = 1
                break
        if nFlag == 0:
            aProsto.append(n)

for n in range(0, len(aProsto)):
    k = 1
    nStepen = 0
    while nMax//(aProsto[n]**k) > 0:
        nStepen += nMax//(aProsto[n]**k)
        k += 1
    nFaktorial = nFaktorial * aProsto[n]**nStepen

cFaktorial = str(nFaktorial)
print(cFaktorial)


nSumma = 0
for n in range(len(cFaktorial)):
    nSumma += int(cFaktorial[n])
    print(cFaktorial[n])

print(nSumma)

# 25 Считаем число Фиббоначи с 1000 знаками 4782   херня какая то

flag = 0
nFib1 = 1
nFib2 = 1
nFib3 = 0
nFib4 = 0
nIndex = 2

while flag == 0:
    nFibItog = nFib1 + nFib2
    nFib1 = nFib2
    nFib2 = nFibItog
    nIndex += 1
    if len(str(nFibItog)) >= 1000:
        flag = 1
print(nFib3)
print(nIndex)


# 21 Дружественные числа

nSummItog = 0
aItog = [0]

for n in range(4,10000+1):
    nSumm1 = 0
    nSumm2 = 0
    for n1 in range(1, n//2+1):
        if n%n1 == 0:
            nSumm1 += n1
    for n2 in range(1, nSumm1//2 +1):
        if nSumm1%n2 == 0:
            nSumm2 += n2
    if  nSumm1 != nSumm2 and nSumm2 == n:
        if nSumm1 not in aItog:
            aItog.append(nSumm1)
            aItog.append(nSumm2)
for n in range(len(aItog)):
    nSummItog += aItog[n]

print(nSummItog)

# 23 Неизбыточные числа (сумма)

def izbyt(n):
    nSumma = 1
    for k in range(1,len(lProsto)):
        if n%lProsto[k] ==0:
            nSumma += lProsto[k]
            nSumma += n/lProsto[k]
        if lProsto[k] > n/2:
            break
    if nSumma > n:
        return (1)
    else:
        return (0)


lProsto = [1, 2, 3, 5, 7, 11, 13]

for n in range(14, 28123//2 +1):
    nFlag = 0
    for k in range(1, len(lProsto)):
        if n % lProsto[k] == 0:
            nFlag = 1
            break
    if nFlag == 0:
        lProsto.append(n)

lIzb = []
lItogi = []
nItog = 1
for n in range (2,28500):
    if n == 28123:
        print(28123)
    nFlag = 0
    if izbyt(n) > 0:
        lIzb.append(n)
        for nCount in range(len(lIzb)):
            k = n + lIzb[nCount]
            if k < 30000:
                lItogi.append(k)
            else:
                break
    if n not in (lItogi):
        nItog += n
    if n%1000 == 0:
        print(n/1000)

print(nItog)

from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    for f in range(2, int(sqrt(n) + 1)):
        if n % f == 0:
            return False
    return True


num_prime = 1
n = 1
while num_prime < 10001:
    if is_prime(n):
        prime = n
        num_prime += 1
    n += 2

print(prime)


nRezult = 0.0000000000001

for n in range(2, 8):
    nRezult = '{0:f}'.format(float(1) / float(n))
    print(n, nRezult, decimal(1.0/n))


import numpy as np

n = 2

a = np.float64((1.0/3)*100000000000000000000)

print( "%20.20f" % a)


def drobi(nChislo):
    cStroka = ""
    nDelimoe = 10
    for n2 in range(1, 3000):
        nSimvol = nDelimoe//nChislo
        nOstatok = nDelimoe - nSimvol*nChislo
        cStroka += str(nSimvol)
        nDelimoe = 10*nOstatok
    return(cStroka)

def kolPeriod (cStroka):
    cLastNum = cStroka[len(cStroka)-1]
    if cStroka[len(cStroka)-10::] == cLastNum *10:
        if cStroka[len(cStroka)-1] == '0':
            return(0)
        else:
            return(1)

    for n4 in range(len(cStroka)-2, 1, -1):
        cSubStroka = cStroka[n4::]
        nDlinaStr = len(cStroka)
        nDlina = len(cSubStroka)
        cStr1 = cStroka[nDlinaStr - nDlina : nDlinaStr]
        cStr2 = cStroka[nDlinaStr - nDlina*2 : nDlinaStr - nDlina]

        if cStr1 == cStr2 and cSubStroka == cStr2:
            return(nDlina)
    return(0)


lSpisok = []

for n1 in range(900, 1000):
    lSpisok.append(drobi(n1))

nMax = 0
for n3 in range(len(lSpisok)):
    nKolvo = kolPeriod(lSpisok[n3])
    if nKolvo > nMax:
        nMax = nKolvo
        print(n3+900, nMax)
print("Itog:", nMax)

'''


lSpisok = []

lNabor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in range(10):
ddddddddddddddddddddddddddd