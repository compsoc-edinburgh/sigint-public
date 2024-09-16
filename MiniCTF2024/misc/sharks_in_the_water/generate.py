import socket, random
from scapy.all import *
from scapy.layers.inet import *

FLAG = "minictf{unl1k3_b335_y0u_c4n_f1nd_5h4rk5_1n_70rn4d05}"

if __name__ == "__main__":
    with open("story.txt", "r") as f:
        data = f.read()
    data = data.replace("FLAG", FLAG)
    
    packets = []
    for char in data:
        ip_layer = IP(dst="localhost")
        packet = ip_layer/TCP(dport=1337)/Raw(load=char)
        packets.append(packet)

    wrpcap("dump.pcap", packets)
            