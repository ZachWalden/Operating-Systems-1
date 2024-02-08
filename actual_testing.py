import subprocess

output = subprocess.check_output("echo nice", shell=True)

print(output)
