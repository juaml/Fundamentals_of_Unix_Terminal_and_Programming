# Excersise 1 & 2: Fundamentals of Unix Terminal and Programming 


## 1. Install miniforge

The full instructions are here: https://conda-forge.org/download/

The following is a summary of what needs to be done depending on your operating system.

Open the Terminal and type

For Windows users: 
```
start /wait "" Miniforge3-Windows-x86_64.exe /InstallationType=JustMe /RegisterPython=0 /S /D=%UserProfile%\Miniforge3
```

For MacOS and Linux users: 
```
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh
```

More detailed instructions can be found here:
- https://github.com/conda-forge/miniforge
- https://conda-forge.org/download/

## 2. Create your first python environment 

Note: From now on, we can use `conda` or `mamba` as both commands will work.
 
To create a new python environment using miniforge type in the Terminal
```
conda create -n first_pyenv python=3.12
```

The `-n` flag is used to specify the name of the environment (here `first_pyenv`, but can be any other name you like) followed by the packages to install in the environment, here `python` using version 3.12.

Before working with the environment, activate it
```
conda activate first_pyenv
```

Install more packages (e.g. numpy) while the environment is active, use
```
conda install numpy
```
If no version is specified, the most recent version will be installed.

Additional Info:
- Environments can be created empty with just a name, see: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
- Installing packages can be done after creating as well. While the environment is activated, type: 
`mamba install (name of the package)`
- Further Information on how to manage your environments can be found here: https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html

## 3. Recreate the Bingo game from the slides using nano

1. Open the terminal and create a directory where you want to work (e.g. `~/course` as in the previous class)
2. Open the nano editor by typing the command `nano` in the Terminal.
3. Replicate the `bingo.py` example from the slides. 
4. To save the script using the key-binding `control+O` (`O` not `zero`)
5. Then close the editor using the key-binding `control+X`

To execute the script type the following while you are in the directory of the script you just created using nano.
```
python bingo.py
```

## 4. Install VSCode

1. Download and install vscode: https://code.visualstudio.com/download
2. Be happy you just entered the world of IDEs 


## 5. VSCode demo (Fede)

1. Go to the directory you selected in step 3 and type `code .`. This should open a VSCode window on that project directory. If you have an error, check the following link to activate the command line interface for VSCode: https://code.visualstudio.com/docs/setup/mac#_launch-vs-code-from-the-command-line

2. How does your `bingo.py` code looks like now?

3. Add some `# %%` cells and run `bingo.py` in interactive mode. You might need to install the _Jupyter_ extension for this to work.

4. Open a new terminal (inside vscode) and run `bingo.py` in `ipython`

5. Encapsulate the code into functions so that _drawing_ a number and _checking_ for bingo are within one function.

6. Enable/install the _pylance_, _flake8_ (from Microsoft) and _ruff_ (from Astral Software) extensions.

7. Is your code looking good now? Use the command palette to _Format Document_ using ruff. 
   *  MAC: Command + Shift + P 
   *  Windows/Linux: Ctrl + Shift + P
  
8. Now encapsulate the code to play bingo in a function and run it 10 times using a _for_ loop. What was your fastest number of draws to bingo? Tell us in the next course.