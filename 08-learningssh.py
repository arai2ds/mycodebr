b0VIM 8.0      ���\�C �V  student                                 pyapi-207-bchd                          ~student/mycodebr/sshf.py                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    utf-8U3210    #"! U                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 tp           /                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             ad  �	  �
     /       �  �  �  �  �  �  �  �  ]    �  �  �  J  I  H  <    �  �  �  w  v  L    �  �  �  p  I    �  �  �  I  H        �
  �
  �
  �
  �
  �
  �
  �
  �
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       main()  if __name__=="__main__":            sshsession.close()         #close connection                        print(results,file=svrlog)                 #with open((server['ip]).replace(".","")+".log","a") "serverresults.log","a") as svrlog:                # with open("serverresults.log","a") as svrlog:              if results != "":             results = cmdissue(sshsession,commandtoissue)         for commandtoissue in CMDLIST:         # get uptime of servers          # touch two files          sshsession.connect(hostname=server['ip'],username=server['un'],pkey=myprivkey)         sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())         sshsession = paramiko.SSHClient()      for server in SRVRS:     # initiate connection to remote machine          myprivkey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")     # harvest RSA key (ssh private key) def main():       return ssh_stdout.read().decode('utf-8').rstrip('\n')     ssh_stdin,ssh_stdout,ssh_stderr = sshsession.exec_command(commandtoissue) def cmdissue(sshsession,commandtoissue):     CMDLIST = cmds.readlines() #CMDLIST = ['touch sshworked.txt','touch sshworked2.ssh','uptime'] with open("cmds2issue.txt","r") as cmds:  SRVRS = [{'ip':'10.10.2.3','un':'bender'},{'ip':'10.10.2.4','un':'fry'}]  import paramiko  import os  #!/usr/bin/python3 