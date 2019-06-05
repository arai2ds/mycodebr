#!/usr/bin/python3

import os

import paramiko

SRVRS = [{'ip':'10.10.2.3','un':'bender'},{'ip':'10.10.2.4','un':'fry'}]

with open("cmds2issue.txt","r") as cmds:
#CMDLIST = ['touch sshworked.txt','touch sshworked2.ssh','uptime']
    CMDLIST = cmds.readlines()
def cmdissue(sshsession,commandtoissue):
    ssh_stdin,ssh_stdout,ssh_stderr = sshsession.exec_command(commandtoissue)
    return ssh_stdout.read().decode('utf-8').rstrip('\n')


def main():
    # harvest RSA key (ssh private key)
    myprivkey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")
    
    # initiate connection to remote machine
    for server in SRVRS:

        sshsession = paramiko.SSHClient()
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshsession.connect(hostname=server['ip'],username=server['un'],pkey=myprivkey)
        # touch two files 

        # get uptime of servers
        for commandtoissue in CMDLIST:
            results = cmdissue(sshsession,commandtoissue)
            if results != "":

               # with open("serverresults.log","a") as svrlog:
               logfile = server['ip'].replace(',','') +'.log'
               with open(logfile,'a') as svrlog:
                   print(svrlog)
                   print('COMMAND ISSUES -', commandtoissue,file = svrlog)
                   print(results,file=svrlog)
               #with open((server['ip]).replace(".","")+".log","a") "serverresults.log","a") as svrlog:
                   print('', file=svrlog)
                     #print(results,file=svrlog)


        #close connection
        sshsession.close()



if __name__=="__main__":

    main()
