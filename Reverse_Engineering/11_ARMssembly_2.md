flag: `picoCTF{ED2C0662}`

my approach to the problem:
- what the program basically does
- It takes an integer argument and stores it at [sp + 12]
- It initializes two variables, [sp + 24] and [sp + 28], to 0.
  In the loop:
  It adds 3 to [sp + 24].
  It adds 1 to [sp + 28].
- The loop continues until [sp + 28] >= argument.
- When the loop exits, it returns the value of [sp + 24], which is the accumulated result of adding 3 during each iteration of the loop.
- when w0 = 4189673334
- [sp + 28] = 4189673334.
- The number of iterations is 4189673334.
- Each iteration adds 3 to [sp + 24], so [sp + 24] will be 4189673334 * 3 = 12569020002
- convert the number to hex 32 bits and you'll get flag