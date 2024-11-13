## arm Assembly 1
flag: `picoCTF{0000001b}`
my approach to the problem
- basically what the code does is func subtracts w0  from 27, the program will print "You win!" if the input is 27 (because 27 - 27 = 0), and "You Lose :(" for any other input.
- so hex of 27 is 0000001b with 32 chars