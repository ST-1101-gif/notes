
# Regular Expression
debugger
<https://regex101.com/r/qqbZqh/2>

toturial
<https://regexone.com/problem/matching_html>


Regular expressions are extremely useful in extracting information from text such as code, log files, spreadsheets, or even documents. 

## Metacharacters

`abc…`	Letters
`123…`	Digits

`\d`	Any Digit
`\D`	Any Non-digit character

`.`	Any Character --> (escape) `\.`	Period


`[abc]`	Only a, b, or c
`[^abc]`	Not a, b, nor c
`[a-z]`	Characters a to z
`[0-9]`	Numbers 0 to 9
`[^n-p]`  character except for letters n to p

`\w`	Any Alphanumeric character
equivalent to the character range [A-Za-z0-9_]
  
`\W`	Any Non-alphanumeric character

`\b` the boundary between a word and a non-word character. 
- It's most useful in capturing entire words (for example by using the pattern \w+\b)

`{m}`	m Repetitions
`{m,n}`	m to n Repetitions
- a{3}
- [^1-9]{2,6}
- .{1,3}

`*`	Zero or more repetitions
`+`	One or more repetitions
- .*
- aa+b*c+
- (,\d+)*
  
`*` and `+` are, by default, "greedy". They will match as much text as they can. 
- ^.*:
<u>ab:cde</u>:f

`?`	Optional character --> (escape) `\?` Question mark
-  ab?c : match either the strings "abc" or "ac" because the b is considered optional

`\s`	Any Whitespace
>The most common forms of whitespace you will use with regular expressions are the space (`␣`), the tab (`\t`), the new line (`\n`) and the carriage return (`\r`) (useful in Windows environments), and these special characters match each of their respective whitespaces. In addition, a whitespace special character `\s` will match any of the specific whitespaces above and is extremely useful when dealing with raw input text.
`\S`	Any Non-whitespace character


It is often best practice to *write as specific regular expressions as possible* to ensure that we don't get false positives when matching against real world text.
e.g. We wanted to match the word "success" in a log file. We certainly don't want that pattern to match a line that says "Error: unsuccessful operation"!
`^…$`	Starts and ends
- ^succuss
  
Note that this is different than the hat used inside a set of bracket [^...] for excluding characters

Regular expressions allow us to not just match text but also to extract information for further processing. 
`(…)`	Capture Group
- ^(IMG\d+\.png)$ captures and extracts the full filename
- ^(IMG\d+)\.png$ captures the part before the period.


`(a(bc))`	Capture Sub-group
- ^(IMG(\d+))\.png$
  
Generally, the results of the captured groups are in the order in which they are defined (in order by open parenthesis).


`(.*)`	Capture all


Specifically when using groups, you can use the `|` (logical OR, aka. the pipe) to denote different possible sets of characters.
`(abc|def)`	Matches abc or def

**back referencing**
Many systems allow you to reference your captured groups by using \0 (usually the full matched text), \1 (group 1), \2 (group 2), etc.

## Examples
Matching decimal numbers

3.14529
-255.34	
128	
1.9e10	
123,340.00
```
^-?\d+(,\d+)*(\.\d+(e\d+)?)?$
```
Matching phone numbers

Task	Text	Capture Groups	 
capture	415-555-1234	415	 
capture	650-555-2345	650	 
capture	(416)555-3456	416 
capture	202 555 4567	202	 
capture	4035555678	403	 
capture	1 416 555 9292	416
```
1?[\s-]?\(?(\d{3})\)?[\s-]?\d{3}[\s-]?\d{4}
```

Matching emails

Task	Text	Capture Groups	 
capture	tom@hogwarts.com	tom	 
capture	tom.riddle@hogwarts.com	tom.riddle	 
capture	tom.riddle+regexone@hogwarts.com	tom.riddle	 
capture	tom@hogwarts.eu.com	tom	 
capture	potter@hogwarts.com	potter	 
capture	harry@hogwarts.com	harry	 
capture	hermione+regexone@hogwarts.com	hermione

```
^([\w\.]*)
```
It will match up to the point in the text where it reaches an '@' or '+'.