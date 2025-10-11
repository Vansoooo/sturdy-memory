s = input()
count_g = int((s.count('G')/len(s)*100))
count_c = int((s.count('C')/len(s)*100))
print("g: ",count_g,"%","c: ",count_c,"%")
for i in range(len(s)):
    if s[i] in 'AT':
        s = s.replace(s[i],'*')
    if s[i] in 'CG':
        s = s.replace(s[i],'#')
if s == s[::-1]:
    print('палиндром')
else:
    print('не палиндром')