#!/usr/bin/python3

import os

import paramiko


CMDLIST = ['touch sshworked.txt','touch sshworked2.ssh','uptime']

def cmdissue(sshsession,commandtoissue):
    ssh_stdin,ssh_stdout,ssh_stderr = sshsession.exec_command(commandtoissue)
    return ssh_stdout.read()


def main():
    # harvest RSA key (ssh private key)
    myprivkey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")
    
    # initiate connection to remote machine

    sshsession = paramiko.SSHClient()
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshsession.connect(hostname="10.10.2.3",username="bender",pkey=myprivkey)
    # touch two files 

    # get uptime of servers
    for commandtoissue in CMDLIST:
        print(cmdissue(sshsession,commandtoissue))


    #close connection
    sshsession.close()



if __name__=="__main__":

    main()
