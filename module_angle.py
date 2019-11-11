
import math

class Angle():
    def trigono(self, a, b):
        sisi_a = a
        sisi_b = b
        sudut_c = 0
        sudut_a = 90

        sudut_b = math.degrees(math.asin(math.sin((math.sin(sudut_a)*sisi_b)/sisi_a)))

        sudut_c = 180-(sudut_b+sudut_a)
        return f'sudut AB = {sudut_c}'

angle = Angle()