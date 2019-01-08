import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="put your filename here",type=str)
parser.add_argument("key", help="put your key here",type=str)
args = parser.parse_args()
f=args.filename
key=args.key
def en(key,f):
    k1=0
    i=4
    k=list(key)
    f2=open(f,'r')
    f=f.replace('decrypted','')
    f1=open('encrypted'+f,'w')
    i=0
    while True:
        k1=ord(k[i%(len(k))])
        m= f2.read(1)
        if not m:
            break
        if(m==' '):
            f1.write('\t')
        elif(m=='\t'):
            f1.write('\n')
        elif(m=='\n'):
            f1.write(' ')
        elif(ord(m)>32):
            if(i%2==0):
                if(ord(m)+k1<127):
                    f1.write(chr(ord(m)+k1))
                else:
                    k5=ord(m)+k1-94
                    while(k5>=127):
                        k5=k5-94
                    f1.write(chr(k5))
            else:
                if(ord(m)-k1>32):
                    f1.write(chr(ord(m)-k1))
                else:
                    k5=ord(m)-k1+94
                    while(k5<=32):
                        k5=k5+94
                    f1.write(chr(k5))
        else:
            f.write(m)
        i=i+1
    f1.close()
    f2.close()
    fu='encrypted'+f
    os.system('cat %s'%fu)
    print('\n')
    print("File encrypted in ",fu)
def de(key,f):
    k1=0
    i=4
    i=0
    k=list(key)
    f2=open(f,'r')
    f=f.replace('encrypted','')
    f1=open('decrypted'+f,'w')
    while True:
        k1=ord(k[i%(len(k))])
        m= f2.read(1)
        if not m:
            break
        if(m==' '):
            f1.write('\n')
        elif(m=='\t'):
            f1.write(' ')
        elif(m=='\n'):
            f1.write('\t')
        elif(ord(m)>32):
            if(i%2!=0):
                if(ord(m)+k1<127):
                    f1.write(chr(ord(m)+k1))
                else:
                    k5=ord(m)+k1-94
                    while(k5>=127):
                        k5=k5-94
                    f1.write(chr(k5))
            else:
                if(ord(m)-k1>32):
                    f1.write(chr(ord(m)-k1))
                else:
                    k5=ord(m)-k1+94
                    while(k5<=32):
                        k5=k5+94
                    f1.write(chr(k5))
        else:
            f1.write(m)
        i=i+1
    f1.close()
    f2.close()
    fu='decrypted'+f
    os.system('cat %s'%fu)
    print('\n')
    print("File encrypted in ",fu)
op=int(input("1.Encrypt  2.Decrypt \n"))
if(op==1):
    en(key,f)
elif(op==2):
    de(key,f)
