import numpy as np

# membuat papan catur 8x8 tanpa ratu
# jika 0 maka tidak ada ratu
# Jika 1 maka ada ratu

langkah = 0

def Cek(catur, baris, kolom):
    #mengecek apakah baris terdapat ratu
    for i in range(0, 8):
        if catur[baris][i] == 1:
            return False

    temp = 0

    #mengecek apakah diagonal terdapat ratu
    while temp < 8:
        if  baris - temp > -1 and kolom - temp > -1 and catur[baris - temp][kolom - temp] == 1 or \
            baris - temp > -1 and kolom + temp <  8 and catur[baris - temp][kolom + temp] == 1 or \
            baris + temp <  8 and kolom - temp > -1 and catur[baris + temp][kolom - temp] == 1 or \
            baris + temp <  8 and kolom + temp <  8 and catur[baris + temp][kolom + temp] == 1:
            return False

        temp += 1
    
    return True


def dfs(catur, curr_kolom):
    global langkah
    
    if curr_kolom > 7:
        return

    for row in range(0,8):
        langkah += 1
                
        #menghapus baris sebelumnya
        dlt = row
        while dlt > -1:
            catur[dlt][curr_kolom] = 0
            dlt -= 1

        #mengeprint banyak langkah dan hasi akhir papan catur
        if Cek(catur, row, curr_kolom):
            catur[row][curr_kolom] = 1
            if curr_kolom == 7:
                print ('langkah:', langkah)
                print (catur)

            dfs (catur, curr_kolom + 1)


if __name__ == "__main__":
    #membuat papan catur kosong
    catur = np.full((8,8),0)

    #memasukan fungsi satu per satu
    dfs(catur, 0)