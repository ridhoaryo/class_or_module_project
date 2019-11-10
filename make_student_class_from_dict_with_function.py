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

def create_obj(x):
    nama = x['nama']
    vars()[nama] = Student(x['nama'], x['usia'])
    return vars()[nama]

data_new_func = list(map(create_obj, student_data))
print(data_new_func[0].nama)
print(data_new_func[0].usia)
print(data_new_func[1].nama)
print(data_new_func[1].usia)
print(data_new_func[2].nama)
print(data_new_func[2].usia)