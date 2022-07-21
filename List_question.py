s = 'my name is devika'
s_value = []
tmp = ''
for c in s:
    if c == ' ':
        s_value.append(tmp)
        tmp = ''
    else:
        tmp += c
if tmp:
    s_value.append(tmp)
    print(s_value)