class Tortuga:
    def counting_sort(self, arr, exp):
        n = len(arr)
        output = [0] * n  # Arreglo temporal para la salida ordenada
        count = [0] * 10  # Arreglo de conteo para los dígitos (0 a 9)

        # Contar las ocurrencias de cada dígito en la posición actual
        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1

        # Acumular el conteo para que 'count' refleje las posiciones finales
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Construir el array de salida
        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        # Copiar el array de salida al array original, para reflejar el orden parcial
        for i in range(n):
            arr[i] = output[i]

    def radix_sort(self, arr):
        # Encontrar el número máximo para saber el número de dígitos
        max_val = max(arr)
        exp = 1
        paso = 1
        print("\nEjecutando Radix Sort:")

        while max_val // exp > 0:
            print(f"\nPaso {paso}: Ordenando por el dígito en la posición {exp}")
            self.counting_sort(arr, exp)
            print(f"Estado del arreglo después de ordenar por el dígito en la posición {exp}: {arr}")
            exp *= 10
            paso += 1

        print("\nArray ordenado con Radix Sort:", arr)

    def heapify_min(self, arr, n, i):
        smallest = i      
        left = 2 * i + 1  
        right = 2 * i + 2 

        if left < n and arr[left] < arr[smallest]:
            smallest = left

        if right < n and arr[right] < arr[smallest]:
            smallest = right

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]  
            print(f"Intercambio: {arr}") 
            self.heapify_min(arr, n, smallest)  

    def heapsort_descendente(self, arr):
        n = len(arr)
        print("\nEjecutando Heap Sort (Descendente):")
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_min(arr, n, i)
            print(f"Construcción del heap mínimo: {arr}")

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i] 
            print(f"Intercambio de la raíz con el último elemento: {arr}")
            self.heapify_min(arr, i, 0)
        
        arr.reverse()
        print(f"\nArray ordenado con Heap Sort (Descendente): {arr}")

    def shell_sort(self, arr):
        n = len(arr)
        gap = n // 2
        print("\nEjecutando Shell Sort:")
        while gap > 0:
            print(f"\nReducción del intervalo a: {gap}")
            for i in range(gap, n):
                temp = arr[i]
                j = i
                print(f"\nPosición inicial: arr[{i}] = {arr[i]}")
                
                while j >= gap and arr[j - gap] > temp:
                    print(f"  Cambio: arr[{j}] = arr[{j - gap}] -> {arr[j - gap]} reemplaza {arr[j]}")
                    arr[j] = arr[j - gap]
                    j -= gap
                
                arr[j] = temp
                print(f"  Estado del arreglo después del paso: {arr}")
            
            gap //= 2  # Reducimos el intervalo a la mitad

        print(f"\nArray ordenado con Shell Sort: {arr}")

    def Arreglo(self):
        arr = []
        Limite = int(input("\nDame el tamaño del arreglo: "))
        for _ in range(Limite):
            Num = int(input("Ingresa un número: "))
            arr.append(Num)
        return arr

# Función principal
def main():
    key = Tortuga()
    arr = key.Arreglo()
    print("\nArreglo inicial:", arr)

    while True:
        print("\nMenú de métodos de ordenamiento:")
        print("1. Quicksort")
        print("2. Radix Sort")
        print("3. Heap Sort (Descendente)")
        print("4. Shell Sort")
        print("5. Salir")
        
        opcion = input("Elige el número del método que deseas usar: ")
        
        if opcion == '1':
            print("\nEjecutando Quicksort:")
            quicksort(arr)
            print("Array ordenado con Quicksort:", arr)
        
        elif opcion == '2':
            key.radix_sort(arr)
        
        elif opcion == '3':
            key.heapsort_descendente(arr)
        
        elif opcion == '4':
            key.shell_sort(arr)
        
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida, por favor selecciona una opción válida.")

# Función Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(f"Ordenando con pivote {pivot}: {arr}")
    print(f"Menores que {pivot}: {left}")
    print(f"Iguales a {pivot}: {middle}")
    print(f"Mayores que {pivot}: {right}")
    return quicksort(left) + middle + quicksort(right)

# Ejecutar el programa
if __name__ == "__main__":
    main()
