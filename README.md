# buh-encoder
## A very dumb Python script designed for more efficient English text storage with a limited characterset.
This is intended to write to `.buh` files, but since it's just writing binary to a path, it really doesn't matter.
Text is encoded with variable length encoding, with more common letters and symbols taking up less space. This saves about 42%, but there's no support for case and there's barely any characters here. It's really only a gimmick, not very pratical.

### Encoding Table
| Byte Sequence | Character |
| ------------- | --------- |
| 0 | (space) |
| 1 | E |
| 2 | T |
| 3 | A |
| 4 | O |
| 5 | I |
| 6 | N |
| 7 | S |
| 8 | R |
| 9 | H |
| a | D |
| b | L |
| c | U |
| d | C |
| e | M |
| f0 | F |
| f1 | Y |
| f2 | W |
| f3 | G |
| f4 | P |
| f5 | B |
| f6 | V |
| f7 | K |
| f8 | X |
| f9 | Q |
| fa | J |
| fb | Z |
| fc | . |
| fd | , |
| fe | ' |
| rest of table is | unfinished|
| ff0 | (space) |
| ff1 |
| ff2 |
| ff3 |
| ff4 |
| ff5 |
| ff6 |
| ff7 |
| ff8 |
| ff9 |
| ffa |
| ffb |
| ffc |
| ffd |
| ffe |
