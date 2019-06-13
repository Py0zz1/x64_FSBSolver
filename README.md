# x64_FSBSolver
for CTF Pwner :)

# Example
exit_got = 0x601020

helper = 0x4050a0

taintable_offset = 6

### exp_6(offset, value, address)
---
This function is used when writing 6 bytes.

`payload = exp_6(6, 0x4050a0, 0x601020)`

**Meaning: I will write 0x4050a0 (helper) 6 bytes to 0x601020 (exit_got).**

### exp_4(offset, value, address) & exp_4L(offset, value, address)
---
This function is used when writing 4 bytes.

`payload = exp_4(6, 0x4050a0, 0x601020)`

**Meaning: Write 0x4050a0 (helper) to 0x601020 (exit_got) using the format string %hn.**

`payload = exp_4L(6, 0x4050a0, 0x601020)`

**Meaning: Write 0x4050a0 (helper) to 0x601020 (exit_got) using the format string %n.**

The length is relatively short.

### exp_2(offset, value, address)
---
This function is used when writing 2 bytes.

`payload = exp_2(6, 0x4050a0, 0x601020)`

**Meaning: I will write 0x4050a0 (helper) 6 bytes to 0x601020 (exit_got).**




