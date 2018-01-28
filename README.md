# A simple program to balance some chemistry equations
### environment: python3 with re, numpy and fractions libs installed
#### caution: only based on conservation of mass, so not work for equations with less elements than components, and only work for equations with parentheses
## Usage:
**Linux Environment:**
```
./equation.py
```
or
```
python equation.py
```
when prompt shown, enter the equation:
### example
Fe3C+HNO3=Fe(NO3)3+CO2+NO2+H2O

and program output the result:

1 Fe3C + 22 HNO3 = 3 Fe(NO3)3 + 1 CO2 + 13 NO2 + 11 H2O

if you enter the equation which have more items than elements, such as:

H2S+KMnO4+H2SO4=MnSO4+K2SO4+S+H2O

the program will exit, and print "Error: more items than elements"
