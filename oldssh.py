#!/usr/bin/python3

import os

import paramiko

CMDLIST = ['touch sshworked.txt','touch sshworked2.ssh','uptime']

def main():
    # harvest RSA key (ssh private key)
    myprikey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")
    
    # initiate connection to remote machine

    sshsession = paramiko.SSHClient()
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshsession.connect(hostname="10.10.2.3",username="bender
    # touch two files 

    # get uptime of servers

    #close connection



if __name__=="__main__":

    main()
