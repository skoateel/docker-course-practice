import time
import multiprocessing

def cpu_intensive_task():
    """Функция, создающая нагрузку на CPU."""
    start_time = time.time()
    # Бесконечный цикл для загрузки CPU
    while True:
        # Вычисляем много чисел Фибоначчи
        fibonacci(35)
        
        # Каждые 10 секунд выводим статистику
        current_time = time.time()
        if current_time - start_time > 10:
            print(f"[{time.strftime('%H:%M:%S')}] Still working...")
            start_time = current_time

def fibonacci(n):
    """Рекурсивное вычисление числа Фибоначчи (намеренно неэффективное)."""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    print(f"[{time.strftime('%H:%M:%S')}] Starting CPU stress test...")
    
    # Количество процессов (можно настроить)
    num_processes = 2
    
    # Создаем и запускаем процессы
    processes = []
    for _ in range(num_processes):
        p = multiprocessing.Process(target=cpu_intensive_task)
        p.start()
        processes.append(p)
    
    # Ждем завершения всех процессов (не произойдет, так как они бесконечные)
    for p in processes:
        p.join()
