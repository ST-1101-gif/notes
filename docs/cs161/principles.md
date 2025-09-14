# <center> Security Principles 
---
## Threat Model
A threat model is a model of who your attacker is and what resources they have.
Understanding your threat model has to do with understanding who and why might someone attack you

common assumptions
## Consider Human Factors
Security systems must be usable by ordinary people, and therefore must be designed to take into account the role that humans will play. 
## Detect

## Defense in depth
Multiple types of defenses should be layered together so an attacker would have to breach all the defenses to successfully attack a system.
## Least Privilege
Try to minimize how much privilege you give each program and system component.
## Seperation of responsipility
Split up privilege, so no one person or program has complete power. Require more than one party to approve before access is granted.
## Ensure complete mediation
When enforcing access control policies, make sure that you check every access to every object.

> Time-Of-Check To Time-Of-Use (TOCTTOU) vulnerability
## Shannon's Maxim
Shannon’s Maxim states that the attacker knows the system that they are attacking.

“**Security through obscurity**” refers to systems that rely on the secrecy of their design, algorithms, or source code to be secure.

A closely related principle is **Kerckhoff’s Principle**, which states that cryptographic systems should remain secure even when the attacker knows all internal details of the system.
## Fail-Safe Defaults
Choose default settings that “fail safe”, balancing security with usability when a system goes down.
## Trusted Computing Base (TCB)