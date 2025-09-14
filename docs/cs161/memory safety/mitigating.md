# <center> Mitigating Memory-Safety Vulnerabilities
---

## Address Space Layout Randomization (ASLR)
With ASLR, each time the program is run, the beginning of each section of memory is randomly chosen. Also, if the program imports libraries, we can also randomize the starting addresses of each library’s source code.

There are some constraints to randomizing the sections of memory. For example, segments usually need to start at a page boundary. In other words, the starting address of reach section of memoy needs to be a multiple of the page size (typically 4096 bytes in a 32-bit architecture).
