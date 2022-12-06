# Given an absolute path for a file (Unix-style), simplify it. Note that absolute path always begin with ‘/’ ( root directory ), a dot in path represent current directory and double dot represents parent directory.

# Examples:

# "/a/./"   --> means stay at the current directory 'a'
# "/a/b/.." --> means jump to the parent directory
#               from 'b' to 'a'
# "////"    --> consecutive multiple '/' are a  valid  
#               path, they are equivalent to single "/".

# Input : /home/
# Output : /home

# Input : /a/./b/../../c/
# Output : /c

# Input : /a/..
# Output:/

# Input : /a/../
# Output : /

# Input : /../../../../../a
# Output : /a

# Input : /a/./b/./c/./d/
# Output : /a/b/c/d

# Input : /a/../.././../../.
# Output:/

# Input : /a//b//c//////d
# Output : /a/b/c/d

input = "/a/../.././../../.y"
commands = input.split('/')
commands.remove('')
commands = [item for item in commands if item != '']
print(commands)
path = []
for command in commands:
    print(command)
    if command not in ['.', '..']:
        path.append(command)
    elif command == '..':
        if len(path)>0:
            path.pop()

print(f"/{'/'.join(path)}")