class Student:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia
        

student_data = [
    {'nama': 'Andi', 'usia': 21},
    {'nama': 'Budi', 'usia': 22},
    {'nama': 'Caca', 'usia': 23},
    {'nama': 'Deni', 'usia': 24},
]

for data in student_data:
    print(data)
    nama = data['nama']
    usia = data['usia']
    vars()[nama] = Student(nama, usia)
    #vars() mengambil value untuk dijadikan variable
    
print(Andi.nama, Andi.usia)
print(Budi.nama, Budi.usia)
print(Caca.nama, Caca.usia)
print(Deni.nama, Deni.usia)