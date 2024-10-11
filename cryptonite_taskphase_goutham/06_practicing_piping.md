# Task-phase writeup

## Challenge-1 Name: Redirecting output
- outputs can be redirected using > char
- solution: `echo PWN > COLLEGE`

## Challenge-2 Name: Redirecting more output
- output from any command can bre redirected
- solution:  `/challenge/run > myflag` [this will redirect the output to the myflag file]
- then `cat myflag` to read the myflag file for the flag

## Challenge-3 Name: Appending output
- using `>>` appends the output
- solution: `/challenge/run >> /home/hacker/the-flag` , this appends the part of the flag to the-flag file and the second half to stdout
- then `echo stdout >> /home/hacker/the-flag` to append the rest of the flag to the-flag file
- `cat /home/hacker/the-flag` to get the flag

## Challenge-4 Name: Redirecting errors
- file Descriptor numbers: it is a number the describes a communication channel in Linux.
- solution: run `/challenge/run > myflag 2> instructions` to redirect the outut to myflag and errors to instructions
- `cat myflag` to get the flag 
 
## Challenge-5 Name: Redirecting inputs
- <  is used to redirect inputs
- solution: run `echo COLLEGE > PWN` this wil redirect COLLEGE to PWN
- `/challenge/run < PWN` to get the flag

## Challenge-6 Name: Grepping stored results
- grep: used to search for specific patterns in files and input streams
- solution: `/challenge/run > /tmp/data.txt` [ to redirect the output ]
- `grep "pwn.college{" /tmp/data.txt` to get the flag

## Challenge-7 Name: Grepping live results
- | operator: Standard output from the command to the left of the pipe will be connected to (piped into) the standard input of the command to the right of the pipe.
- run `/challenge/run | grep pwn.college{` to get the flag

## Challenge-8 Name: Grepping errors
 - >& : redirects a file descriptor to another file descriptor
 - solution:  `/challenge/run 2>& 1 | grep pwn.college{`
 
## Challenge-9 Name: Duplicating piped data with tee
- tee: uplicates data flowing through your pipes to any number of files provided on the command line
- solution: `touch random` to store the data.
- `/challenge/pwn | tee random | /challenge/college` data gets intercepted
- `cat random` which tells us to `/challenge/pwn --secret` to get the flag [secret arg is provided]

  
