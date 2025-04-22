# Excersise 1 & 2: Fundamentals of Unix Terminal and Programming 


## 1. Install miniforge

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
 
To create a new python environment using miniforge type in the Terminal
```
conda create -n first_pyenv python=3.12
```

The `-n` flag to specify the name of the environment, here `first_pyenv` (can be any other name you like) followed by the packages to install in the environment, here `python(version 3.12)`.

Before working with the environment, activate it
```
conda activate first_pyenv (or the name you have selected)
```

Install more packages (e.g. numpy) while the environment is active, use
```
conda install numpy
```
If no version is specified, the most recent version will be installed.

Additional Info:
- After installing miniforge you can either type `conda`  or `mamba` with the same effect.
- Environments can be created empty with just a name, see: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
- Installing packages can be done after creating as well. While the environment is activated, type: 
`mamba install (name of the package)`
- Further Informations on how to manage your environments can be foudn here: https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html

## 3. Recreate the Bingo game from the slides using nano

1. Open the nano editor by typing the command `nano` in the Terminal.
2. Replicate the `bingo.py` example from the slides. 
3. To save the script using the key-binding `control+O` (`O` not `zero`)
4. Then close the editor using the key-binding `control+X`

To execute the script type the following while you are in the directory of the script you just created using nano.
```
python bingo.py
```

## 4. Install VSCode

1. Download and install vscode: https://code.visualstudio.com/download
2. Be happy you just entered the world of IDEs 


## 5. VSCode demo (Fede)

(more stuff to do here)