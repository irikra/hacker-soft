#!/bin/bash

read -p "Введите IP-адрес или имя хоста: " target

# Выполним сканирование с помощью nmap
echo "Сканируем $target с опцией --vuln"
nmap -sV --script vuln $target
