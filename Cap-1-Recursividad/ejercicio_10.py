import math

def invertir(n=1023):
    
    if n<=1 and n>=-1:
        return n
    
    if n<0:
        return -1*(abs(n)%10 * 10 ** math.trunc(math.log10(abs(n)))) +  invertir(math.trunc(n/10))

    return n%10 * 10 ** math.trunc(math.log10(n)) +  invertir(n//10) 

print(invertir(123456789))