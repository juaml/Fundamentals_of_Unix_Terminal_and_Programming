# Lets create a new project and initialize a git repository
cd
mkdir test_git
cd test_git
git init
echo "Hello World" > hello.txt
git status
# The file hello.txt is untracked, so we need to add it to the staging area
# and then commit it to the repository
# To add the file to the staging area, we use the git add command
# To commit the file to the repository, we use the git commit command
# The -m flag allows us to add a commit message
git add hello.txt
git commit -m "Initial commit"
echo "This is a test file" >> hello.txt
