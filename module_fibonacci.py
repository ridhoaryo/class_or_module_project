fibonacci_list = [0,1]
for i in range(0,1000):
    fibonacci_list.append(fibonacci_list[i]+fibonacci_list[i+1])
class Fibonacci:
    def cek_fibo(self, i):
        return fibonacci_list[i]
    def is_fibo(self, i):
        if i in fibonacci_list:
            return True
        else:
            return False

fibonacci = Fibonacci()