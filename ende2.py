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
    print("File encrypted in ",'encrypted'+f)
    fu='encrypted'+f
    os.system('cat %s'%fu)
    print('\n')
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
    print("File encrypted in ",'decrypted'+f)
    fu='decrypted'+f
    os.system('cat %s'%fu)
    print('\n')
op=int(input("1.Encrypt  2.Decrypt \n"))
if(op==1):
    en(key,f)
elif(op==2):
    de(key,f)
