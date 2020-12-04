class Mun:
    def function(self, num1, num2):
        my_list = []
        for even_number in range(num1, num2+1):
            if even_number % 2 == 0:
                my_list.append(even_number)
        retunr my_list
