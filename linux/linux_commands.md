#vBasic Linux Commands      Shalom Mitz   3-Feb-2025

## wild cards:  

   * --> any sequence of chars   . --> one char
   examples:   *.txt    student_name_???.csv

## path: 

   ~ --> home dir   / --> root dir   . --> current dir   .. --> parent dir
   paths can be absolute (start with /) or relative (to the current dir)
   separated by  /

## re-execute commands: 

   Arrow-up: get previous command(s)  history: show previous commands

## chaining:  

   | --> connects output of one command to input on next command    > --> put output into file

## commands:

	find <path>: find all the files in path  pwd: present working directory
	ls: shows files and dictionaries in current dictionary
		ls -l: the same, shows details such as size
	cd: change to home directory
	cd <dir name>: change to the named directory
	rm <file name>: remove the named file
	rm -rf <directory name>: remove a directory and everything inside
	mv <old name> <new name>: change the name of file or directory
	mv <name> <directory>: move the name file or dir to a new directory
	cat > <file name> start creating new file (end with ^D)
	cat <file name>: shows the named file on screen
	cp <current file name> <new file name>: copies a file
	more <file name>: shows on screen, page by page
	grep <word> <file name>: find word in the named file
	diff <first file> <second file>: shows difference between two file
	clear: clear the screen
	find <path>: find all the files in path
        su: became super-user (lets you do dangerous things)
        sudo: lets you execute dangerous commands
        
## Applications:

    vi <file name>: edit files (visual editor): hard to use but fast
        vi commands:   Esc   i   A  :wq  x   dd
    git <command>: a time machine for projects
        git commands:   init   add   clone push pull status commit log
    nano <file name>: edit files. Easier to use
    gedit <file name>: graphical edit file(s)
    ristretto <file name>: show image(s)
    atril <file name>: show PDF(s)
    pip install <package name>: installs Python modules
    apt: manages the Ubuntu packages
         apt commands:  list install remove update upgrade
    
    
