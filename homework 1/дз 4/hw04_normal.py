# Иванов М.

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    def e_fibonacci(num):
        if (num == 1) | (num == 2):
            return 1
        else:
            return e_fibonacci(num - 1) + e_fibonacci(num - 2)
    ser = []
    if m < n :
        pass
    elif m == n :
        ser.append(elem_fibonacci(n))
    else:
        ser.append(e_fibonacci(n))
        ser.append(e_fibonacci(n+1))
        counter = m - n - 1
        idx = 2
        while counter > 0:
            ser.append(ser[idx-1] + ser[idx-2])
            counter -= 1
            idx += 1
    return ser
print(fibonacci(3,9))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin):
    n = 1 
    length_array = len(origin)
    while n < length_array:
        for i in range(length_array-n):
            if origin[i] > origin[i+1]:   
                origin[i], origin[i+1] = origin[i+1], origin[i]
        n += 1

a = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
sort_to_max(a)
print(a) 



# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(lambda_f, array):
    result = []
    for a in array:
        if lambda_f(a):
            result.append(a)
    return result

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

A1 = [1,1]
A2 = [2,2]
A3 = [3,3]
A4 = [4,4]

def is_paral(A1,A2,A3,A4):
    A1A2 = [A2[0]-A1[0],A2[1]-A1[1]]
    A3A4 = [A4[0]-A3[0],A4[1]-A3[1]]
    A1A4 = [A4[0]-A1[0],A4[1]-A1[1]]
    A2A3 = [A3[0]-A2[0],A3[1]-A2[1]]
    if ((A1A2[0]*A3A4[1]-A1A2[1]*A3A4[0]) == 0 ) & ((A1A4[0]*A2A3[1]-A1A4[1]*A2A3[0]) == 0 ):
        return True
    else:
        return False

print(is_paral(A1,A2,A3,A4))
