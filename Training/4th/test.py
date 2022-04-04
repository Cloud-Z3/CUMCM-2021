from time import *
def fastpow(a,n):
    mul=1
    while(n!=0):
        if n&1==1:
            mul*=a
        n=n>>1
        a=a**2
    return mul
n=3000000
t1=time()
print(fastpow(2,n))
t2=time()
print(2**n)
t3=time()
print(2<<(n-1))
t4=time()

print(t2-t1,t3-t2,t4-t3)