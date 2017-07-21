name1 = input("What's your name? ")
name2 = input("What's the other person's name?")
name3 = " "
name4 = " "
comp = 0
s0=0
fcounter = 0
s1 = len(name1)
s2 = len(name2)
s5 = s1+s2
a=0

s6 = list("FLAMES")
if (s1 < s2):
    name3 = name1
    name4 = name2
else:
    name3 = name2
    name4 = name1
s3 = list(name3)
s4 = list(name4)
i=0
j=0
counter=0
for i in range(len(s3)):
    for j in range(len(s4)):
        if s3[i] == s4[j]:
            comp = comp+2
            i=i+1
            break
    break
i=0
counter=s1+s2
while fcounter<5:
    if i<6:
        print (fcounter)
        if s6[i]!='*':
            if counter == 0:
                counter = s1+s2
                fcounter+=1
                s6[i]='*'
            else:
                i=i+1
                counter= counter - 1
    else:
        i=(comp/2)-i
    i=i+1

print (s6)
for a in range(6):
    if(s6[a]!="*"):
        print (s6[a])
