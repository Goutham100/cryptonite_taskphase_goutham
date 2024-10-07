# Task-phase writeup
## Challenge-1 Name: Matching with *

### Category: linux Basics

### Step 1: go to /challenge directory using globbing
- run: `cd /c*` [*: shell replaces this with anything that matches the pattern]

### Step 2: run `/challenge/run`

### Tools used:
- none

## Challenge-2 Name: Matching with ?

### Category: linux Basics

### Step 1: go to /challenge directory using globbing
- replace c and l with ?
- run: `cd /?ha??enge` [?: shell replaces this with a single char that matches the pattern]

### Step 2: run `/challenge/run`

### Tools used:
- none

## Challenge-3 Name: Matching with []

### Category: linux Basics

### Step 1: go to /challenge directory

### Step 2: run `/challenge/run` with a single argument that bracket-globs into file_b, file_a, file_s, and file_h
- run: `/challenge/run file_[absh]` [[]: limited version of ?, where it matches the chat within the []s]

### Tools used:
- none

## Challenge-4 Name: Matching paths with []

### Category: linux Basics

### Step 1: run `/challenge/run` with a single argument that bracket-globs into the absolute paths to the file_b, file_a, file_s, and file_h files
- run `/challenge/run /challenge/files/file_[abhs]` to get the file

### Tools used:
- none

