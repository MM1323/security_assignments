# security_assignments


## Assignment 1: Secure Messaging ##

This project is due on September 17, 2021 at 5 pm. You may work with a partner on this assignment
and submit one project per team.

Secure messaging is essential to trusting any Internet communications, but it is not limited to
commercial messaging apps or code written by professionals.
For this assignment, you will be creating a secure 2-way messaging application using cryptographic
primitives. At the end of the assignment, you will have a Python application that will enable you
to exchange secure messages with anyone else in the class. No one else will be able to read these
messages (not Colgate ITS, your ISP, other people on the same WiFi network, tech companies, etc.),
and you will able to detect any unauthorized message modifications.
It is a bad idea to write your own cryptograhy primitives unless you are an expert ("Don’t roll
your own crypto!"), so you will be using the publicly available Python libraries PyCryptodome and
pyDH.

## Assignment 2: Network Intrusion Detection ##

Network operators actively monitor their networks to protect against various intrusion attacks.
Network attackers often perform random "portscans" of IP addresses to find vulnerable machines.
Network Intrusion Detection Systems (NIDS) attempt to detect and flag such behavior as malicious.
In this assignment, you will analyze NetFlow network measurement data from a campus border
router to identify potentially malicious traffic sent to the campus network. You will then simulate
an online algorithm for identifying malicious remote hosts.

### Objectives ###
• Gain familiarity with network measurement data
• Implement basic approaches for identifying malicious traffic
• Reason about the network security threats faced by universities