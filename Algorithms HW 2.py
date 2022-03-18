# Slit in Half
def string_split(n):
    temp1 = ''
    temp2 = ''

    if len(n) % 2 == 0:
        for i in n:
            temp1 = n[0:len(n)//2]
            temp2 = n[-len(n)//2:-1]

    else:
        for i in n:
            temp1 = n[0:len(n)//2+1]
            temp2 = n[-len(n)//2+1::]

    return temp2 + temp1

str1 = 'bbbbbcaaaaa'

print(string_split(str1))

#Unique characters in string
def string_unique(string: str):
    string = string.lower()
    d = {}
    for l in string:
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1
    print(d)

    for k, v in d.items():
        if d[k] == 1:
            return True
        else: return False


str2 = 'aabcde'
print(string_unique(str2))
