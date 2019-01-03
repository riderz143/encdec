op=int(input("1.Encrypt  2.Decrypt \n"))
def en():
    k1=0
    i=4
    key=input("Enter key:")
    f=input("Enter filename:")
    f1=open(f,'r')
    for k in key:
        k1=k1+ord(k)+i
        i=i+4
    k1=(k1*4)%94+32
    mes=f1.read()
    f1.close()
    f1=open(f,'w')
    i=0
    for  m in mes:
        if(m==' ' or m=='\n' or m=='\t'):
            f1.write(m)
        else:
            if(i%2==0):
                if(ord(m)+k1<127):
                    f1.write(chr(ord(m)+k1))
                else:
                    f1.write(chr(ord(m)-94+k1))
            else:
                if(ord(m)-k1>31):
                    f1.write(chr(ord(m)-k1))
                else:
                    f1.write(chr(ord(m)-k1+94))
        i=i+1
    f1.close()
def de():
    k1=0
    i=4
    key=input("Enter key:")
    f=input("Enter filename:")
    f1=open(f,'r')
    for k in key:
        k1=k1+ord(k)+i
        i=i+4
    k1=(k1*4)%94+32
    mes=f1.read()
    i=0
    f1.close()
    f1=open(f,'w')
    for  m in mes:
        if(m==' ' or m=='\n' or m=='\t'):
            f1.write(m)
        else:
            if(i%2!=0):
                if(ord(m)+k1<127):
                    f1.write(chr(ord(m)+k1))
                else:
                    f1.write(chr(ord(m)-94+k1))
            else:
                if(ord(m)-k1>31):
                    f1.write(chr(ord(m)-k1))
                else:
                    f1.write(chr(ord(m)-k1+94))
        i=i+1
    f1.close()
if(op==1):
    en()
elif(op==2):
    de()
