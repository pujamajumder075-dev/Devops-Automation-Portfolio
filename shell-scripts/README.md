# 📜 Shell Scripting Reference & Labs

A comprehensive collection of Bash shell scripts covering basics to advanced DevOps automation.

## 📁 Folder Structure

### 1. **basics/** - Shell Scripting Fundamentals
Core concepts and basic shell scripting patterns.

- **hello_world.sh** - Your first shell script with echo statements
- **variables_and_user_input.sh** - Working with variables and user input (read command)
- **command_line_arguments.sh** - Passing arguments to scripts ($0, $1, $2, $#)
- **file_and_directory_checking.sh** - File and directory existence checks (-f, -d flags)

**Learning Outcomes:**
- Shebang (#!) and script execution
- Echo and print statements
- Variable assignment and usage
- User input with read command
- Command-line arguments handling
- File system operations

---

### 2. **conditionals/** - Control Flow & Decision Making
Conditional statements and logical operations.

- **if_else_conditionals.sh** - Simple if-else logic ([ ] operators)

**Learning Outcomes:**
- if-else statements
- Test operators and comparisons
- String and numeric comparisons
- Conditional logic in scripts

---

### 3. **loops/** - Iteration & Repetition
Loop constructs for repeating tasks.

- **for_loop_example.sh** - For loops with ranges and sequences
- **while_loop_example.sh** - While loops with counters and conditions

**Learning Outcomes:**
- For loops with ranges
- While loops and conditions
- Counter increments
- Loop control

---

### 4. **functions/** - Reusable Code Blocks
Defining and calling functions in shell scripts.

- **user_verification_function.sh** - Function definition and user verification
- **source_script_example.sh** - Sourcing external scripts

**Learning Outcomes:**
- Function definition and calls
- Function parameters and return values
- Sourcing external scripts
- Code reusability

---

### 5. **automation/** - Real-World Automation
Practical automation scripts for DevOps tasks.

- **backup_script.sh** - Backup directory with timestamp

**Learning Outcomes:**
- File archiving (tar, gzip)
- Timestamp generation
- Path handling
- Backup automation

---

### 6. **advanced/** - Complex Scenarios
Advanced shell scripting patterns and real-world use cases.

- **package_installation.sh** - Package management automation
- **cricket_team_management.sh** - User and group management system

**Learning Outcomes:**
- System administration
- User/group management
- Error checking and validation
- Complex workflows

---

## 🚀 Quick Start

### Prerequisites
```bash
# Check bash version
bash --version

# Most scripts require sudo for system operations
sudo -v
```

### Running Scripts

#### Making Scripts Executable
```bash
chmod +x script_name.sh
```

#### Running Scripts
```bash
# Run with bash
bash script_name.sh

# Run directly (after chmod +x)
./script_name.sh

# Run with arguments
./script_name.sh arg1 arg2
```

### Examples by Category

#### Basics
```bash
# Simple hello world
bash basics/hello_world.sh

# Variables and user input
bash basics/variables_and_user_input.sh

# Command-line arguments
bash basics/command_line_arguments.sh arg1 arg2

# File checking
bash basics/file_and_directory_checking.sh
```

#### Conditionals
```bash
# If-else logic
bash conditionals/if_else_conditionals.sh
```

#### Loops
```bash
# For loop
bash loops/for_loop_example.sh

# While loop
bash loops/while_loop_example.sh
```

#### Functions
```bash
# User verification
bash functions/user_verification_function.sh

# Source example
bash functions/source_script_example.sh
```

#### Automation
```bash
# Backup script (requires SOURCE and TARGET paths)
bash automation/backup_script.sh
```

#### Advanced
```bash
# Package installation (requires package name)
sudo bash advanced/package_installation.sh nginx

# Cricket team management (requires sudo)
sudo bash advanced/cricket_team_management.sh
```

---

## 🔑 Key Concepts

### Shell Variables
- `$0` - Script name
- `$1, $2, ...` - Command-line arguments
- `$#` - Number of arguments
- `$@` - All arguments
- `$USER` - Current user
- `$HOME` - Home directory

### Test Operators
- `-f` - File exists
- `-d` - Directory exists
- `-e` - File or directory exists
- `-z` - String is empty
- `-n` - String is not empty
- `==` - String equality
- `-eq` - Numeric equality
- `-lt` - Less than
- `-gt` - Greater than

### Useful Commands
- `echo` - Print text
- `read` - Read user input
- `touch` - Create files
- `mkdir` - Create directories
- `tar` - Archive files
- `gzip` - Compress files
- `chmod` - Change permissions
- `useradd` - Create users
- `groupadd` - Create groups
- `systemctl` - Manage services

---

## 📝 Common Patterns

### Check if file exists
```bash
if [ -f "/path/to/file" ]; then
    echo "File exists"
else
    echo "File not found"
fi
```

### Simple for loop
```bash
for i in {1..10}; do
    echo "Iteration $i"
done
```

### While loop counter
```bash
count=1
while [ $count -le 10 ]; do
    echo "Count: $count"
    count=$((count+1))
done
```

### Function definition
```bash
function my_function() {
    echo "Hello from function"
    return 0
}

my_function
```

### Read user input
```bash
read -p "Enter your name: " name
echo "Hello, $name"
```

---

## 💡 Tips & Best Practices

✅ Always add shebang (#!/bin/bash) at the top  
✅ Use meaningful variable names  
✅ Add comments for clarity  
✅ Check for file/directory existence before operations  
✅ Use quotes around variables: "$var"  
✅ Add error handling and validation  
✅ Make scripts executable: chmod +x script.sh  
✅ Use functions for code reusability  
✅ Log important operations  

---

## 🎓 Learning Path

1. **Start with Basics**
   - hello_world.sh
   - variables_and_user_input.sh

2. **Learn Control Flow**
   - command_line_arguments.sh
   - if_else_conditionals.sh

3. **Master Loops**
   - for_loop_example.sh
   - while_loop_example.sh

4. **Advanced Concepts**
   - user_verification_function.sh
   - backup_script.sh

5. **Real-World Scenarios**
   - package_installation.sh
   - cricket_team_management.sh

---

## 🔗 Useful Resources

- [GNU Bash Manual](https://www.gnu.org/software/bash/manual/)
- [ShellCheck - Script Analyzer](https://www.shellcheck.net/)
- [Linux Command Reference](https://linux.die.net/man/)

---

**Built with ❤️ for DevOps engineers learning shell scripting**
