import socket
import csv

def tcpScanning(ip_add, port):
    tmp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tmp_socket.settimeout(1)
    result = tmp_socket.connect_ex((ip_add, int(port)))
    if result == 0:
        print(f'[+] TCP {port}')
    else:
        print(f'[-] TCP {port}')

    tmp_socket.close()
    
def udpScanning(ip_add, port):

    tmp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tmp_socket_param = (ip_add, int(port))
    tmp_socket.settimeout(1)
    tmp_socket.sendto(b'0x00', tmp_socket_param)
    try:
        data, add = tmp_socket.recvfrom(1024)
        if data:
            print(f'[+] UDP {port}')

        else:
            print(f'[-] UDP {port}')

    except socket.timeout:
        print(f'[-] UDP {port} - {socket.timeout}')

    tmp_socket.close()

def tcpPresetScan(ip_add):
    try:
        with open('scanning_assets/TCP_ports.csv', newline='', encoding='utf-8') as tcp_portlist:
            reader = csv.reader(tcp_portlist)

            for row in reader:
                print(f'{tcpScanning(ip_add, int(row[1]))}, as L4 protocol {row[0]}')

    except Exception as e:
        print(f'An unexcepted error occured: {e}')


def udpPresetScan(ip_add):
    try:
        with open('scanning_assets/UDP_ports.csv', newline='', encoding='utf-8') as udp_portlist:
            reader = csv.reader(udp_portlist)

            for row in reader:
                print(f'{udpScanning(ip_add, int(row[1]))}, as protocol {row[0]}')

    except Exception as e:
        print(f'An unexcepted error occured: {e}')