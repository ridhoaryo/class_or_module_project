import datetime as dt
class Waktu:
    hari_bulan_dict = {
        'Monday': 'Senin',
        'Tuesday': 'Selasa',
        'Wednesday': 'Rabu',
        'Thursday': 'Kamis',
        'Friday': 'Jumat',
        'Saturday': 'Sabtu',
        'Sunday': 'Minggu',
        'January': 'Januari',
        'February': 'Selasa',
        'March': 'Rabu',
        'April': 'Kamis',
        'May': 'Jumat',
        'June': 'Sabtu',
        'July': 'Minggu',
        'August': 'Agustus',
        'September': 'September',
        'October': 'Oktober',
        'November': 'Nopember',
        'December': 'Desember'
    }
    time = dt.datetime.now()
    hari = hari_bulan_dict.get(time.strftime('%A'))
    tanggal = time.strftime('%d')
    bulan = hari_bulan_dict.get(time.strftime('%B'))
    tahun = time.strftime('%Y')
    jam = time.strftime('%H')
    menit = time.strftime('%M')
    detik = time.strftime('%S')