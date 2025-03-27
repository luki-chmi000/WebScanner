import subprocess

nav_elements = ['1. Skan jednego portu', '2. Skan zakresu portów', '3. Skan podstawowych portów TCP',
                '4. Skan podstawowych portów UDP', '9. Wyjście']

mainloop = True

while mainloop:

    # Generacja listy w menu nawigacyjnym z wyżej zdefiniowanej listy
    for nav_element in nav_elements:
        print(f'{nav_element} \n')

    nav_variable = input('Wybierz metodę skanowania: ')

    if nav_variable == '1':
        subprocess.run(['python', 'scan_one_port.py'])
    elif nav_variable == '2':
        subprocess.run(['python', 'scan_port_range.py'])
    elif nav_variable == '3':
        subprocess.run(['python', 'scan_tcp_ports.py'])
    elif nav_variable == '4':
        subprocess.run(['python', 'scan_udp_ports.py'])
    elif nav_variable == '9':
        mainloop = False

