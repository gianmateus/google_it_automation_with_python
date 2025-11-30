guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")
    
guests.close()

# with open("guests.txt") as guests:
#     for line in guests:
#         print(line)

new_guest = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "a") as guests:
    for i in new_guest:
        guests.write(i + "\n")

guests.close()

# with open("guests.txt") as guests:
#     for line in guests:
#         print(line)

# Abra o arquivo no modo “leitura”.
# Itere cada linha do arquivo e coloque o nome de cada hóspede em uma lista Python.
# Abra o arquivo novamente no modo “gravação”.
# Adicione o nome de cada hóspede da lista Python ao arquivo, um por um.

guests = open("guests.txt", "r")
guest_list = []
for line in guests:
    guest_list.append(line.strip())

guests.close()

guests = open("guests.txt", "w")
for guest in guest_list:
    guests.write(guest + "\n")

guests.close()

checked_out = ["Andrea", "Manuel", "Khalid"]
temp_list = []

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

with open("guests.txt") as guests:
    for line in guests:
        print(line)

guests_to_check = ["Bob", "Andrea"]
checked_in = []

with open("guests.txt", "r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print(f"{check} is checked in.")
        else:
            print(f"{check} is not checked in.")