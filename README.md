# buh-encoder
## A very dumb Python script designed for more efficient English text storage with a limited characterset.
This is intended to write to `.buh` files, but since it's just writing binary to a path, it really doesn't matter.
Text is encoded with variable length encoding, with more common letters and symbols taking up less space. This saves about 42%, but there's no support for case and there's barely any characters here. It's really only a gimmick, not very pratical.
