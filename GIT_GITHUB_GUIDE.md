# 🔧 Git & GitHub Complete Guide - Hands-On Practice

Based on real-world DevOps workflow and best practices

## 📖 Table of Contents

1. [Initial Setup](#initial-setup)
2. [SSH Key Configuration](#ssh-key-configuration)
3. [Repository Operations](#repository-operations)
4. [Branching Strategy](#branching-strategy)
5. [Committing Changes](#committing-changes)
6. [Working with Remotes](#working-with-remotes)
7. [Common Workflows](#common-workflows)
8. [Troubleshooting](#troubleshooting)

---

## 🚀 Initial Setup

### Initialize a New Git Repository

```bash
# Navigate to your project directory
cd ~/git_practice

# Initialize git
git init

# Output:
# Initialized empty Git repository in /home/ubuntu/git_practice/.git/
```

**What happens:**
- Creates a hidden `.git` folder to track all changes
- Sets up the repository structure
- Initializes with default branch (master or main)

### Configure Git Identity

```bash
# Set global name and email
git config --global user.name "Puja Majumder"
git config --global user.email "pujamajumder075@gmail.com"

# Verify configuration
git config --global --list

# Edit configuration file
git config --global --edit
```

**Important:**
- Use the same email for GitHub account
- This appears on all your commits
- Can be configured locally per repository too

---

## 🔐 SSH Key Configuration

### Generate SSH Key

```bash
# Generate ed25519 SSH key (modern & secure)
ssh-keygen -t ed25519 -C "pujamajumder075@gmail.com"

# Output:
# Generating public/private ed25519 key pair.
# Enter file in which to save the key (/home/ubuntu/.ssh/id_ed25519):
```

**Key Details:**
- Press Enter to use default location
- Leave passphrase empty (or set one for security)
- Generates two files:
  - `id_ed25519` - Private key (KEEP SECRET!)
  - `id_ed25519.pub` - Public key (Share with GitHub)

### Display Your Public Key

```bash
# View your public key
cat /home/ubuntu/.ssh/id_ed25519.pub

# Output:
# ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDqcLR7OdCaztmQCzFI+e82wn4rVUcxn592VXd5hrrV6 ubuntu@ip-172-31-42-16
```

### Add SSH Key to GitHub

1. Go to GitHub Settings → SSH and GPG Keys
2. Click "New SSH key"
3. Paste your public key (from `id_ed25519.pub`)
4. Give it a descriptive name (e.g., "Ubuntu Dev Machine")
5. Click "Add SSH key"

### Verify SSH Connection

```bash
# Test SSH connection to GitHub
ssh -T git@github.com

# Output should be:
# Hi pujamajumder075-dev! You've successfully authenticated, but GitHub does not provide shell access.
```

---

## 📁 Repository Operations

### Clone a Repository

```bash
# Clone using SSH (after SSH setup)
git clone git@github.com:pujamajumder075-dev/Git-Github.git

# Or clone using HTTPS
git clone https://github.com/pujamajumder075-dev/Git-Github.git

# Output:
# Cloning into 'Git-Github'...
# remote: Enumerating objects: 3, done.
# remote: Counting objects: 100% (3/3), done.
# remote: Compressing objects: 100% (2/2), done.
# remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0 (from 0)
# Receiving objects: 100% (3/3), done.
```

### Navigate to Repository

```bash
# Enter cloned repository
cd Git-Github

# List files
ls
# Output:
# git-help.txt

# Check current status
git status
# Output:
# On branch main
# Your branch is up to date with 'origin/main'.
# nothing to commit, working tree clean
```

---

## 🌳 Branching Strategy

### View Branches

```bash
# List all local branches
git branch

# Output:
#   devops
# * main
# (* indicates current branch)

# List remote branches
git branch -r

# List all branches (local + remote)
git branch -a
```

### Create a New Branch

```bash
# Create and switch to new branch in one command
git checkout -b devops

# Output:
# Switched to a new branch 'devops'

# Alternative: Create branch then switch
git branch devops          # Create
git checkout devops        # Switch

# Modern way (git 2.23+):
git switch -c devops
```

### Switch Between Branches

```bash
# Switch to existing branch
git checkout main

# Output:
# Switched to branch 'main'
# Your branch is up to date with 'origin/main'.

# Verify you're on correct branch
git branch
# Output:
#   devops
# * main
```

### Delete a Branch

```bash
# Delete local branch (after merging)
git branch -d devops

# Force delete local branch
git branch -D devops

# Delete remote branch
git push origin --delete devops
```

---

## 💾 Committing Changes

### View Commit History

```bash
# View commit log
git log

# Output:
# commit 1f5c58c426939bfd0c30e24cdbb164f41904d84c (HEAD -> main)
# Author: Ubuntu <ubuntu@ip-172-31-42-16.eu-north-1.compute.internal>
# Date:   Sun Jun 7 08:17:00 2026 +0000
#
#     added hello text
#
# commit 77c9c2cebebb4119079345814187595ceba33c52 (origin/main, origin/HEAD, devops)
# Author: pujamajumder075-dev <pujamajumder075@gmail.com>
# Date:   Sun Jun 7 06:51:20 2026 +0000
#
#     help file added
```

### Create Files and Commit

```bash
# Create a new file
vi hello.txt

# Type content:
# hi i am in main

# Check status
git status
# Output:
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         hello.txt

# Stage the file
git add hello.txt

# Verify staging
git status
# Output:
# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)
#         new file:   hello.txt

# Create commit
git commit -m "added hello text"

# Output:
# [main 1f5c58c] added hello text
#  1 file changed, 1 insertion(+)
#  create mode 100644 hello.txt
```

### Commit Best Practices

```bash
# Good commit message format:
# - Start with verb (add, fix, update, remove)
# - Be descriptive but concise
# - Use lowercase first letter
# - No period at end

# Good examples:
git commit -m "add user authentication module"
git commit -m "fix database connection timeout"
git commit -m "update documentation for API endpoints"
git commit -m "remove deprecated function calls"

# Bad examples:
git commit -m "fix"                    # Too vague
git commit -m "UPDATED EVERYTHING"    # Too general
git commit -m "asdfgh"                 # Meaningless
```

### Stage Multiple Files

```bash
# Stage specific files
git add file1.sh file2.py

# Stage all changes
git add .

# Stage all Python files
git add *.py

# Stage interactively
git add -p
```

---

## 🔄 Working with Remotes

### View Remote Information

```bash
# Show remote repositories
git remote

# Output:
# origin

# Show remote with URLs
git remote -v

# Output:
# origin  git@github.com:pujamajumder075-dev/Git-Github.git (fetch)
# origin  git@github.com:pujamajumder075-dev/Git-Github.git (push)
```

### Pull Changes from Remote

```bash
# Fetch latest changes from remote (doesn't merge)
git fetch origin

# Pull changes and merge (fetch + merge)
git pull origin main

# Pull and rebase (recommended for clean history)
git pull --rebase origin main
```

### Push Changes to Remote

```bash
# Push current branch to remote
git push origin main

# Push new branch to remote
git push -u origin devops

# Push all branches
git push --all

# Push all tags
git push --tags
```

### Check Remote Status

```bash
# Show local commits ahead of remote
git status

# Output:
# On branch main
# Your branch is ahead of 'origin/main' by 1 commit.
#   (use "git push" to publish your local commits)
```

---

## 🔀 Common Workflows

### Feature Branch Workflow

```bash
# 1. Create feature branch from main
git checkout -b feature/user-auth

# 2. Make changes
vi auth.py
git add auth.py
git commit -m "add user authentication"

# 3. Push to remote
git push -u origin feature/user-auth

# 4. Create Pull Request on GitHub
# (Done via GitHub web interface)

# 5. After PR merged, delete branch
git checkout main
git branch -d feature/user-auth
git push origin --delete feature/user-auth
```

### Updating Main Branch

```bash
# 1. Fetch latest changes
git fetch origin

# 2. Switch to main
git checkout main

# 3. Pull latest changes
git pull origin main

# 4. Go back to feature branch
git checkout feature/user-auth

# 5. Merge main into feature (to get latest updates)
git merge main

# 6. Resolve conflicts if any
# Then commit and continue
```

### Merging Branches

```bash
# 1. Switch to target branch
git checkout main

# 2. Merge feature branch
git merge feature/user-auth

# Output:
# Updating 77c9c2c..95dabaf
# Fast-forward
#  auth.py | 50 ++++++++++++++++++++++++++++++++
#  1 file changed, 50 insertions(+)

# 3. Push merged changes
git push origin main
```

---

## 🐛 Troubleshooting

### Undoing Changes

```bash
# Undo changes in working directory (before staging)
git restore filename.txt

# Or old way:
git checkout -- filename.txt

# Unstage a file (after git add)
git restore --staged filename.txt

# Or old way:
git reset filename.txt

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1
```

### Fixing Commit Messages

```bash
# Amend last commit message
git commit --amend -m "corrected message"

# Amend without changing message
git commit --amend --no-edit
```

### Checking Differences

```bash
# Show differences in working directory
git diff

# Show differences in staged changes
git diff --cached

# Show differences between branches
git diff main devops

# Show differences between commits
git diff HEAD~1 HEAD
```

### Stashing Changes

```bash
# Save work in progress (without committing)
git stash

# List stashed changes
git stash list

# Restore stashed changes
git stash pop

# Apply without removing from stash
git stash apply
```

---

## 📋 Git Cheat Sheet

| Command | Purpose |
|---------|---------|
| `git init` | Initialize new repository |
| `git clone <url>` | Copy remote repository locally |
| `git status` | Show current status |
| `git add <file>` | Stage changes |
| `git commit -m "msg"` | Create commit |
| `git push` | Upload to remote |
| `git pull` | Download from remote |
| `git branch` | List branches |
| `git checkout -b <branch>` | Create and switch branch |
| `git merge <branch>` | Merge branch into current |
| `git log` | View commit history |
| `git diff` | Show changes |
| `git stash` | Save work temporarily |

---

## ✅ Best Practices

✅ **Commit Often** - Small, logical commits are easier to understand and revert  
✅ **Write Good Messages** - Clear messages help future you and your team  
✅ **Use Branches** - Keep main branch stable, use feature branches for work  
✅ **Pull Before Push** - Always fetch latest before pushing  
✅ **Review Before Commit** - Check what you're committing with `git diff`  
✅ **Keep SSH Key Safe** - Never share your private key  
✅ **Use SSH** - More secure than HTTPS for repeated operations  
✅ **Backup Important Work** - Push to remote regularly  

---

## 🎓 Learning Resources

- [GitHub Official Docs](https://docs.github.com)
- [Git Official Documentation](https://git-scm.com/doc)
- [GitHub Learning Lab](https://lab.github.com)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)
- [Oh Shit, Git!](https://ohshitgit.com) - Common mistakes and fixes

---

**Created from hands-on DevOps practice and real-world workflows** ❤️
