import random

def shuffleString(teks, n) :
    
    hasil = []
    txt=list(teks)
    for i in range(n) :
        acak =random.sample(teks, len(teks))
        joined = ''.join(acak)
        
        if(joined in hasil) :
            continue
        else :
            hasil.append(joined)
            print(joined)


teks = input("Masukkan teks yang ingin anda acak : ")
n = int(input("Berapa banyak hasil acakan yang anda mau ? "))

shuffleString(teks,n)

    
