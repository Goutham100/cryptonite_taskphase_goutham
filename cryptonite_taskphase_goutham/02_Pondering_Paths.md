# Task-phase writeup
## Challenge-1 Name: The Root

### Challenge description:
type the command and hit enter

### Category: linux Basics

## Step 1: Enter the path to get the flag
- Enter `/pwn` to get the flag.

### Tools used:
- none

## Challenge-2 Name: Program and absolute paths

### Challenge description:
type the command and hit enter.

### Category: linux Basics

## Step 1: Enter the path and run the  run program to get the flag
- Enter `/challenge/run` to get the flag.

### Tools used:
- none

## Challenge-3 Name: Position thy self

### Challenge description:
traverse through the directory and execute the given program

### Category: linux Basics

## Step 1: find the contents of the directory im in
- run `ls` , output: Desktop
- enter Desktop and run the program
- gets the directory where the program is , go to it and run the program to get the flag

### Tools used:
- none

## Challenge-4 Name: Position elsewhere

### Challenge description:
traverse through the directory and execute the given program

### Category: linux Basics

## Step 1: find the contents of the directory im in
- run `ls` , output: Desktop
- enter Desktop and run the program
- gets the directory where the program is , go to it and run the program to get the flag

### Tools used:
- none

## Challenge-5 Name: Position yet elsewhere

### Challenge description:
traverse through the directory and execute the given program

### Category: linux Basics

## Step 1: find the contents of the directory im in
- run `ls` , output: Desktop
- enter Desktop and run the program
- gets the directory where the program is , go to it and run the program to get the flag

### Tools used:
- none


## Challenge-6 Name: implicit relative paths, from /

### Challenge description:
traverse through the directory and execute the given program

### Category: linux Basics

## Step 1: find the contents of the directory im in
- run `ls` , output: Desktop
- enter Desktop and run the program
- gets the directory where the program is in which is /, so i go back to / using cd .. command and run the program.

### Tools used:
- none

## Challenge-7 Name: explicit relative paths, from /

### Challenge description:
traverse through the directory and execute the given program

### Category: linux Basics

## Step 1: find the contents of the directory im in
- run `ls` , output: Desktop
- enter Desktop and run the program
- gets the directory where the program is in which is /, so i go back to / using `cd ..` command and run the program explicitly using `./`

### Tools used:
- none

## Challenge-8 Name: explicit relative paths.

### Challenge description:
traverse through the directory and execute the given program

### Category: linux Basics

## Step 1: find the contents of the directory im in
- run `ls` , output: Desktop
- enter Desktop and run the program
- gets the directory where the program is in which is /, so i go back to / using `cd ..` command and then enter challenge.
- then I used `./run` to get the flag as it requires to enter from relative path.

### Tools used:
- none

## Challenge-9 Name: Home sweet Home.

### Challenge description:
traverse through the directory and execute the given program

### Category: linux Basics

## Step 1: go to the home directory [not necessary and can be skipped]
- use `cd ..` command to go home

## step 2: run challenge/run using a specified parameter
- the parameter has to be 3 chars and an absolute path which is `~/~`
- run `/challenge/run ~/~` to get the flag

### Tools used:
- none


