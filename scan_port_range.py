import scanning_functions

ip_add = input('Enter Host IP-Address: ')
start_port = int(input('Enter first port: '))
end_port = int(input('Enter last port: '))
prot_type = input('Enter L4 protocol type: ')

try:
    if prot_type.upper() == 'TCP':
        for port in range(start_port, end_port + 1):
            scanning_functions.tcpScanning(ip_add, port)

    elif prot_type.upper() == 'UDP':
        for port in range(start_port, end_port + 1):
            scanning_functions.udpScanning(ip_add, port)

except Exception as e:
    print(e)



