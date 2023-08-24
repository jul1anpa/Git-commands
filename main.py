'''
You can use git config --global 
user.name to change a "username"
user.email to change an "email"

git init will initialize a new git repository
git status will return the your status
git add . will add all commits to the added queue
git commit will commit all queued commits
git log will return all commitments and a time log 

git branch will return all branch names
git branch <new branch name> will create a new branch
git checkout <branch name> will switch your working branch
You can also use the -b flag after checkout to create and switch to a branch at the same time
git merge <branch name> will merge the provided branch with your current branch
git  branch -d <branch name> will delete a branch

git remote add origin <url> will set an online repo location that you can push your local repo changes to
git push -u origin master will push all changes in your master branch
'''

first, last = input("What's your name? ").split(' ')

print("Hello, ", first)