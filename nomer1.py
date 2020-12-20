teks=input('masukkan teksnya!')
a=input('huruf apa yang diubah?')
b=input('diubah ke huruf apa?')
def ubahHuruf(teks,a,b):
    txtDiinginkan= teks.replace(a,b)
    print(txtDiinginkan)
def gantiHuruf(teks,a,b):
    listTeks=list(teks)
    for i in range(len(listTeks)):
        if(listTeks[i]==a):
            listTeks[i]=b
        else:
            continue
    hasil= ''.join(listTeks)
    print(hasil)
ubahHuruf(teks,a,b)
gantiHuruf(teks,a,b)
