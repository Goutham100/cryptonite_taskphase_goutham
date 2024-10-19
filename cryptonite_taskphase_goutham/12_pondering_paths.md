# Task-phase writeup

## Challenge-1 Name: the path variable
- PATH variable : contains a colon-separated list of directories where the shell looks for executables.
- you can blank it out with `PATH=""`
- solution : ![img.png](images/12_images/img.png)

## Challenge-2 Name: setting path
- by adding directories to or replacing directories in the PATH you can expose programs to be launched using their bare name
- solution: ![img_1.png](images/12_images/img_1.png)

## Challenge-3 Name: Adding Commands
- solution : in this path variable should be updated to shell script win , which should be able to give the flag
- the shell script contains `read line </flag;echo $line` which reads a line from /flag, stores it in variable line and prints it
- ![img.png](images/12_images/img2.png)

## Challenge-4 Name: Hijacking Commands
- solution: ![img.png](images/12_images/img3.png)