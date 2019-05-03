'''
=========================================================================
Soal 1 - Fungsi Pangkat
=========================================================================
'''
def pangkat(angka, level):
    hasil = 1
    for x in range(level):
        hasil *= angka
    return hasil

print(pangkat(2,2))
print(pangkat(3,3))
print(pangkat(10,5))
