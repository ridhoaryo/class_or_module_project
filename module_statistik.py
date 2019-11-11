class Statistic:
    def get_mean(self, num_list):
        hasil = 0
        for i in num_list:
            hasil += i
        return hasil / len(num_list)
    
    def get_median(self, num_list):
        num_list.sort()
        middle = len(num_list) % 2
        index_middle = len(num_list) // 2
        if middle == 1:
            return num_list[index_middle]
        else:
            return (num_list[index_middle-1]+num_list[index_middle])/2
        
    def get_modus(self, num_list):
        hasil_jumlah = 0
        angka = 0
        for i in num_list:
            jumlah_angka_saat_ini = num_list.count(i)
            if hasil_jumlah > jumlah_angka_saat_ini:
                continue
            elif hasil_jumlah < jumlah_angka_saat_ini:
                hasil_jumlah = jumlah_angka_saat_ini
                angka = i
        return angka

stat = Statistic()