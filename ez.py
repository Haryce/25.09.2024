def bubble_sort(arr): #функция для сортировки бузырьком
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr): #функция для быстрой сортировки
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def insertion_sort(arr): #функция для сортировки вставками
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Ввод элементов массива
arr = []
print("Введите 10 элементов массива:")
for i in range(10):
    num = int(input(f"Элемент {i+1}: "))
    arr.append(num)

# Выбор способа сортировки
print("Выберите сортировку:")
print("1. Пузырьковая сортировка")
print("2. Быстрая cортировка ")
print("3. Сортировка вставками")

choice = input("Введите номер сортировки (1/2/3): ")

if choice == '1':
    bubble_sort(arr)
elif choice == '2':
    quick_sort(arr)
elif choice == '3':
    insertion_sort(arr)
else:
    print("Неверный выбор!")
    exit() #завершает программу если выбор неверный


print("Отсортированный массив:", arr) # Вывод отсортированного массива
