import time
import requests
import nmap
import subprocess
import random
import socket

# banner
def print_banner(text: str) -> None:
    text_length = len(text)
    banner_width = text_length + 4 
    print("+" + "-" * banner_width + "+")
    print("| " + " " * text_length + "   |")
    print("| " + text + "   |")
    print("| " + " " * text_length + "   |")
    print("+" + "-" * banner_width + "+")

def dos():



# Вывод статистики
print(f"Отправлено {num_syns} SYN-пакетов")
print(f"Время выполнения: {end_time - start_time} секунд")


# nmap full scan
def nmap_full():
    target = input("IP цели= ")
    print("Выполнение полного сканирования Nmap...")
    subprocess.run(["nmap", "-A", target], check=True)

# nmap full+ vulns scan
def nmap_vulns():
    target = input("IP цели= ")
    print("Выполнение сканирования Nmap с поиском уязвимостей...")
    # Здесь используется опция -sV для определения версии сервиса и --script vuln для поиска уязвимостей
    subprocess.run(["nmap", "-A", "-sV", "--script", "vuln", target], check=True)

# Добавляем вывод результатов в функцию nmap_full
def nmap_full():
    target = input("IP цели= ")
    print("Выполнение полного сканирования Nmap, это займет около 5 минут")
    result = subprocess.run(["nmap", "-A", target], check=True, text=True, capture_output=True)
    print(result.stdout)  # Выводим стандартный вывод nmap
    if result.stderr:
        print("Ошибка:", result.stderr)  # Выводим стандартный поток ошибок, если есть ошибки

# Добавляем вывод результатов в функцию nmap_vulns
def nmap_vulns():
    target = input("IP цели= ")
    print("Выполнение сканирования Nmap с поиском уязвимостей, это займет около 8 минут")
    result = subprocess.run(["nmap", "-A", "-sV", "--script", "vuln", target], check=True, text=True, capture_output=True)
    print(result.stdout)  # Выводим стандартный вывод nmap
    if result.stderr:
        print("Ошибка:", result.stderr)  # Выводим стандартный поток ошибок, если есть ошибки


print_banner("KIRIKRA")

print('ФУНКЦИИ')
print('1-dos')
print('2-nmap scan')
print('3-nmap vuln scan')
print('')
print('')


choice = int(input('Выбери функции '))


if choice == 1:
    dos()
elif choice == 2:
    nmap_full()
elif choice == 3:
    nmap_vulns()
