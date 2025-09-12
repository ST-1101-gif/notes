# Filters
## Capture Filters
BPF (Berkeley Packet Filter)​​ Syntax
```
[Protocol][Direction][Host/Net]
```
Protocol​: ether, ip, ip6, arp, tcp, udp, icmp
Direction: src / dst
Host / Net: host 192.168.1.1, net 192.168.1.0/24, port 80, portrange 1-1024

Logical Operations​: and (&&), or (||), not (!)

## Display Filters
Wireshark Syntax

Port Filter
```
tcp.port==80
tcp.dstport==80
tcp.srcport==80
```

Protocol Filter
```
http
tcp
ssh
```

http Filter
```
http.request.method=="GET"
```
