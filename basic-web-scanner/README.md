# basic-web-scanner
 Basic (but constantly developed) web scanner for private purposes.

 These app pretends to be second nmap, but for now it has fraction of functionalities of original.

 These app is still under construction so probability of unexpected errors and code implosions is pretty high.

 Best way to start this aplication (in alpha version) is using the ,,Python FIle in Dedicated Terminal" commited at main.py file (if you`re using MS Visual Studio). Most important thing to run these app properly is to run main.py file.

 Version a_280325 provides only one function:
 scport {mode} {ip_address} {port_1} {port_2} {L4_protocol}
 Where:
 -mode: one (scanning one port), range (scanning range of ports), tcp_preset (scan of predefined tcp ports), udp_preset (scan of predefined udp ports)
 -port_2 argument is used only in range scanning mode. It designates upper limit of scanning ports
 -l4_protocol argument is used to choose type of data sended to selected port (TCP/UDP)

Examples of usage scport command:
-scport one 127.0.0.1 21 TCP - scanning port 21 TCP (FTP) at localhost
-scport range 127.0.0.1 1 20 UDP - scanning ports from 1 to 20, sending to them UDP datagrams
-scport tcp_preset 127.0.0.1 - scanning ports at localhost with use predefined list of TCP ports
-scport udp_preset 127.0.0.1 - scanning ports at localhost with use predefined list of UDP ports

CAUTION
At the moment these app is able to search for now opened ports. Opening ports functionality is under construction
Scaning bigger amount of ports is pretty slow. Threaded scan is also under construction
