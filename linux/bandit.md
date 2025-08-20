# level0
```sh
cat readme
```
ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

# level1
weird file name
```sh
cat ~/-
```
263JGJPfgU6LtdEvgfWU1XP5yac29mFx

# level2
space in file name
```sh
cat ~/--spaces\ in\ this\ filename--
```
MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

# level3
dot in file name 
```sh
cd inhere
ls -a 
cat ./...Hiding-From-You
```
2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

# level4
file information
```sh
file ./*
cat ./-file07
```
4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

# level5
file filter
```sh
cd inhere
find . -type f -size 1033c
cat maybehere07/.file2
```
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

# level6
file filter
```sh
find / -type f -size 33c -user bandit7 -group bandit6 | grep password
cat /var/lib/dpkg/info/bandit7.password
```
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

# level7
```sh
cat data.txt | grep millionth
```
dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

# level8
```sh
sort data.txt | uniq -u
```
4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

# lebel9
`strings` - print the sequences of printable characters in files
```sh
strings data.txt
```
FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey



# level10
base64
```sh
base64 -d data.txt
```
dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

# level11
Rot13
`tr`: translate or delete characters


```sh
cat data.txt | tr "a-zA-Z" "n-za-mN-ZA-M"
```
7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4



# level12
- hexdump
`xxd`: make a hex dump or do the reverse

- file compression
  - `gzip` 
  - `bzip2`
  - `tar`
  - ...
```sh
xxd -r data.txt
file data.txt   # gzip
mv data.txt data.gz
gzip -d data.gz
file data.out   # bzip2
mv data.out data.bz2
bzip2 -d data.bz2
file data   # POSIX tar archive (GNU)
mv data data.tar
tar -xf data.tar 
...
```
FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn

# level13
`ssh -i`: identity_file
Selects a file from which the identity (private key) for public key authentication is read.
```sh
ssh -i ./sshkey.private bandit14@localhost -p 2220
cat /etc/bandit_pass/bandit14
```
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS

# level14
`nc`: arbitrary TCP and UDP connections and listens
```sh
nc localhost 30000
```
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo

# level15
`openssl`: OpenSSL command line program
>OpenSSL is a cryptography toolkit implementing the Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1) network protocols and related cryptography standards required by them.
The openssl program is a command line program for using the various cryptography functions of OpenSSL's crypto library from the shell.  It can be used for
>>o  Creation and management of private keys, public keys and parameters
o  Public key cryptographic operations
o  Creation of X.509 certificates, CSRs and CRLs
o  Calculation of Message Digests and Message Authentication Codes
o  Encryption and Decryption with Ciphers
o  SSL/TLS Client and Server Tests
o  Handling of S/MIME signed or encrypted mail
o  Timestamp requests, generation and verification

```sh
openssl s_client -connect localhost:30001
```
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx

# level16
`nmap`: Network exploration tool and security / **port scanner**
`ncat`: Concatenate and redirect sockets
```sh
nmap -sV localhost -p 31000-32000
# several open ports, 2 ssl 
ncat --ssl localhost 31790
# submit password -> private key in /tmp/key/private.key
ssh -i /tmp/key/private.key bandit17@localhost -p 2220
```

# level17
`diff`: compare files line by line
```sh
diff passwords.new passwords.old
```
x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO

# level18
executing commands remotely
```sh
ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat ./readme"
```
cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8

# level19
setuid: set user ID
```sh
./bandit20-do cat /etc/bandit_pass/bandit20
```
0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO

# level20
`nc -l`: Listen for an incoming connection
```sh
echo "0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO" | nc -l 1234 &
# echo: send to pipe immediately, but not send to the port until connected
# listen on local port 1234
./suconnect 1234
# connect local port 1234 
```
EeoULMCra2q0dSkYj561DX7s1CpBuOBt

# level21
`cron`: daemon to execute scheduled commands

```sh
ls /etc/cron.d
cat cronjob_bandit22
cat ...
```
tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q

# level22
```sh
cat cronjob_bandit23
# #!/bin/bash

# myname=$(whoami)
# mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

# echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

# cat /etc/bandit_pass/$myname > /tmp/$mytarget
echo I am uer bandit23 | md5sum | sut -d ' ' -f 1
# 8ca319486bfbbc3663ea0fbe81326349
cat /tmp/8ca319486bfbbc3663ea0fbe81326349
```
0Zf11ioIjMVN551jX3CmStKLYqjk54Ga

# level23
```sh
$ cat cronjob_bandit24
$ cat /usr/bin/cronjob_bandit24.sh
```
```sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname/foo
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done
```
```sh
$ vim /tmp/getpassword.sh
```
```sh
#!/bin/bash 

cat /etc/bandit_pass/bandit24 > /tmp/pw.txt
```
```sh
$ chmod +x  /tmp/getpassword.sh
$ cp /tmp/getpassword.sh /var/spool/bandit24/foo
$ cat /tmp/pw.txt
```
gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8

# level24
boom
```sh
#!/bin/bash

for i in {0000..9999}
do
        echo gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 $i >> possibilities.txt
done

cat possibilities.txt | nc localhost 30002 > result.txt
```
```sh
$ cat result.txt | grep -v Wrong    # -v: invert matching 
```
iCi86ttT4KSNe1armKiwbQNmB3YJP3q4

# level25
`/etc/passwd`: stores the basic information of all users
```sh
$ cat /etc/passwd | grep bandit26   # check shell
bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
# user name:password:uid:gid:comment:home directory:shell
$ cat /usr/bin/showtext
#!/bin/sh
 
export TERM=linux
 
more ~/text.txt # we should stop here
exit 0  # !!!
$
```
`more`:  file perusal filter for crt viewing
hidden feature: type `v` will call the defualt editor 

```sh
# first shrink the terminal interface
$ ssh -i ./bandit26.sshkey bandit26@localhost -p 2220
# page viewing, type v
:set shell=/bin/bash    # command mode
:shell  # call shell (bash)
cat /etc/bandit_pass/bandit26
```
s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ

# level26
```sh
./bandit27-do cat /etc/bandit_pass/bandit27
```
upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB

# level27
```sh
git clone ssh://bandit27-git@localhost/home/bandit27-git/repo
```
Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN

# level28
version
```sh
mkdir /tmp/git-bandit28
cd /tmp/git-bandit28
git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo # add port!
cat README.md
# password: xxxxx
git log
# versions shown
git checkout 68314e012fbaa192abfc9b78ac369c82b75fab8f
cat README.md
```
4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7

# level29
branch
```sh
git branch -a
git checkout dev
cat README.md
```
qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL

# level30
tag
```sh
git tag
git show secret
```
fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy

# level31
add -> commit -> push
```sh
echo "May I come in?" > key.txt
git add -f key.txt
git commit -m "key"
git push origin master
```
3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K

# level32
`$0` - Name of the script
```sh
# UPPER SHELL
$0
cat /etc/bandit_pass/bandit33
```
tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0