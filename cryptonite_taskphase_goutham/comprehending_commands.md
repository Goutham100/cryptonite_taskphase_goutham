# Task-phase writeup
## Challenge-1 Name: cat: not the pet, but the command

### Category: linux Basics

### Step 1: check for files in the current directory
- Enter `ls`
- you'll see a file called flag

### step 2: use cat command on the flag file
- you'll get the flag

### Tools used:
- none

## Challenge-2 Name: catting absolute paths

### Category: linux Basics

### Step 1: go to root which is /
- use `cd ..` to go to the / directory

### step 2: use cat command on the flag file at its absolute path
- `cat /flag` to get the flag

### Tools used:
- none

## Challenge-3 Name: more catting practice

### Category: linux Basics

### Step 1: use cat on the absolute path which is /lib/ipxe/qemu/flag
- use `cat /lib/ipxe/qemu/flag` to get the flag

### Tools used:
- none

## Challenge-4 Name: grepping for a needle in a haystack

### Category: linux Basics

### Step 1: use grep and use SEARCH_STRING as pwn.college 
- use:  `grep pwn.college /challenge/data.txt` to get the flag

### Tools used:
- none

## Challenge-5 Name: listing files

### Category: linux Basics

### Step 1: go to challenge directory
- use:  `cd ../..` to get to the root
- use: cd challenge to enter the directory
- use `ls`
- run the program using `./name_of_file` to get the flag

### Tools used:
- none

## Challenge-6 Name: touching files

### Category: linux Basics

### Step 1: create files /tmp/pwn and /tmp/college
- use:  `touch /tmp/pwn` and `touch /tmp/college`

### Step 2: run /challenge/run to get the flag

### Tools used:
- none

## Challenge-7 Name: removing files

### Category: linux Basics

### Step 1: remove delete_me file
- use:  `rm delete_me`

### Step 2: run /challenge/check to get the flag

### Tools used:
- none

## Challenge-8 Name: hidden files

### Category: linux Basics

### Step 1: go to / directory
- use:  `cd ../..`

### Step 2: view the files starting with.
- use: `ls -a` , you'll be greeting with a file named .flag-27761288348281

### Step 3: use to cat to view that file
- use: `cat .flag-27761288348281` , to get the flag

### Tools used:
- none