import re
import numpy as np

rad_num = {}

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
print(type(coeffs))
print(np.linalg.solve(coeffs, np.zeros([1, dim])))
