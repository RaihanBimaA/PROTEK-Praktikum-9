mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

listBaruMhs = []

for i in range(len(mhs)) :
    nama = mhs[i].split(':')
    listBaruMhs.append(nama)

    tanggal = listBaruMhs[i][2].split('-')
    tanggal.reverse()
    
    tglJoined = '/'.join(tanggal)
    listBaruMhs[i][2] = tglJoined


print('=' * 75)
print('NIM'.ljust(10), 'NAMA MAHASISWA'.ljust(25), 'TGL LAHIR'.ljust(25), 'TEMPAT LAHIR'.ljust(10))
print('-' * 75)

for i in range(len(listBaruMhs)) :
    print(listBaruMhs[i][0].ljust(10), listBaruMhs[i][1].ljust(25), listBaruMhs[i][2].ljust(25), listBaruMhs[i][3].ljust(10))
