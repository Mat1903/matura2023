class Matura2019czerwiec:

    def __init__(self):
        with open('liczby.txt', 'r') as file:
            self.data = [int(x.strip()) for x in file.readlines()]

        with open('pierwsze.txt', 'r') as file:
            self.data_primal = [int(x.strip()) for x in file.readlines()]

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

    def zadanie4_1(self):
        Odp_1 = []
        for i in data:
            data_list.append(int(i.rstrip()))
        for i in data_list:
            if i>=100 and i<=5000 and if_prime_number(i):
                Odp_1.append(i)

        return Odp_1
    def zadanie4_2(self):
        Odp_2 = []
        for i in data_primal:
            data_list_primal.append(int(i.rstrip()))
        
        for i in data_list_primal:
            if if_prime_number(int(str(i)[::-1])):
                Odp_2.append(i)

        return Odp_2

    def zadanie4_3(self):
        Odp_3 = 0
        for i in data_primal:
            data_list_primal.append(int(i.rstrip()))
        
        for i in data_list_primal:
            if waga(i)==1:
                Odp_3+=1

        return Odp_3

