import scanning_functions

ip_add = input('Enter IP address of analyzed host')
port = int(input('Enter value of analyzed port'))
prot_type = input('Enter type of L4 protocol (TCP/UDP)')


try:
    if prot_type.upper() == 'TCP':
        print(scanning_functions.tcpScanning(ip_add, port))

    elif prot_type.upper() == 'UDP':
        print(scanning_functions.udpScanning(ip_add, port))

except Exception as e:
    print(f'An unexcepted error occured: {e}')


