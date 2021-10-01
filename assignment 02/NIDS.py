import csv
import matplotlib.pyplot as plt
from collections import defaultdict
from TestNIDS import *


def parse_netflow():
    """Use Python's built-in csv library to parse netflow.csv and return a list
       of dictionaries. The csv library documentation is here:
       https://docs.python.org/3/library/csv.html"""
    with open('netflow.csv', 'r') as netflow_file:
        netflow_reader = csv.DictReader(netflow_file)
        netflow_data = list(netflow_reader)
        return netflow_data


def is_internal_IP(ip):
    """Return True if the argument IP address is within campus network"""
    s = ip.split('.')
    if s[0] == "128" and s[1] == "112":
        return True
    return False


def plot_bro(num_blocked_hosts):
    """Plot the list of the number of Bro blocked hosts indexed by T"""
    fig = plt.figure(figsize=(16,8))
    plt.plot(range(len(num_blocked_hosts)), num_blocked_hosts, linewidth=3)
    plt.xlabel("Threshold", fontsize=16)
    plt.ylabel("Number of Blocked Hosts", fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.title("Sensitivity of Bro Detection Algorithm", fontsize=16)
    plt.grid()
    plt.savefig("sensitivity_curve.png")


def detect_syn_scan(netflow_data):
    tcpCount = 0
    synFlag = 0
    extra = 0
    for item in netflow_data:
        if (item.get("Protocol") == "TCP"):
            tcpCount += 1
            if(item.get("Flags") == "....S."):
                synFlag += 1
            else:
                extra+= 1
    
    percent_synonly = (synFlag/tcpCount)*100 

    # Do not change this print statement
    print("\nPercent SYN-only flows: {} -> {}\n".format(
        percent_synonly, test_percent_synonly(percent_synonly)))


def detect_portscan(netflow_data):

    synonly_knownbad = []           # default value
    synonly_NOTknownbad = []        # default value
    other_knownbad = []             # default value      
    other_NOTknownbad = []          # default value
    tcpCount = 0

    for item in netflow_data:
        if (item.get("Protocol") == "TCP"):
            tcpCount+= 1
            if (item.get("Flags") == "....S." or item.get("Flags") == "...RS."):
                if (item.get("Dst port") == "135" or item.get("Dst port") == "139" or item.get("Dst port") == "445" or item.get("Dst port") == "1433"):
                    synonly_knownbad.append(item)
                else:
                    synonly_NOTknownbad.append(item)
            else:
                if (item.get("Dst port") == "135" or item.get("Dst port") == "139" or item.get("Dst port") == "445" or item.get("Dst port") == "1433"):
                    other_knownbad.append(item)
                else:
                    other_NOTknownbad.append(item)

    percent_knownbad = (len(synonly_knownbad) + len(other_knownbad))/ (tcpCount) * 100 
    percent_synonly_knownbad = len(synonly_knownbad) / (len(synonly_knownbad) + len(other_knownbad)) * 100
    percent_synonly_NOTknownbad = len(synonly_NOTknownbad) / (len(synonly_NOTknownbad) + len(other_NOTknownbad)) * 100 
                         
    # Do not change these statements
    print("Precent of TCP flows to known bad ports: {} -> {}".format(
        percent_knownbad, test_percent_knownbad(percent_knownbad)))
    print("Percent of SYN-only TCP flows to known bad ports: {} -> {}".format(
        percent_synonly_knownbad, test_percent_synonly_knownbad(percent_synonly_knownbad)))
    print("Percent of SYN-only TCP flows to other ports: {} -> {}\n".format(
        percent_synonly_NOTknownbad, test_percent_synonly_NOTknownbad(percent_synonly_NOTknownbad)))
    return synonly_knownbad, synonly_NOTknownbad, other_knownbad, other_NOTknownbad


def detect_malicious_hosts(netflow_data, synonly_knownbad, synonly_NOTknownbad, 
                           other_knownbad, other_NOTknownbad):
    
    maliciousIP = set()
    benign_IP = set()
    questionable = set()
    
    for item in synonly_knownbad:
         if (not is_internal_IP(item.get("Src IP addr"))):
             maliciousIP.add(item.get("Src IP addr"))
    
    for item in synonly_NOTknownbad:
         if (not is_internal_IP(item.get("Src IP addr"))):
             maliciousIP.add(item.get("Src IP addr"))

    for item in other_knownbad:
         if (not is_internal_IP(item.get("Src IP addr"))):
             maliciousIP.add(item.get("Src IP addr"))

    for item in other_NOTknownbad:
         if (not is_internal_IP(item.get("Src IP addr"))):
             benign_IP.add(item.get("Src IP addr"))

    num_malicious_hosts = len(maliciousIP)
    num_benign_hosts =  len(benign_IP)
            
    for ip in maliciousIP:
        if ip in benign_IP:
            questionable.add(ip)
    
    for ip in questionable:
            maliciousIP.remove(ip)
            benign_IP.remove(ip)

    num_questionable_hosts = len(questionable)  
    num_malicious_hosts = len(maliciousIP)
    num_benign_hosts = len(benign_IP)

    # Do not change these print statements
    print("Number of malicious hosts: {} -> {}".format(
        num_malicious_hosts, test_num_malicious_hosts(num_malicious_hosts)))
    print("Number of benign hosts: {} -> {}".format(
        num_benign_hosts, test_num_benign_hosts(num_benign_hosts)))
    print("Number of questionable hosts: {} -> {}\n".format(
        num_questionable_hosts, test_num_questionable_hosts(num_questionable_hosts)))


class Bro:
    """TODO: complete this class to implement the Bro algorithm"""
    
    def __init__(self, threshold):
        # self.T is the threshold number of unique destination addresses from
        #     successful and/or failed connection attempts (depending on port)
        #     before a host is marked as malicious
        self.T = threshold
        
        # self.good_services is the list of port numbers to which successful connections 
        #     (SYN and ACK) should not be counted against the sender
        self.good_services = [80, 22, 23, 25, 113, 20, 70]

        # You may add additional class fields and/or helper methods here

    def run(self, netflow_data):
        """TODO: Run the Bro algorithm on netflow_data, returning a 
                 set of blocked hosts. You may add additional helper methods 
                 or fields to the Bro class"""
        blocked_hosts = set()
        hosts = dict()
        # list of intern that its trying tonssend to 
        
        #externa ip: [internal ip]

        for flow in netflow_data: # loop simulates an "online" algorithm 
            ip = flow.get("Src IP addr")
            val = flow.get("Dst IP addr")
            if (not is_internal_IP(ip)) and (flow.get("Protocol") == "TCP"):    
                if float(flow.get("Dst port")) in self.good_services: 
                    flag = flow.get("Flags")
                    if (not ("A" in flag)) and (not ("S" in flag)):
                        if not(ip in hosts):
                            hosts[ip] = set(val)
                        else:
                            hosts[ip].add(val)
                            if len(hosts.get(ip)) > self.T:
                                blocked_hosts.add(ip)
                else:
                    flag = flow.get("Flags")
                    if ("S" in flag):
                        if not(ip in hosts):
                                hosts[ip] = set(val)
                        else:
                            hosts[ip].add(val)
                            if len(hosts.get(ip)) > self.T:
                                blocked_hosts.add(ip)
       

        # Do not change this return statement
        return blocked_hosts


def main():
    """Run all functions"""
    netflow_data = parse_netflow()
    detect_syn_scan(netflow_data)
    portscan_flows = detect_portscan(netflow_data)
    detect_malicious_hosts(netflow_data, *portscan_flows)
    num_blocked_hosts = [len(Bro(T).run(netflow_data)) for T in range(1, 121)]
    plot_bro(num_blocked_hosts)
    print("Bro sensitivity curve plotted")


if __name__=="__main__":
    main()
