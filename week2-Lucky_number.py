n = int(input("Lutfen ust siniri giriniz: "))
s = [i for i in range(1,n + 1)]
print("Original sequence: ",s)
a = 2
for i in range(1,len(s)):
    del s[a-1::a]
    a += 1
print("Lucky numbers are ",s)