# coding: utf-8
from AES import *
import pickle
import numpy as np

_Nk = 4
_Nr = 10



def Round(In):
    i = 0
    Step1 = SubBytes(In)  # SubBytes() #5.1.1
    Step2 = ShiftRows(Step1)  # ShiftRows() #5.1.2
    output = Mixcolums(Step2)  # Mixcolums #5.1.3 #Round10　では行わない
    return(output)


for mode in ['A', 'B', 'C', 'D']:
    print(mode)
    A = []
    inpu = "00000000000000000000000000000000"
    for n in range(4):
        for num in range(1, 256, 1):
            inp = split(inpu, 2, _Nk)  # ８bit毎に分割(split)
            a = Round(inp)[0]

            if mode == 'A':
                inp[n][n] = '0x' + format(num, '02x')
            elif mode == 'B':
                if n == 0:
                    inp[0][3] = '0x' + format(num, '02x')
                elif n == 1:
                    inp[1][0] = '0x' + format(num, '02x')
                elif n == 2:
                    inp[2][1] = '0x' + format(num, '02x')
                elif n == 3:
                    inp[3][2] = '0x' + format(num, '02x')
            elif mode == 'C':
                if n == 0:
                    inp[0][2] = '0x' + format(num, '02x')
                elif n == 1:
                    inp[1][3] = '0x' + format(num, '02x')
                elif n == 2:
                    inp[2][0] = '0x' + format(num, '02x')
                elif n == 3:
                    inp[3][1] = '0x' + format(num, '02x')
            elif mode == 'D':
                if n == 0:
                    inp[0][1] = '0x' + format(num, '02x')
                elif n == 1:
                    inp[1][2] = '0x' + format(num, '02x')
                elif n == 2:
                    inp[2][3] = '0x' + format(num, '02x')
                elif n == 3:
                    inp[3][0] = '0x' + format(num, '02x')

            num = {'A': 0, 'B': 1,
                   'C': 2, 'D': 3}
            b = Round(inp)[num[mode]]

            diff = []
            for i in range(4):
                diff.append((int(a[i], 0) ^ int(b[i], 0)))
            A.append(diff)

    A = np.array(A)
    with open('D10' + mode + '.pkl', 'wb') as f:
        pickle.dump(A, f)
