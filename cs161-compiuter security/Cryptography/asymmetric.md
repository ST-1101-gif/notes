# <center> Asymmetric cryptography
---
$$
KeyGen()->(PK,SK)\\
Enc(M, PK)->C\\
Dec(C, SK)->M
$$
## Trapdoor One-way Functions
A **trapdoor one-way function** is a function that is one-way, but also has a special backdoor that enables someone who knows the backdoor to invert the function.
- one-way: encryption with public key
- backdoor: decryption with private key

## RSA
RSA public-key cryptosystem, named after its inventors Ronald Rivest, Adi Shamir and Leonard Adleman



RSA Hardness: 
Suppose $n = pq$, i.e. $n$ is the product of two large primes $p$ and $q$.
Given $c =m^e \pmod n$ and $e$, it is computationally hard to find $m$. However, with the factorization of $n$ (i.e. $p$ or $q$), it becomes easy to find $m$.

Let $p$ and $q$ be two large primes (typically having, say, 512 bits each), and let $N = pq$. 
Also, let $e$ be any number that is relatively prime to $(p−1)(q−1)$. (Typically $e$ is chosen to be a small value such as 3.) 

Then Bob’s public key is the pair of numbers $(N,e)$. 
The private key is the number $d$, which is the inverse of $e$ mod $(p−1)(q−1)$. (This inverse is guaranteed to exist because $e$ and $(p−1)(q−1)$ are coprime.)

encryption: $C = M^e \mod N$

decryption: $M = C^d \mod N$


deterministic, so not IND-CPA secure

**public-key padding** is a tool for mixing in some randomness so that the ciphertext output “looks random,” but can still be decrypted to retrieve the original plaintext.

>Despite the name, RSA padding modes are more similar to the IVs in block cipher modes than the padding in block cipher modes. 

One common padding scheme is **OAEP (Optimal Asymmetric Encryption Padding)**. 

- Encryption：
```
r = random()
masked_m = M XOR MGF(r)
masked_r = r XOR MGF(masked_m)
EM = masked_m||masked_r
C = RSA_Enc(EM, PK)
```
- Decryption:
```
EM = RSA_Dec(C, SK)
r = masked_r XOR MGF(masked_m)
M = masked_m XOR MGF(r)
```

## El Gamal encryption
-   **System parameters**: a 2048-bit prime $p$, and a value $g$ in the range $2 \ldots p-2$. Both are arbitrary, fixed, and public.

-   **Key generation**: Bob picks $b$ in the range $0 \ldots p-2$ randomly, and computes $B = g^{b} \bmod p$. His public key is $B$ and his private key is $b$.

-   **Encryption**: $E_{B}(m) = (g^{r} \bmod p, m \times B^{r} \bmod p)$ where $r$ is chosen randomly from $0 \ldots p-2$.

-   **Decryption**: $D_{b}(R, S) = R^{-b} \times S \bmod p$.

## Public Key Distribution
Attila the attacker could broadcast his own public key, pretending to be Bob: he could send a spoofed broadcast message that appears to be from Bob, but that contains a public key that Attila generated. 


## Session Keys
Because public key schemes are expensive and difficult to make IND-CPA secure, we tend to only use public key cryptography to distribute one or more **session keys**, which are the keys used to *actually* encrypt and authenticate the message

Often, we generate several different session keys for different purposes (MAC, encrypt...).

Alice:
generates a random set of session keys. 
encrypts the message using a symmetric algorithm with the session keys
encrypts the random session keys with Bob’s public key

Bob:
decrypts the session keys
uses the session keys to decrypt the original message.

## Digital Signature
$$
S = Sign(SK, M)\\
Verify(PK, M, S) -> true / false
$$