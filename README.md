# x64_FSBSolver
for CTF Pwner :)

# Usage

 `git clone https://github.com/Py0zz1/x64_FSBSolver.git`
  
  `cd ./x64_FSBSolver`
  
  `cp ./x64fsb [Your Workspace]`
 
 
 And Just `import x64fsb`
 
# Example
exit_got = 0x601020

helper = 0x4050a0

taintable_offset = 6

## exp_6(offset, value, address)
This function is used when writing 6 bytes.

`payload = x64fsb.exp_6(6, 0x4050a0, 0x601020)`

**Meaning: I will write 0x4050a0(helper) 6bytes to 0x601020(exit_got).**

Payload Length Too long.
## exp_4(offset, value, address) & exp_4L(offset, value, address)
This function is used when writing 4 bytes.

`payload = x64fsb.exp_4(6, 0x4050a0, 0x601020)`

**Meaning: Write 0x4050a0(helper) to 0x601020(exit_got) using the format string %hn.**

`payload = x64fsb.exp_4L(6, 0x4050a0, 0x601020)`

**Meaning: Write 0x4050a0(helper) to 0x601020(exit_got) using the format string %n.**

With exp_4L(), the length of the payload is relatively short.

## exp_2(offset, value, address)
This function is used when writing 2 bytes.

`payload = x64fsb.exp_2(6, 0x50a0, 0x601020)`

**Meaning: I will write 0x4050a0(helper) 2bytes to 0x601020(exit_got).**

Payload Length Too short.
# Contact
Email: peeper830@gmail.com

Blog: [py0zz1.tistory.com](https://py0zz1.tistory.com)

