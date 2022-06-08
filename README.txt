By użyć programu bez instalacji dodatkowych bibliotek można wykorzystać pipenv:

w cmd:
pipenv install
pipenv run python .\main.py

Program jest prostym mockupem systemu logowania opartego na odcisku palca i rozpoznawaniu płci poprzez głos.
Po uruchomieniu programu widzimy dwie opcje:
0 - nowy użytkownik
1 - zarejestrowany użytkownik

DLA NOWEGO UŻYTKOWNIKA:
Po wybraniu '0' zostaniemy poproszeni o wprowadzenie kilku danych:
- imię / login
- płeć (m / k)
- plik odcisku palca (z folderu fingers_data_base)
- plik głosowy (z folderu voices) (podczas wpisywania trzeba dodać voices\ przed nazwą pliku)

DLA ZAREJESTROWANEGO UŻYTKOWNIKA:
Po wybraniu '1' zostaniemy poproszeni o wprowadzone wcześniej imię / login
(każda wartość wpisana zostaje sprawdzona w bazie danych)

Po wprowadzeniu danych, które zostaną zaakceptowane, użytkownik zostanie zalogowany
