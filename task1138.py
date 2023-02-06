# Задана последовательность натуральных чисел, завершающаяся числом 0. Требуется определить значение второго 
# по величине элемента в этой последовательности, то есть элемента, который будет наибольшим, 
# если из последовательности удалить наибольший элемент.

# 1 7 9 0	 -> 7
# 1 2 3 4 5 6 7 0 8 9 10	-> 6

numbers = input("Введите список чисел: ").split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
for i in range(len(numbers)):
    if numbers[i] == 0:
        zero = i
        break

largest = 0
second_large = 0
for i in range(len(numbers[:zero])):
    if numbers[i] > largest:
        second_large = largest
        largest = numbers[i]
        
print(second_large)
