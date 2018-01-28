#!/usr/bin/env python3
import re
import numpy as np
from fractions import gcd, Fraction

rad_num = {}

def lcm(x, y):
    return x*y/gcd(x,y)
rea, pro = input('please enter the chemistry equation\n').split('=')
rea_comps = rea.split('+')
pro_comps = pro.split('+')
rea_eles = []
pro_eles = []
dim = len(rea_comps) + len(pro_comps)
eles = list(set(re.findall('[A-Z][a-z]?', rea)))
coeffs = np.zeros([len(eles), dim])
for i in rea_comps:
    rea_eles.append(re.findall('[A-Z][a-z]?\d*|\(.*?\)\d*', i))
    for j in rea_eles[-1]:
        if '(' in j:
            rea_eles[-1].remove(j)
            for k in range(int(re.findall('\d*$', j)[0] if re.findall('\d*$', j)!=[''] else '1')):
                for m in re.findall('[A-Z][a-z]?\d*', re.findall('\((.*?)\)', j)[0]):
                    rea_eles[-1].append(m)
for i in pro_comps:
    pro_eles.append(re.findall('[A-Z][a-z]?\d*|\(.*?\)\d*', i))
    for j in pro_eles[-1]:
        if '(' in j:
            pro_eles[-1].remove(j)
            for k in range(int(re.findall('\d*$', j)[0] if re.findall('\d*$', j)!=[''] else '1')):
                for m in re.findall('[A-Z][a-z]?\d*', re.findall('\((.*?)\)', j)[0]):
                    pro_eles[-1].append(m)
for ele in range(len(eles)):
    for i in range(len(rea_eles)):
        for j in rea_eles[i]:
            if eles[ele] in j:
                if j.replace(eles[ele], '').isdigit():
                    coeffs[ele][i] += int(j.replace(eles[ele], ''))
                elif j.replace(eles[ele], '').strip() == '':
                    coeffs[ele][i] += 1
    for i in range(len(rea_eles) ,len(rea_eles)+len(pro_eles)):
        for j in pro_eles[i-len(rea_eles)]:
            if eles[ele] in j:
                if j.replace(eles[ele], '').isdigit():
                    coeffs[ele][i] -= int(j.replace(eles[ele], ''))
                elif j.replace(eles[ele], '').strip() == '':
                    coeffs[ele][i] -= 1

print(coeffs)
if coeffs.shape[0] < coeffs.shape[1] - 1:
    print("Error: more items than elements")
    exit()
#print(np.linalg.solve(np.matrix(coeffs)[:dim-1,:dim-1], np.zeros(dim-1)))
#print(np.matrix(coeffs)[:dim-1,:dim-1])
#print(np.matrix(coeffs)[:dim-1,dim-1])
a = 1
coes = []
#print(np.linalg.solve(np.matrix(coeffs)[:dim-1,:dim-1], np.matrix(coeffs)[:dim-1,dim-1]))
for i in np.array(np.linalg.solve(np.matrix(coeffs)[:dim-1,:dim-1], np.matrix(coeffs)[:dim-1,-1])):
    #print(Fraction(i[0]).limit_denominator())
    coes.append(Fraction(i[0]).limit_denominator())
for i in coes:
    a = lcm(a, i.denominator)
coes.append(1)
for i in range(len(coes)):
    coes[i] = abs(coes[i]*a)
for i in range(len(coes)):
    coes[i] = str(int(coes[i])) + ' ' + (rea_comps+pro_comps)[i]
coes[len(rea_comps)-1]+=' = '+coes[len(rea_comps)]
del coes[len(rea_comps)]
print(' + '.join(coes))
