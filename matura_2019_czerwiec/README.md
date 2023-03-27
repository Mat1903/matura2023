Zadanie 4. Wybrane liczby
=================

Liczby pierwsze to liczby naturalne większe od 1, które mają dokładnie dwa dzielniki: jedynkę
i samą siebie.
Dane są dwa pliki: `liczby.txt` i `pierwsze.txt`. Plik `liczby.txt` zawiera 300
wierszy. W każdym wierszu tego pliku znajduje się jedna liczba całkowita dodatnia z zakresu
od 1 do 100 000.
Plik pierwsze.txt zawiera 200 wierszy. W każdym wierszu tego pliku znajduje się jedna
liczba pierwsza z zakresu od 10 do 1 300 000.
Uwaga: pomocnicze pliki `liczby_przyklad.txt` i `pierwsze_przyklad.txt`,
zawierają dane, które możesz wykorzystać, aby sprawdzić poprawność działania swojego(-ich)
programu(-ów). Każdy z nich zawiera po 50 wierszy. W każdym wierszu znajduje się jedna
liczba. Odpowiedzi dla danych z tych plików są podane pod treściami zadań.

**Napisz program** (lub kilka programów), który(e) da(dzą) odpowiedzi do poniższych zadań. Pliki źródłowe z rozwiązaniem zapisz pod nazwą zgodną z numerem zadania,
z rozszerzeniem odpowiadającym użytemu językowi programowania
## Zadanie 4.1. (0–4)

Podaj, (zachowując ich kolejność) te liczby z pliku `liczby.txt`, które są liczbami
pierwszymi z przedziału 〈100; 5000〉. Odpowiedź zapisz w pliku `wyniki4_1.txt`.
Dla pliku `liczby_przyklad.txt` odpowiedzią są liczby: 103, 163, 173, 701, 1033, 2137,
3529, 4933, 977, 2143.

## Zadanie 4.2. (0–4)

Podaj, w kolejności ich występowania w pliku `pierwsze.txt`, wszystkie te liczby, które
czytane od prawej do lewej również są liczbami pierwszymi. Odpowiedź zapisz w pliku
`wyniki4_2.txt.`
Przykład:
Jeśli odczytamy liczbę pierwszą 17 od prawej do lewej, otrzymamy liczbę 71, która również
jest liczbą pierwszą.
Dla pliku pierwsze_przyklad.txt liczbami spełniającymi warunek zadania są: 701,
709, 1033, 167, 1109, 1619, 1009, 179, 1499, 76001, 1601, 31873

## Zadanie 4.3. (0–4)

Niech w(N) oznacza sumę cyfr liczby N. Dla danej liczby N tworzymy ciąg, w którym
N = w(N), a każdy kolejny element jest sumą cyfr występujących w poprzednim elemencie:
                                N1 = w(N)
                                N2 = w(N1)
                                N3 = w(N2)

Ciąg kończy się, gdy jego wyraz jest liczbą jednocyfrową. Tę liczbę nazywamy wagą liczby
N.

## ODPOWIEDZI: 

`Odpowiedź do zadania4.1:` [563, 2087, 163, 2423, 3581, 911, 997, 113, 1049, 1511, 2467, 283, 3559, 521, 4201, 877, 1301, 2749, 4919, 1213, 2039, 4111, 3331, 401, 2221]

`Odpowiedź do zadania4.2:` [31, 37, 101, 1009, 1021, 113, 1499, 1213, 1217, 1229, 1231, 1237, 1487, 1223, 7027, 7043, 3821, 31873, 1511, 140527, 151169, 151189, 193261, 1297001, 1061, 100267, 100271, 100279, 181957, 13, 112163, 112181, 3803, 76001, 160183, 160201, 160243, 17, 907, 701, 383, 389, 1103, 1109, 31721, 1583, 1597, 1601, 1619, 3571, 112111]

`Odpowiedź do zadania4.3:` 27
