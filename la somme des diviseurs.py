
M=int(input("veuillez saisir un nombre:"))
N=int(input("veuillez saisir un nombre:"))
SM=0
SN=0
for i in range(2,M):
    if(M%i==0):
        SM+=i
for j  in range(2,N):
    if (N%j==0):     
        SN+=j
if (SM==N) and (SN==M):
    print(M,"et",N,"sont des amis")
else:
    print(M,"et",N," ne sont pas des amis")