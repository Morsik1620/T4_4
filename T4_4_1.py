import random
# Напишите рекурсивную функцию для вычисления факториала числа n
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


# Напишите рекурсивную функцию для вычисления суммы всех элементов в списке. Убедитесь, что у функции есть базовый случай
def sum_list(arr):
    if len(arr) == 0: # Базовый случай: Функция сначала проверяет, является ли список пустым
        return 0
    else:
        return (arr[0]+ sum_list(arr[1:]))


# Напишите рекурсивную функцию для выполнения бинарного поиска элемента в отсортированном списке. Функция должна
# возвращать индекс найденного элемента или -1, если элемент не найден
def binary_search(arr, num):
    first = 0
    last = len(arr) - 1

    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == num:
            return mid
        elif num < arr[mid]:
            last = mid - 1
        else:
            first = mid + 1

    return -1



n = 5
arr = [random.randint(0, 10) for _ in range(10)]
arr.sort()
num = arr[random.randint(0, len(arr) - 1)]  # случайный элемент из списка для поиска
print('Список с которым работаем:',arr)
print('Факториал числа n:', factorial(n))
print ('Сумма элементов списка:', sum_list(arr))
print(f'Поиск элемента {num} в отсортированном списке{arr}. Нужный нам элемент находится на {binary_search(arr, num)} позиции')

class Stack:
    def __init__(self):  # Иницилизация стека
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Стек пуст"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Стек пуст"

    def is_empty(self):
        return len(self.stack) == 0  # Проверяем длину списка

    def size(self):
        return len(self.stack)


# Пример использования
if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push('test')
    stack.push(True)
    print(stack.pop())  # Получаем самый последний элемент стека 'True' и его удаляет
    print(stack.peek())  # Получаем последний элемент стека "test" и не удаляет его
    print(stack.is_empty())  # Проверяем пуст ли стек, не пуст -> False
    print(stack.size())  # Получаем размер нашего стека
