class ReverseCase:
    def reverse(self, a_list):
        y = list(a_list)
        new_list = []
        for char in y:
            if char.isupper() == True:
                new_list.append(char.lower())
            else:
                new_list.append(char.upper())
        new_list = ''.join(new_list)
        return new_list

reversecase = ReverseCase()