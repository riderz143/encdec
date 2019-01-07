op=int(input("1.Encrypt  2.Decrypt \n"))
def en():
    k1=0
    i=4
    key=input("Enter key:")
    for k in key:
        k1=k1+ord(k)+i
        i=i+4
    k1=(k1*12)%93+33
    f=input("Enter filename:")
    f2=open(f,'r')
    f1=open('1'+f,'w')
    i=0
    while True:
        m= f2.read(1)
        if not m:
            break
        if(m==' '):
            f1.write('\t')
        elif(m=='\t'):
            f1.write('\n')
        elif(m=='\n'):
            f1.write(' ')
        elif(ord(m)>32 and ord(m)<127):
            if(i%2==0):
                if(ord(m)+k1<127):
                    f1.write(chr(ord(m)+k1))
                else:
                    f1.write(chr(ord(m)-94+k1))
            else:
                if(ord(m)-k1>32):
                    f1.write(chr(ord(m)-k1))
                else:
                    f1.write(chr(ord(m)-k1+94))
        else:
            f1.write(m)
        
        i=i+1
    f1.close()
    f2.close()
def de():
    k1=0
    i=4
    key=input("Enter key:")
    for k in key:
        k1=k1+ord(k)+i
        i=i+4
    k1=(k1*12)%93+33
    i=0
    f=input("Enter filename:")
    f2=open(f,'r')
    f1=open('1'+f,'w')
    while True:
        m= f2.read(1)
        if not m:
            break
        if(m==' '):
            f1.write('\n')
        elif(m=='\t'):
            f1.write(' ')
        elif(m=='\n'):
            f1.write('\t')
        elif(ord(m)>32 and ord(m)<127):
            if(i%2!=0):
                if(ord(m)+k1<127):
                    f1.write(chr(ord(m)+k1))
                else:
                    f1.write(chr(ord(m)-94+k1))
            else:
                if(ord(m)-k1>32):
                    f1.write(chr(ord(m)-k1))
                else:
                    f1.write(chr(ord(m)-k1+94))
        else:
            f1.write(m)
        i=i+1
    f1.close()
    f2.close()
if(op==1):
    en()
elif(op==2):
    de()
