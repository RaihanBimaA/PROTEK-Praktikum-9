n = int(input("berapa n ? "))
def bintang(n):
    pucuk=(n+1)/2
    x=3
    for i in range (n):
        if(i<pucuk):
            count=i+1
        else:
            count=i-x
            x=x+4
        bintang='*'*(i+count)
        print(bintang.center(15))
bintang(n)
