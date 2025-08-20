# <center> Vim
---
## Philosophy
- Vim is a modal editor: it has different modes for inserting text vs manipulating text. 
- Vim is programmable (with Vimscript and also other languages like Python)
- Vim's interface itself is a programming language: keystrokes (with mnemonic names) are commands, and these commands are composable. 
- Vim avoids the use of the mouse
- Vim even avoids using the arrow keys
## Modal editing
- **Normal**: for moving around a file and making edits
  - `<ESC>`
- **Insert**: for inserting text
  - `i`
- **Replace**: for replacing text
  - `R`
- **Visual** for selecting blocks of text
  - Visual mode： `v`
  - Visual Line mode: `V`
  - Visual Block mode: `^V`
- **Command-line**: for running a command
  - `:`
  
## Buffers, tabs, and windows

Vim maintains a set of open files, called "**buffers**". 
A Vim session has a number of **tabs**, each of which has a number of **windows** (split panes). Each window shows a single **buffer**. 
A given buffer may be open in multiple windows, even within the same tab. (unlike other programs)

## Command Line
- `:q` quit (close window)
- `:w` save ("write")
- `:wq` save and quit
- `:e {name of file}` open file for editing
- `:ls` show open buffers
- `:help {topic}` open help
    - `:help :w` opens help for the `:w` command
    - `:help w` opens help for the `w` movement


## Vim's interface is a programming language

### Movement
*Normal Mode*

Movements in Vim are also called "**nouns**", because they refer to chunks of text.

- Basic movement: `hjkl` (left, down, up, right)
- Words: `w` (next word), `b` (beginning of word), `e` (end of word)
- Lines: `0` (beginning of line), `^` (first non-blank character), `$` (end of line)
- Screen: `H` (top of screen), `M` (middle of screen), `L` (bottom of screen)
- Scroll: `Ctrl-u` (up), `Ctrl-d` (down)
- File: `gg` (beginning of file), `G` (end of file)
- Line numbers: `:{number}<CR>` or `{number}G` 
- Misc: `%` (corresponding item)
- Find: `f{character}`, `t{character}`, `F{character}`, `T{character}`
    - find/to forward/backward {character} on the current line
    - `,` / `;` for navigating matches
- Search: `/{regex}`, `n` / `N` for navigating matches
## Selection
*Visual Mode*
- Visual mode： `v`
- Visual Line mode: `V`
- Visual Block mode: `^V`
  
Can use movement keys to make selection.

## Edit
Vim's editing commands are also called "**verbs**", because verbs act on nouns.
- `i` enter Insert mode
    - but for manipulating/deleting text, want to use something more than
    backspace
- `o` / `O` insert line below / above
- `d{motion}` delete {motion}
    - e.g. `dw` is delete word, `d$` is delete to end of line, `d0` is delete
    to beginning of line
- `c{motion}` change {motion}
    - e.g. `cw` is change word
    - like `d{motion}` followed by `i`
- `x` delete character (equal to `dl`)
- `s` substitute character (equal to `cl`)
- Visual mode + manipulation
    - select text, `d` to delete it or `c` to change it
- `u` to undo, `<C-r>` to redo
- `y` to copy / "yank" (some other commands like `d` also copy)
- `p` to paste
- Lots more to learn: e.g. `~` flips the case of a character

## Count

- `5j` move 5 lines down
- `7dw` delete 7 words
- `c2w` change 2 words
  
## Modifiers
- `i`: in
- `a`: around

examples:

- `ci(` change the contents inside the current pair of parentheses
- `ci[` change the contents inside the current pair of square brackets
- `da'` delete a single-quoted string, including the surrounding single quotes
  
## Customizing Vim