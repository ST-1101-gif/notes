
# Layers of Internet
## Layer 1: Physical Layer
In the Internet, we’re looking for a way to signal bits (1s and 0s) across space. 
The technology could be voltages on an electrical wire, wireless radio waves, light pulses along optical fiber cables, among others.

## Layer 2: Link Layer
In the Internet, a **link** connects two machines. That link could be using any sort of technology (wired, wireless, optical fiber, etc.). If we use links to connect up a bunch of nearby computers, we get a **local area network (LAN)**.

At Layer 2, we can also group bits into units of data called **packets** (or **frames** at this layer), and define where a packet starts and ends in the physical signal. We can also handle problems like multiple people simultaneously using the same wire to send data.

## Layer 3: Internet Layer
In the Internet, the post office receiving and redirecting mail is called a **switch** or **router**.

If we build additional links between switches, we can connect up local networks. With enough links and local networks, we can connect everybody in the world, resulting in the **Internet**.

On the Internet, the operators are **Internet service providers**, who own and operate Internet structure.

### Network of Networks
![](picture/internet.png)
In the Internet, **end hosts** are machines (e.g. servers, laptops, phones) communicating over the Internet. By contrast, a **switch** (also called a **router**) is a machine that isn’t sending or receiving its own data, but exists to help the end hosts communicate with each other. 

### Best-Effort Service Model
service model: a contract between the network and users, describing what the network does and doesn’t support.
The designers of the Internet didn’t support any of those models. Instead, the Internet only supports **best effort** delivery of data.
If you send data over Layer 3, the Internet will try its best to deliver it, but there is no guarantee that the data will be delivered. The Internet also won’t tell you whether or not the delivery succeeded.

### Packets Abstraction
Packets are limited in size. If the application has some large data to send (e.g. a video), we need to somehow split up that data into packets, and send each packet through the network independently.

## Layer 4: Transport
This layer uses Layer 3 as a building block, and implements an additional **protocol** for re-sending lost packets, splitting data into packets, and reordering packets that arrive out-of-order (among other features).

The transport layer protocol allows us to stop thinking in terms of packets, and start thinking in terms of **flows**, streams of packets that are exchanged between two endpoints.

## Layer 7: Application
The Internet’s design allows it to be a general-purpose communication network for any type of application data.


Each layer relies on services from the layer directly below, and provides services to the layer directly above.
Two layers interact directly through the interface between them.