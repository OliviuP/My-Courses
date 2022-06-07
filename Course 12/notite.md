#Python interpretor

Interpretorul este un program care converteste fiecare expresie (linie de cod)
dintr-un limbaj de programare de nivel inalt, in cod masina.

Atat compilatoarele cat si interpretoarele, indeplinesc aceeasi functie si anume sa conveteasca 
din limbaj de programare de nivel inalt in cod masina, principala diferenta
fiind ca un compliator converteste tot codul in cod masina inainte ca programul
sa fie executat

## Compilator vs Interpretor

|                       | compliator                                                                                                                                                                                                                                                                                                                                                    | interpretor                                                                                         |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| pasi in programare    | 1. scrie programul <br>2. Compilatorul va citi și analiza toate liniile de cod pentru corectitudine;daca găsește incorectitudini va arunca o eroare <br>3. Compliatorul va converti codul sursa în cod masina<br>4. Creează legături între diferite fișiere de cod, obtinanduse un program rulabil / executabil (cunoscut ca și .exe)<br>5. Executa programul | 1. Scrie programul <br>2. Executa codul sursa, linie cu linie                                       |
| Avantaje              | Întreg programul este deja tradus în cod mașină, astfel ca timpul de execuție este mai scurt                                                                                                                                                                                                                                                                  | Mai usor de folosit/ înțeles în special pentru începători                                           |
| Dezavantaje           | Nu poti modifica programul (executabilul) fără a recomplila tot proiectul.                                                                                                                                                                                                                                                                                    | Poti rula doar pe computere care au interpretorul corespunzător programului                         |
| Durata de executive   | Rapid                                                                                                                                                                                                                                                                                                                                                         | Incet                                                                                               |
| Generarea programului | Generează un fișier executabil care poate fi executat independent de programul original                                                                                                                                                                                                                                                                       | Nu generaza fisher executabil; de fiecare data când se executa codul sursa îl va interpreta din nou |
| Executarea            | Executarea este separată de compilare; se întâmplă doar după ce tot programul a fost complet.                                                                                                                                                                                                                                                                 | Executarea este parte a procesului de interpretare( linie cu linie)                                 |
| Necesar de memorie    | Programul se executa independent și nu necesita compilatorul în memorie                                                                                                                                                                                                                                                                                       | Interpretorul exista în memorie în timpul execuției.                                                |
| Optimizari            | Vede tot programul înainte sa îl transforme în cod mașină, așa capoate face ce oprimizari crede<br>ca sunt necesare astfel încât codul sa ruleze mai repede.                                                                                                                                                                                                  | Nu poate face optimizări pentru ca nu vede tot codul înaintea execuției                             |
| Erori                 | Arata toate erorile după ce programul este complilat                                                                                                                                                                                                                                                                                                          | Arata erorile dintr-o singura linie de cod.                                                         |
| Limbaje               | C, C++, C#, Java                                                                                                                                                                                                                                                                                                                                              | Python, Perl, PHP, Ruby                                                                             |

---
Modul -> un script ( fisier cu extensia .py) care este inportat de alte module

Script -> Fisier cu extensia .py ce contine cod python

Pachet -> Un director (Folder) in care se afla scripturi python; mai mult decat
un pachet trebuie sa contina un fisier numit `__init__.py`

Standard library -> biblioteca care deja exista in python si este usor de importat

External library -> Biblioteca care trebuie instalata cu pip, pentru a putea fi utilizata

---

## Importuri 

`import modul_a` -> importarea unui modul cu redenumire

`import modul_a as m_a` -> importarea unui modul cu redenumire

`from modul_a import find_index` -> importatrea unei singure functii dintr-un modul

`from modul_a import *` -> importarea tuturor obiectelor (functii, clase sau alte variabile) dintr-un modul

---

## Reguli de import 

- Un singur import pe fiecare linie

- Importurile trebuie impartite in 3 sectiuni:
    - Module din librarii standard
    - Module din librarii externe 
    - Module din proiect (codul nostru)

- In fiecare sectiune importurile ar trebui sortate alfabetic

---

## Ordinea de cautare a importurilor

1. Directorul curent

2. Orice cale derivata din variabila de sistem **PYTHONPATH**

3. Locatia librariilor standard

4. Locatia librariilor externe

# PIP (Package installer for Python)

`pip` ->  librarie care ne ofera posibilitatea de a instala pachete externe 

`pip help` -> arata toate comenzile disponibile si cum pot fi folosite

`pip install <nume_pachet>` -> instaleaza pachetul cu numele specificat( cea mai recenta versiune)

`pip uninstall <nume_pachet` -> dezinstaleaza pachetul cu numele specificat

`pip freeze` -> afiseaza toate pachetele externe instalate si versiunile lor 

`pip freeze > requirements.txt` -> salveaza lista afisata de `pip freeze`, intr-un fisiere cu numele specificat

`pip list -o` -> afiseaza doar pachetele pentru care exista o veriune mai noua decat cea instalata

`pip install -U <nume_pachet` -> daca pachetul este instalat deja instaleaza ultima versiune disponibila

`pip install <nume_pachet>==versiune` -> instaleaza pachetul cu versiunea specificata

# Virtualenv

Scopul enviroment-urilor este sa creeze un spatiu izolat pentru librariile unui
proiect 

Acest lucru ajuta ca fiecare proiect sa aibe propriile dependente, indiferent de pachete sau versiuni ale acelorasi pechete sunt folosite de oricare program in parale

Nu exista un numar maxim de enviroment-uri ce pot fi create

## Virtualenvwrapper 

`mkvirtualenv <env_name>` -> creearea uniui enviroment virtual

`workon <env_name>` -> activarea unui enviroment virtual

`deactivate` -> dezactivarea unui enviroment virtual

`lsvirtualenv` -> afiseaza toate enviromenturile create 

`rmvirtualenv <env_name>` -> sterge un enviroment virtual

# Pachet Propriu

De ce avem nevoie:

- Librarie setuptools -> librarie care ajuta la impachetarea si pregatirea
propriului pachet pentru a il trimite pe serverul pypi(python package index)
- fisierul setup.py -> configuratia initala pentru impachetarea propirului pachet 
- fisierul MANIFEST.in -> contine numele tuturor fisierelor care nu sunt de tip .py pentru
a informa funtia setup sa le includa in pachet.
- fisierul README.md -> contine documentatia proiectului
- unealta twine -> ajuta la publicarea pachetului in pypi

## Pasi pentru creearea unui pachet propriu 

1. Creeaza un folder nou 
2. Creeaza un enviroment nou si activeaza enviromentul
3. Instaleaza setuptools (`pip install setuptools`)
4. Creeaza fisierul `setup.py`

```from setuptools import setup


setup(
    name="sergiu-dyno", # numele cu care va fi vizibilă librăria noastră în PYPI
    version="0.1.0",# versiunea curentă a librăriei
    author="Matei Sergiu",
    author_email="mateisergiu777@gmail.com",
    packages=["sergiu_dyno"], # Folderul in care se afla codul sursa 
    package_dir={"": "src/"}, # Calea către codul sursă al librăriei
    include_package_data=True, # Dacă librăria conține și alte tipuri de fișiere decât fișiere python
    description="Prints a dinosaur"
)

```

5. Creeaza directorul src/<nume_proiect> si adauga codul librariei
6. Creeaza fisierul de requirements (`pip freeze > requirements.txt`)
7. Creeaza fisierul README.md
8. Creeaza fisierul MANIFEST.in
9. Instalare py (`pyp install twine wheel`)
10. Incarcare pachet pe pypi(`)
    1. `python setup.py sdist`
    2. `python setup.py bdist_wheel`
    3. `twine upload dist/<nume_arhiva_whl_cu_cea_mai_recenta_versiune>`

!!! Atentie 

Pentru orice modificare adusa pachetului, este necesara schimbarea versiunii din fisierul `setup.py` (incrementare cu 1| 0.1.0 | 0.2.0)
si urmarea pasului 10 pentru a acutliza versiunea pachetului din pypi