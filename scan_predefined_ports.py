import csv
import scanning_functions

ip_add = input('Enter analyzed IP Address: ')

try:
    with open('TCP_ports.csv', newline='', encoding='utf-8') as tcp_portlist:
        reader = csv.reader(tcp_portlist)

        for row in reader:
            print(f'{scanning_functions.tcpScanning(ip_add, int(row[1]))}, as protocol {row[0]}')

except Exception as e:
    print(f'An unexcepted error occured: {e}')
