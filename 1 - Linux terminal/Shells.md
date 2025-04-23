## Filesystem

1. Navigate to the home directory.
2. Create a directory named `course`.
3. Print the current working directory.
4. Create a `mybin` directory inside the `course` directory.
5. Create a symbolic link to `/bin/bash` in the `mybin` directory.
6. Print the list of files in the `mybin` directory.

## Permissions
1. Print the permissions inside the `mybin` directory. Should I be allowed to change the contents of the bash file?
2. Copy the `bash` file into `mybash`.
3. Print the permissions again.
4. Remove the execution permission from `mybash`.
5. Run `./mybash`. What's going on?
6. Create a directory `mydir`.
7. Remove the execution permission from `mydir`.
8. Navigate into `mydir`. What's going on?
9. Change the permission to `770` for mydir. Did this allow now to navigate?
11. Set the umask to `077`.
12. Create a directory named `test1`.
13. Set the umask to `002`.
14. Create a directory named `test2`.
15. Print the permissions. What's the difference between `test1` and `test2`. What is it allowed for `test2` that it is not allowed in for `test1`?

## Scripts
1. Navigate to the `mybin` directory.
2. Create a file named `myscript.sh` using `nano`.
3. Add some text. Save the file and exit `nano`.
4. Use the `cat` command to print the contents of the file.
5. Edit the file again, and add the following content:

```bash
#!/bin/bash

cd ~
mkdir test_script

for i in {1..10}
do
   echo "This is the loop number ${i}"
done
```
6. Execute the file with `./myscript.sh`? Does it work? Can you fix it?

## Variables
1. Set the variable `a` to string of your preference.
2. Print the content of the variable (`echo $a`).
3. Run a child `bash` process.
4. Print the content of the variable (`echo $a`). Does it look empty?
5. Exit the child process.
6. Print the content of the variable (`echo $a`). Is it working now?
7. Export the variable `a`.
8. Run a child `bash` process.
9. Print the content of the variable (`echo $a`). What about now?
10. Print all the environmental variables (`env`). Is it there?
11. `unset` the variable `a`.
12. Print all the environmental variables (`env`). Is it there?
13. Exit the child process.
14. Print all the environmental variables (`env`). Is it there? Why?

## PATH environmental variable
1. Navigate to the home directory.
2. Execute `myscript.sh`. Does it work? Is `~/course/mybin/` in the PATH variable?
3. At the `~/course/mybin` directory to the `PATH` variable. Important: expand `~` as this symbol won't work here.
4. Execute `myscript.sh`. Does it work now?

## Input/Output (I/O)
1. `echo` a string of your preference to `~/course/echoed.txt`.
2. `cat` the written file by redirecting standard input (`stdin`).
3. Append another line to `~/course/echoed.txt` using `echo`.
4. Look for a specific word you have written to `~/course/echoed.txt` using `cat` and `grep` commands and the pipe (`|`) character.
5. Try `cat ~/course/notfound.txt`. Do you get an error? Is the error showing up in standard output (`stdout`) or standard error (`stderr`)? (Hint: try redirecting both streams (`stdout` and `stderr`) to `/dev/null`) Can you redirect it to the other stream?
6. Redirect the previous command's `stdout` and `stderr` streams to `~/course/null.txt`.