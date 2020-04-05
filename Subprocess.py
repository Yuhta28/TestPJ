from subprocess import Popen, PIPE
import subprocess

process = Popen(['cat', 'Loop.py'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
print(stdout)

# Subprocess call():
subprocess.call(["ls", "-l"])

# Save process output
s = subprocess.check_output(["echo", "Hello World!"])
print("s = " + str(s))
