#!/bin/bash

read -p "Введи IP-адрес или имя хоста: " target

# Выполним сканирование с помощью nmap
echo "Сканирую $target с опцией -sV..."
nmap -sV $target
