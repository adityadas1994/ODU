name1 = raw_input("What's your name? ")                 #stores the person's name
name2 = raw_input("What's the other person's name?")    #stores the other person's name
name3 = " "                                             #empty variable for the smaller name
name4 = " "                                             #empty variable for the larger name
comp = 0
s0=0
fcounter = 0
s1 = len(name1)
s2 = len(name2)
s5 = s1+s2
a=0

s6 = list("FLAMES")
if (s1 < s2):                       #finding the smaller name and storing it in name3 and storing the larger name in name4
    name3 = name1
    name4 = name2
else:
    name3 = name2
    name4 = name1
s3 = list(name3)                #converting the names to list to manipulate them
s4 = list(name4)
i=0
j=0
counter=0
for i in range(0,len(s3)-1):                #loop to find the number of matching letters
    for j in range(0,len(s4)-1):
        if s3[i] == s4[j]:
            comp = comp+2
            i=i+1
            break
counter=s1+s2                   #stores the total length of the names
i=0
while fcounter<5:               #the flames strike counter
    if i<6:                     #if index less than 6
        print (fcounter)            #debugging print !! not required
        if s6[i]!='*':              #if the letter in flame already struck out ignore and go to next index
            if counter == 1:        #if the flame counter has dropped to 1
                counter = comp/2
                fcounter+=1         #incrementing the strike counter
                s6[i]='*'           #striking the letter in flames string
            else:
                i=i+1
                counter= counter - 1        #counting the flame counter
    else:
        i=(comp/2)-i                #if the index reaches 6 then it is directly made the value that is left after subtracting the comp -i value
    i=i+1

print (s6)                  #debugging print!! not required
for a in range(6):
    if(s6[a]!="*"):
        print (s6[a])           #print the relationship
