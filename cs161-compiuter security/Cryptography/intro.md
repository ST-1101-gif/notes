
**Confidentiality** is the property that prevents adversaries from reading our private data. The ciphertext C should give the attacker no additional information about the message M.

**Integrity** is the property that prevents adversaries from tampering with our private data.

**Authenticity** is the property that lets us determine who created a given message.

## IND-CPA Security

**indistinguishability under chosen plaintext attack (IND-CPA) game**

1. The adversary Eve chooses two different messages, $M_0$ and $M_1$, and sends both messages to Alice.

2. Alice chooses a bit $b \in \{0, 1\}$ uniformly at random, and then encrypts $M_b$. Alice sends the encrypted message $Enc(K, M_b)$ back to Eve.

3. Eve is now allowed to ask Alice for encryptions of messages of Eve’s choosing. Eve can send a plaintext message to Alice, and Alice will always send back the encryption of the message with the secret key. Eve is allowed to repeat this as many times as she wants. Intuitively, this step is allowing Eve to perform a chosen-plaintext attack in an attempt to learn something about which message was sent.

3. After Eve is finished asking for encryptions, she must guess whether the encrypted message from step 2 is the encryption of $M_0$ or $M_1$.

## Threat models
- **ciphertext-only attack**
- **known plaintext attack**
Eve has intercepted an encrypted message and also already has some partial information about the plaintext
- **replay attack** 
Eve can capture an encrypted message from Alice to Bob and re-send the encrypted message to Bob again.
- **chosen-plaintext attack**
Eve can trick Alice to encrypt arbitrary messages of Eve’s choice, for which Eve can then observe the resulting ciphertexts.
- **chosen-ciphertext attack**
Eve can trick Bob into decrypting some ciphertexts. 