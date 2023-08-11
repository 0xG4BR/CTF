import string
def twos_complement(num, num_bits):
    # Calculate the two's complement of a negative integer
    max_value = 2 ** num_bits
    return (max_value + num) % max_value

alpha = string.printable
obf = ["F3E8CBAE4506845A","D008415E3DA6FE57","A000DD2081212233","1D18F58B0471AF23","3E7842CE09650FE1","ACE032648FCA37C3","95F407C02A7C91DE","527AB667E553409F","2E7282C94B833F4E","C7D7B7CC1EF11C76","1635194D1A79108A","9244AB86CD2B437D","24A79BB914980ED4","4FFDF0D33AE23C1B","DA6A80480CA3D177","EC0B96FA5B47D8BD","E727B17F11D949CF","5DB33628E663B2C5","9CB0F62570A8DCFB","FCA985E439B85FA5","74FF69F230510213","6158C21746B559BF","EF6CEE899EA4EB99","DB6DBC548C7390A2","34F7508DA1E3D62C","6B68BE8E7B01F9D5","1F15932FED2D9D55","56EA5C0DF8AA88C4","4A626F05389AC103","AD7E75299460DF12","3B87BABBB4310AE9","C6974CC8666ED226"]

v6 = []

for i in range(0,len(obf)):
  for j in range(0,len(obf[i]),2):
    v6.append(obf[i][-2]+obf[i][-1])
    obf[i] = obf[i][:len(obf[i]) - 2]

obf = v6

v3 = "689df84315f73e8c01efe535"

v1 = ["A2D81B89C91EA301","50BEEA056C0664AD","EFB9C02AF9C37924","BB059906A5477823","97847BFE5A064AFC","F3C8F3B317BD0EEC"]
for i in v1:
   print(len(i))
v6 = []
for i in range(0,len(v1)):
  for j in range(0,len(v1[i]),2):
    v6.append(v1[i][-2]+v1[i][-1])
    v1[i] = v1[i][:len(v1[i]) - 2]
v1 = v6
v1.append('3A')
print(len(v1))
v2 = -4294
v10 = 0
v9 = 0
inp_byte = 0
flag = [";"]*50
for inp in alpha:
    if ";" not in flag:
       break
    for i in range(0,50 - 1):

        inp_byte = inp
        v10 =  int(obf[ord(inp_byte)],16)
        v9 = ord(v3[i % 24])
        if ( ((i % 24) & 1) != 0 ):
         v9 = ~v9
        v10 ^= v9
        v10 = int(obf[v10],16)
        if ( (v10 & 1) != 0 ):
            v10 ^= 0x42
        v10 = twos_complement(~v10,8) 
        if ( v10 == int(v1[i],16)):
            flag[i] = inp
            print(flag)


print("".join(flag))

