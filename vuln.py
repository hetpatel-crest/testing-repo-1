import os


def run(cmd):
    # insecure: command injection via os.system with untrusted input
    os.system("echo " + cmd)


password = "hardcoded_secret_value_12345"
