# files-question4
# Iss text ko question3.txt ke naam ki file mein save karo.
# Code Example

# rishabh - meerut
# imtiyaz - delhi
# nilima - cochin
# rati - shimla
# ayishah - delhi
# raghu - shimla
# naseer - kanpur
# karthikeyan - delhi
# salma - jaipur
# pankaj - delhi
# brijesh - delhi
# govind - delhi
# puneet - shimla
# siddhi - delhi
# suman - jaipur
# rajeev - shimla
# mohinder - delhi
# rajendra - jaipur
# priyanka - shimla
# neela - delhi
# sashi - jaipur
# sarika - delhi
# deepti - shimla
# harshad - delhi
# trishna - raipur
# pradeep - jaipur
# sekhar - delhi
# nand - delhi
# anoop - delhi
# balwinder - tokyo

# Iss file mein dhyaan se dekhoge toh ek insaan ka naam aur ek sheher ka naam milegaYeh sheher woh sheher hai jisme woh insaaan rehta hai. Ab aapne ek aisa code likhna hai jo:
# 1 Delhi mein rehne waale logon ko ek alag file mein daale. Delhi waali file ka naam "delhi.txt" hona chaiye.
# 2 Shimla mein rehne waale logon ko ek alag file mein daale. Shimla waali file na naam "shimla.txt" hona chaiye
# 3 Aur saare log jo delhi aur shimla mein nahi rehte, unko ek alag file mein daale. Iss file ka naam "others.txt" hona chaiye
# Aapko aisa code likhna hai, jo aisi file mein kitni bhi lines pe chal paye.

name="""rishabh - meerut
imtiyaz - delhi
nilima - cochin
rati - shimla
ayishah - delhi
raghu - shimla
naseer - kanpur
karthikeyan - delhi
salma - jaipur
pankaj - delhi
brijesh - delhi
govind - delhi
puneet - shimla
siddhi - delhi
suman - jaipur
rajeev - shimla
mohinder - delhi
rajendra - jaipur
priyanka - shimla
neela - delhi
sashi - jaipur
sarika - delhi
deepti - shimla
harshad - delhi
trishna - raipur
pradeep - jaipur
sekhar - delhi
nand - delhi
anoop - delhi
balwinder - tokyo"""

u=open("list.txt","w")
b=u.write(name)
print(b)
u.close()
b=open("list.txt","r")
f=b.read().splitlines()
for i in f:
    if "delhi" in i:
        f=open("delhi.txt","a")
        f.write(i)
        f.write("\n")
        f.close()
    if "shimla" in i:
        f=open("shimla.txt","a")
        f.write(i)
        f.write("\n")
        f.close()
    if "delhi" not in i and "shimla" not in i:
        f=open("other.txt","a")
        f.write(i)
        f.write("\n")
        f.close()
f=open("delhi.txt","r")
print(f.read())