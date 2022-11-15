#https://www.codewars.com/kata/5286b2e162056fd0cb000c20

def collatz(n):
    alist=[str(n)]
    while n!=1:
        if n%2==0:
            n=n/2
        else:
            n=(n*3)+1
        alist.append(str(int(n)))
    return "->".join(alist)