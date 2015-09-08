# -*- coding:utf-8 -*-

import commands
import time

USERINFO = {'USER_TOKEN': '','ACCOUNT_NAME':''}

crtpath = '/root/task/api/ssl6/ca.crt'   
 
def testcasecmd(cmd,USERINFO):

    token = USERINFO.get('USER_TOKEN')
    account = USERINFO.get('ACCOUNT_NAME')
    if 'X-Auth-Token:' in cmd:
        tokenstr = 'X-Auth-Token: %s' % (token)
        cmd = cmd.replace('X-Auth-Token:',tokenstr)
    cmd = cmd.replace('http','https')
    cmd = cmd + ' --cacert ' + crtpath
    # if account:
    #    cmd = cmd + ' >> /root/log/%s' % (account)
    print cmd
    flag , output = commands.getstatusoutput(cmd)
    return flag,output
    
