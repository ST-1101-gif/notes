# <center> Cryptographic Hashes
---
A cryptographic hash function is a function,$H$ , that when applied on a message,$M$ , can be used to generate a fixed-length “fingerprint” of the message.

## Properties

deterministic 

unkeyed

Avalanche effect: a small change in the input causes a significant and unpredictable change in the output hash value.



- One-way / Preimage resistant: given a hash output $y$, it's infeasible to find any $x$ such that $H(x) = y$

- Second preimage resistant: Given an input $x$, it's infeasible to find another input $x'$ such that $H(x) = H(x')$

- Collision resistant: It's infeasible to find any pair of messagess $x,x'$ such that $H(x) = H(x')$

>infeasible: there is no known way to accomplish it with any realistic amount of computing power


Under certain threat models, hash functions can be used to verify message integrity. 
