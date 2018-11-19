import pickle

key = [0]*16
for mode in ['A', 'B', 'C', 'D']:
    with open('key' + mode + '.pkl', 'rb') as f:
        key_candidate = pickle.load(f)

    for x in key_candidate[0]:
        if x in key_candidate[1] and x in key_candidate[2]:
            print(x)
            if mode == 'A':
                key[0] = x[0]
                key[7] = x[1]
                key[10] = x[2]
                key[13] = x[3]
                break
            elif mode == 'B':
                key[1] = x[0]
                key[4] = x[1]
                key[11] = x[2]
                key[14] = x[3]
                break
            elif mode == 'C':
                key[2] = x[0]
                key[5] = x[1]
                key[8] = x[2]
                key[15] = x[3]
                break
            elif mode == 'D':
                key[3] = x[0]
                key[6] = x[1]
                key[9] = x[2]
                key[12] = x[3]
                break
print(key)
with open('10Rkey.txt', mode='w') as f:
    original_key = '0x'
    for i in key:
        original_key += format(i, '02x')
    f.write(original_key)
print(original_key)
