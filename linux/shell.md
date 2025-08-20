# <center> CLI
---

## Terminal

"end point of a railway line," 1888, from terminal (adj.); sense of "device for communicating with a computer" is first recorded 1954. Earlier "final part of a word" (1831).

## the Shell

## Environment Variable

## Shell Command

`chmod` - change file mode bits

symbolic representation: [ugoa...][[-+=][perms...]...]

- `ugoa` controls which users' access to the file will be changed
  - `u`: user / owner
  - `g`: group
  - `o`: others
  - `a`: all (default)
- `perms` is either zero or more letters from the set `rwxXst`, or a single letter from the set `ugo`.
- `rwxXst`: read (r), write (w), execute (or  search  for directories)  (x),  execute/search  only if the file is a directory or already has execute permission for some user (X), set user or group ID on execution (s), restricted deletion flag or sticky bit (t)

octal number representation
derived by adding up the bits with values 4 (read), 2 (write), and 1 (execute)
- The first digit selects the set user ID (4) and set group ID (2) and restricted deletion or sticky (1) attributes.  
- The second: owner
- The third: group
- The fourth: other users 

`chown` - change file owner and group
```sh
chown [OPTION]... [OWNER][:[GROUP]] FILE...
```
If a colon but  no  group name follows the user name, that user is made the owner of the files and the group of the files is changed to that user's login group.

---

`nc` — arbitrary TCP and UDP connections and listens
The nc (or netcat) utility is used for just about anything under the sun involving TCP, UDP, or UNIX-domain sockets.

CLIENT/SERVER MODEL
On one console, start nc listening on a specific port for a connection.  
```sh
$ nc -l 1234
```
On a second console (or a second machine), connect to the machine and port being listened on:
```sh
$ nc -N 127.0.0.1 1234  # -N: shutdown(2) the network socket after EOF on the input.
```
There should now be a connection between the ports.  Anything typed at the second console will be concatenated to the first, and vice-versa.  
After the connection has been set up, nc does not really care which side is being
used as a ‘server’ and which side is being used as a ‘client’. 

DATA TRANSFER

Start by using nc to listen on a specific port, with output captured into a file:
```sh
$ nc -l 1234 > filename.out
```
Using a second machine, connect to the listening nc process, feeding it the file which is to be transferred:
```sh
$ nc -N host.example.com 1234 < filename.in
```
After the file has been transferred, the connection will close automatically.

TALKING TO SERVERS

For example, to retrieve the home page of a web site:
```sh
$ printf "GET / HTTP/1.0\r\n\r\n" | nc host.example.com 80
```

PORT SCANNING

```sh
$ nc -zv host.example.com 20-30
Connection to host.example.com 22 port [tcp/ssh] succeeded!
Connection to host.example.com 25 port [tcp/smtp] succeeded!
```

---


---

As we covered in the lecture find's -exec can be very powerful for performing operations over the files we are searching for. However, what if we want to do something with all the files, like creating a zip file? As you have seen so far commands will take input from both arguments and STDIN. When piping commands, we are connecting STDOUT to STDIN, but some commands like tar take inputs from arguments. To bridge this disconnect there's the xargs command which will execute a command using STDIN as arguments. For example ls | xargs rm will delete the files in the current directory.

finds all HTML files in the folder and makes a zip with them
```sh
find . -type f -name "*.html" | xargs -d '\n' tar -cvzf archive.tar.gz 
```
### Globbing
- Wildcards
  - `*`: expand 0 or more characers
  - `?`: expand exactly 1 character
- Curly braces `{}`
  
```sh
convert image.{png,jpg}
# Will expand to
convert image.png image.jpg

cp /path/to/project/{foo,bar,baz}.sh /newpath
# Will expand to
cp /path/to/project/foo.sh /path/to/project/bar.sh /path/to/project/baz.sh /newpath

# Globbing techniques can also be combined
mv *{.py,.sh} folder
# Will move all *.py and *.sh files


mkdir foo bar
# This creates files foo/a, foo/b, ... foo/h, bar/a, bar/b, ... bar/h
touch {foo,bar}/{a..h}
touch foo/x bar/y
# Show differences between files in foo and bar
diff <(ls foo) <(ls bar)
# Outputs
# < x
# ---
# > y
```

## Shell Function
Functions are executed in the current shell environment. Thus, they can modify environment variables.

```sh
mcd () {
    mkdir -p "$1"
    cd "$1"
    export VAR=$(pwd)   # export environment variable
}
```
## Script

### Shebang
The **​​shebang​​** (#!) is a special sequence at the ​​beginning of a script file​​ that tells the system which interpreter (program) should be used to execute the script.
```sh
#!/bin/bash
```
use the `env` command that will resolve to wherever the command lives in the system, increasing the portability of scripts
```sh
#!/usr/bin/env python
```

### Special Characters
- `$0` - Name of the script
- `$1` to `$9` - Arguments to the script. `$1` is the first argument and so on.
- `$@` - All the arguments
- `$#` - Number of arguments
- `$?` - **Return code** of the previous command
- `$$` - Process identification number (PID) for the current script
- `!!` - Entire last command, including arguments. 
  A common pattern: `sudo !!`
- `$_` - Last argument from the last command. If you are in an interactive shell, you can also quickly get this value by typing `Esc` followed by `.` or `Alt+.`

### Return Code
The **return code** or **exit status** is the way scripts/commands have to communicate how execution went.
A value of 0 usually means everything went OK; anything different from 0 means an error occurred.

Exit codes can be used to conditionally execute commands using `&&` and `||`. 
Commands can also be separated within the same line using a semicolon `;`.
```sh
false || echo "Oops, fail"
# Oops, fail

true || echo "Will not be printed"
#

true && echo "Things went well"
# Things went well

false && echo "Will not be printed"
#

true ; echo "This will always run"
# This will always run

false ; echo "This will always run"
# This will always run
```
### Command Substitution
Whenever you place `$( CMD )` it will execute `CMD`, get the output of the command and substitute it in place

### Control Flow
```sh
#!/bin/bash

echo "Starting program at $(date)" # Date will be substituted

echo "Running program $0 with $# arguments with pid $$"

for file in "$@"; do
    grep foobar "$file" > /dev/null 2> /dev/null
    # When pattern is not found, grep has exit status 1
    # We redirect STDOUT and STDERR to a null register since we do not care about them
    if [[ $? -ne 0 ]]; then
        echo "File $file does not have any foobar, adding one"
        echo "# foobar" >> "$file"
    fi
done
```

### Execute

```sh
chmod +x example.sh
./example.sh [param]
```

```sh
sh example.sh [param]
```
## shell functions vs. scripts

- Functions have to be in the same language as the shell, while scripts can be written in any language. This is why including a shebang for scripts is important.
- Functions are loaded once when their definition is read. Scripts are loaded every time they are executed. This makes functions slightly faster to load, but whenever you change them you will have to reload their definition.
- Functions are executed in the current shell environment whereas scripts execute in their own process. Thus, functions can modify environment variables, e.g. change your current directory, whereas scripts can't. Environment variables which have been exported using `export` are passed by value to scripts.
- As with any programming language, functions are a powerful construct to achieve modularity, code reuse, and clarity of shell code. Often shell scripts will include their own function definitions.

## Job Control
Shell is using a UNIX communication mechanism called a **signal** to communicate information to the process
When a process receives a signal it stops its execution, deals with the signal and potentially changes the flow of execution based on the information that the signal delivered. For this reason, signals are **software interrupts**.