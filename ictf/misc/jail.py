#!/usr/local/bin/python

from subprocess import PIPE, Popen
from time import sleep

cmd = input("Try your hand at cracking the cosmo jail\n> ")

if any([_ in cmd.lower() for _ in ["exec", "system", "flag"]]):
    print("Won't allow it. This just simply won't do")
    quit()

# install cosmo 0.10.0 from https://github.com/cosmo-lang/cosmo/releases/tag/v0.10.0
process = Popen("/usr/local/bin/cosmo", stdin=PIPE)
process.stdin.write(cmd.encode("ascii"))
process.stdin.close()

sleep(1)
