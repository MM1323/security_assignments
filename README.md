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

## Assignment 3: Web Security ##

A startup named BUNGLE! is about to launch its first product: a web search engine that accepts logins
and tracks users’ search histories. However, their investors are nervous about security problems.
Unlike the Bunglers who developed the site, you took COSC 311, so the investors have hired you to
perform a security evaluation before the site goes live to the public.

Your first task will be to attack the BUNGLE! website by exploiting three common classes of
vulnerabilities: cross-site scripting (XSS), cross-site request forgery (CSRF), and SQL injection.
You will need to exploit these vulnerabilities with various flawed defenses in place. Understanding
how these attacks work will help you better defend your own web applications.

Your second task will be to modify the source code of the BUNGLE! website to defend against
password breaches and some of the attacks you have demonstrated. Protect BUNGLE!. . . protect the
world!

## Assignment 4: Web Tracking ##

Internet tracking involves the use of many web technologies, including cookies, local data storage,
and browser fingerprinting, to build profiles of users’ Internet habits. These techniques allow data
aggregation companies to make sophisticated inferences about the interests and personalities of
individuals, even if they do not know these individuals’ exact identities.

A result of web tracking is that different people may have very different experiences on the web based
on how sites personalize content and advertising to their profiles. While occasionally convenient
(e.g. some personalized ads), this type of personalization can also cause and perpetuate biases or
create “content bubbles.”

For example, real estate sites may choose to display ads only to individuals who are inferred to be
from majority groups, online loan quotes may be cheaper for people inferred to be wealthy and
at lower risk of default, and articles about fringe theories may be more prominently displayed to
individuals who are already primed for conspiracies.

One goal of Internet privacy researchers is to measure the prevalence of web trackers and identify
especially egregious third-party tracking domains. In this assignment, you will perform these
measurement tasks to discover the scale of cookie-based web tracking.

## Assignment 5: Anonymization ##

The release of publicly available datasets is essential for public health, public policymaking,
transparent governance, and collaborative research & development. However, public datasets often
contain sensitive attributes that could cause harm if they are deanonymized to reveal the identity of
the individuals they describe.

Public datasets are often prone to deanonymization by linking multiple datasets and background
knowledge on attributes known as quasi-identifiers (QI). Naïve anonymization techniques, such as
removing names or addresses, do not account for the breadth of possible quasi-identifiers and remain
vulnerable to deanonymization. Fortunately, computer scientists have developed anonymization
algorithms that provide stronger theoretical guarantees.

In this assignment, you will gain experience with the k-anonymity, l-diversity, and t-closeness
algorithms on a public dataset.

## Assignment 6: Usable Privacy ##

Modern operating systems and software applications designed for consumer use often have a range
of customization options including extensive privacy settings. These settings ostensibly allow users
to tune their preferred tradeoff between privacy and functionality, such as by turning off voice
assistants or browsing in “incognito mode.”

However, the complexity of customization options and the sheer number of possible settings can
discourage users without sufficient time or technological expertise from effecting privacy behaviors
that match their real preferences. Additionally, the range of user interfaces across devices and
platforms challenges even experts who wish to alter default privacy options.

The field of usable privacy studies how users interact with and understand privacy features of
computer technologies. In this assignment, you will conduct a small usable privacy experiment to
measure the difficulty of adjusting privacy settings on different platforms. You will contribute your
data to a shared class dataset and generate summary figures of the type that could be included in an
academic publication.
