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
eles = list(set(re.findall('[A-Z][a-z]?|\((?:[^()]*(?:\(.*\))?[^()]*)+\)', rea)))
coeffs = np.zeros([len(eles), dim])
for i in rea_comps:
    rea_eles.append(re.findall('[A-Z][a-z]?\d*|\((?:[^()]*(?:\(.*\))?[^()]*)+\)\d+', i))
for i in pro_comps:
    pro_eles.append(re.findall('[A-Z][a-z]?\d*|\((?:[^()]*(?:\(.*\))?[^()]*)+\)\d+', i))
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
#print(np.linalg.solve(np.matrix(coeffs)[:dim-1,:dim-1], np.zeros(dim-1)))
#print(np.matrix(coeffs)[:dim-1,:dim-1])
#print(np.matrix(coeffs)[:dim-1,dim-1])
a = 1
coes = []
try:
    #print(np.linalg.solve(np.matrix(coeffs)[:dim-1,:dim-1], np.matrix(coeffs)[:dim-1,dim-1]))
    for i in np.array(np.linalg.solve(np.matrix(coeffs)[:dim-1,:dim-1], np.matrix(coeffs)[:dim-1,dim-1])):
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
except np.linalg.LinAlgError:
    print("Warning: the number of elements is too small")
