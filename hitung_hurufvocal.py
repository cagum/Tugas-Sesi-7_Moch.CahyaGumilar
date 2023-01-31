# Menghitung huruf vokal dan konsonan
kata = input('Ketikkan kata : ')
panjang_kata = len(kata)
i = 0
jml_vocal = 0
jml_konsonan = 0

while i < panjang_kata:
    if(kata[i] == 'a' or kata[i] == 'A' or kata[i] == 'i' or kata[i] == 'U' or kata[i] == 'e' or kata[i] == 'E' or kata[i] == 'O' or kata[i] == 'o'):
        jml_vocal += 1
    else:
        jml_konsonan += 1
    i += 1
print('Jumlah huruf vocal pada kalimat = ',jml_vocal)
print('Jumlah huruf konsonan pada kalimat ',jml_konsonan)

