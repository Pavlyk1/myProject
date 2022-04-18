


cryptos="abcdefghijklmnopqrstuvwxyz"
def encrypt(test,key):
    resoult=""
    for i in test:
        k=cryptos.index(i)
        A=k+key
        if A> len(cryptos):
            A=A-len(cryptos)
       # print(i,cryptos[A])
        resoult=resoult+cryptos[A]
    return resoult
def decrypt (text,k):
    resoult=""
    for i in text:
        b=cryptos.index(i)
        a=b-k
        if a<0:
            a=a+len(cryptos)
        resoult=resoult+cryptos[a]
    return resoult

    