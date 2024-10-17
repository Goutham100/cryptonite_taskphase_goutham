# Task-phase writeup

## Challenge-1 Name: Printing Variables
- variables can be printed with `echo $name_of_variable` .
- solution: `echo $FLAG

## Challenge-2 Name: Setting Variables
- variables can be set with `name_of_variable=value`
- solution : `PWN="COLLEGE"`

## Challenge-3 Name: Multi_word Variables
- if you want to enter a data with space to a variable it should be within quotes
- for example `PWN="COLLEGE YEAH"` which is the solution

## Challenge-4 Name: Exporting Variables
- variables can be exported to different shell sessions using export
- for example: `export variable_name` passes variable_name into environment variables
- solution:  
```
              PWN=COLLEGE
              export PWN
              COLLEGE=PWN
              /challenge/run

```
## Challenge-5 Name: Printing Exported Variables
- env command prints all the exported variables 

## Challenge-6 Name: Storing Command Output
- use `variable=$(command)` to store the output of command in a variable
- solution: `PWN=$(/challenge/run)` then `echo $PWN `to display the flag

## Challenge-7 Name: Reading Input
- read command reads the input by the user
- solution : `read PWN` then enter COLLEGE which assigns COLLEGE to PWN.

## Challenge-8 Name: Reading files
- you can redirect the output to standard input of read
- solution: `read PWN < /challenge/read_me`

