#!/usr/bin/env python3
import csv  # Importa o módulo csv para trabalhar com arquivos CSV

def read_employees(csv_file_location):
    # Configura um dialeto personalizado para leitura do CSV
    # skipinitialspace=True remove espaços extras, strict=True força regras de formato
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    
    # Abre e lê o arquivo CSV como um dicionário, onde a primeira linha são as chaves
    employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')
    
    # Cria uma lista vazia para armazenar os dados dos funcionários
    employee_list = []
    # Converte cada linha do CSV em um dicionário e adiciona à lista
    for data in employee_file:
        employee_list.append(dict(data))
    
    return employee_list  # Retorna lista com todos os funcionários

def process_data(employee_list):
    # Cria uma lista vazia para armazenar todos os departamentos
    department_list = []
    # Extrai o nome do departamento de cada funcionário e adiciona à lista
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    
    # Cria um dicionário vazio para contar funcionários por departamento
    department_data = {}
    # set() remove departamentos duplicados, então iteramos só os únicos
    for department_name in set(department_list):
        # Conta quantas vezes cada departamento aparece na lista
        department_data[department_name] = department_list.count(department_name)
    
    return department_data  # Retorna dicionário com contagem por departamento

def write_report(dictionary, report_file):
    # Abre arquivo para escrita (w+), cria se não existir
    with open(report_file, "w+") as f:
        # Itera pelos departamentos em ordem alfabética (sorted)
        for k in sorted(dictionary):
            # Escreve cada linha no formato "departamento:quantidade"
            f.write(str(k) + ':' + str(dictionary[k]) + '\n')
        f.close()  # Fecha o arquivo (opcional com 'with')

# Execução do programa:
# 1. Lê o arquivo CSV de funcionários
employee_list = read_employees('/home/student/data/employees.csv')
# 2. Processa os dados para contar funcionários por departamento
dictionary = process_data(employee_list)
# 3. Escreve o relatório final em um arquivo txt
write_report(dictionary, '/home/student/data/report.txt')