#! /usr/bin/env python2
from subprocess import check_output

def get_pass(accout_name):
    return check_output("GNUPGHOME='~/.offlineimap.d/gnupg' gpg -dq ~/.offlineimap.d/"+str(accout_name)+"pw", shell=True).strip("\n")
