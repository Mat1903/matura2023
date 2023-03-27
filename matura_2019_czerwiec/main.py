dane = open("liczby.txt")
dane_tablica=[]

dane_pierwsze = open("pierwsze.txt")
dane_tablica_pierwsze=[]

def czypierwsza(n):
    if n==2:
        return True
    if n == 0 or n == 1:
        return False
    for i in range(2,n//2+1):
        if n % i == 0:
            return False
    return True

def waga(n):
    sum=0
    sum_tmp=0
    for i in str(n):
        sum+=int(i)
    while sum>=10:
        sum_tmp=sum
        sum=0
        for i in str(sum_tmp):
            sum+=int(i)
    return sum



for i in dane:
    dane_tablica.append(int(i.rstrip()))

for i in dane_pierwsze:
    dane_tablica_pierwsze.append(int(i.rstrip()))

Odp_1=[]

for i in dane_tablica:
    if i>=100 and i<=5000 and czypierwsza(i):
        Odp_1.append(i)

Odp_2=[]

for i in dane_tablica_pierwsze:
    if czypierwsza(int(str(i)[::-1])):
        Odp_2.append(i)


Odp_3 = 0

for i in dane_tablica_pierwsze:
    if waga(i)==1:
        Odp_3+=1
print()

print(f"Odpowiedź do zadania4.1: {Odp_1}")
print()
print(f"Odpowiedź do zadania4.2: {Odp_2}")
print()
print(f"Odpowiedź do zadania4.3: {Odp_3}")
print()