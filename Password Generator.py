# Password Generator
import random

print("--------------------------------------")
print("-----Strong Password Generator--------")
print("--------------------------------------")
char = input("How long password do you need....? ")
print("--------------------------------------")
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
a_z = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
A_Z = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
sym = ['@', '#', '$', '%', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

ans = ()
for i in range(int(char)):
    passwd = (random.choice(num),random.choice(a_z),random.choice(A_Z),random.choice(sym))
    ans= ans+passwd

print("Your Password is = ")
for j in ans[:int(char)]:
    print(j,end="")

print("\n--------------------------------------")
