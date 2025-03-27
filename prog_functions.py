#import of built-in libs
import subprocess
import re

#import of local libraries
from scanning_functions import tcpScanning, udpScanning, tcpPresetScan, udpPresetScan

#function responsible for entered address validation
def validateIP(ip_address):

    #definition of pattern used to check if entered by user ip address is compatible with IP-Add format
    pattern = r"""^(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.
    (25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.
    (25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.
    (25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)$"""

    #function returns result of match operation.
    return re.match(ip_address) is not None



#function responsible for entered port validation. Requires further testing (reason-potential probems with input like 244/2)
def validatePort(port_num):
    if 0 <= int(port_num) <= 65535: return True
    else: return False



#Function responsible for entered data validation
def userDataValidation(ip_add_tuple = None, ports_tuple = None):
    #Entered IP data checking
    if ip_add_tuple == None: return True

    for i in range (0, len(ip_add_tuple)):
        #If any of entered IP is invalid - returns false and stops execution of further steps
        if ip_add_tuple[i] == False:
            return False
    
    if ports_tuple == None: return True
    
    #entered port data checking
    for i in range(0, len(ports_tuple)):
        #if any of entered ports is invalid - returns false and stops execution of further steps
        if ports_tuple[i] == False:
            return False
        
    #Otherwise, entered data meets the requirements
    return True    


############## WARNING! FUNCTION PLACED BELOW REQUIRES MORE ATTENTION #######################
#fn responsible for user data processing 
def parseInput(input_string):

    #splitting of entered data to format eg. ['scport', 'one', '192.168.1.1', '53']
    input_string = input_string.split()
    print(input_string)
    #checking if entered command represented by input string[0] is scport command (port scanning module)
    #logic of entered data is simple input_string[0] - function, other - arguments 
    if input_string[0] == 'scport':
        
        #if argument no. 1 == '/?' - we want to display prepared file which contain cheatsheet for user
        if input_string[1] == '/?':
            with open('help/scport_coms.txt', 'r') as help:
                help.read()
                print(help)

        #if 1st argument is 'one' - we want to handle one port scanning
        if input_string[1] == 'one':
            #validation of IP format and port format. 
            if userDataValidation((input_string[2]), input_string[3]) == True:
                #checking entered by user L4 protocol type and commiting scan
                #TCP scanning procedure for entered IP address and port 
                if input_string[4].upper() == "TCP":
                    tcpScanning(input_string[2], input_string[3])
                
                #UDP scanning procedure for entered IP address and port 
                elif input_string[4].upper() == "UDP":
                    udpScanning(input_string[2], input_string[3])

                #if user entered unsupported L4 transport protocol - internal error is displayed 
                else:
                   print("Inpropper name of packet/datagram type.")
            #bounded with port format validation - if entered port is out of range/entered in bad format - user gets info about that
            else: 
                print("Invalid data has been entered")

        # if 1st argument is 'range' - procedure of port range scanning is deployed
        if input_string[1] == 'range':
            #validation of IP and port format.
            if userDataValidation((input_string[2]), (input_string[3], input_string[4])) == True:    
                for i in range(int(input_string[3]), int(input_string[4])+1):
                    if input_string[5].upper() == "TCP":
                        tcpScanning(input_string[2], i)
                    elif input_string[5].upper() == "UDP":
                        udpScanning(input_string[2], i)
                    else:
                        print("Invalid L4 protocol entered (not TCP/UDP)")
            
            else:
                print("Invalid data has been entered (Address or Port)")

        if input_string[1] == 'tcp_preset':
            if userDataValidation(input_string[2]) == True:
                tcpPresetScan(input_string[2])
            else:
                print("Invalid data has been entered")

        if input_string[1] == 'udp_preset':
            if userDataValidation(input_string[2]) == True:
                udpPresetScan(input_string[2])
            else:
                print("Invalid data has been entered")

    else: print("Implosion XD")
             