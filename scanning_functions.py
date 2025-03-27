import socket

def tcpScanning(ip_add, port):
    tmp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tmp_socket.settimeout(1)
    result = tmp_socket.connect_ex((ip_add, port))
    tmp_socket.close()

    if result == 0:
        return f'[+] TCP {port}'
    else:
        return f'[-] TCP {port}'

def udpScanning(ip_add, port):

    tmp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tmp_socket_param = (ip_add, port)
    tmp_socket.settimeout(1)
    tmp_socket.sendto(b'0x00', tmp_socket_param)

    try:
        data, add = tmp_socket.recvfrom(1024)
        if data:
            return f'[+] UDP {port}'

        else:
            return f'[-] UDP {port}'

    except socket.timeout:
        return f'[-] UDP {port} - {socket.timeout}'


    tmp_socket.close()