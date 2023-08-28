import scapy.all as scapy
import argparse

def create_ob():
    create_obj = argparse.ArgumentParser()
    create_obj.add_argument("-r","--range",dest="prang",default="192.168.1.0/24",help="r: ip range usage: -r 192.168.1.1/24")
    pars_arg = create_obj.parse_args()
    if not pars_arg.prang:
        print("enter ip address")
    else:
        return pars_arg
def param(dstp):
    request_arp = scapy.ARP(pdst=dstp)
    broadcast_arp = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined = broadcast_arp/request_arp
    (answered_list,unanswered) = scapy.srp(combined,timeout=1)
    answered_list.summary()
a = create_ob()
try:
    param(a.prang)
except:
    pass
