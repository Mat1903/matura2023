data = open("liczby.txt")
data_list=[]

data_primal = open("pierwsze.txt")
data_list_primal=[]

def if_prime_number(n):
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



for i in data:
    data_list.append(int(i.rstrip()))

for i in data_primal:
    data_list_primal.append(int(i.rstrip()))

Odp_1=[]

for i in data_list:
    if i>=100 and i<=5000 and if_prime_number(i):
        Odp_1.append(i)

Odp_2=[]

for i in data_list_primal:
    if if_prime_number(int(str(i)[::-1])):
        Odp_2.append(i)


Odp_3 = 0

for i in data_list_primal:
    if waga(i)==1:
        Odp_3+=1
print()

print(f"Odpowiedź do zadania4.1: {Odp_1}")
print()
print(f"Odpowiedź do zadania4.2: {Odp_2}")
print()
print(f"Odpowiedź do zadania4.3: {Odp_3}")
print()