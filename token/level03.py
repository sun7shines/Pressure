# -*- coding:utf-8 -*-

import commands
import testlib
import urllib
testcasecmd = testlib.testcasecmd

from request_validate_token import get_user_accessToken,validateToken
from level02 import if_01_get_token

def account_meta(USERINFO):
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = '''curl -i http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + ''' -X META -H "X-Auth-Token: " ''' 
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])
    
def container_meta(cnt,USERINFO):
      
    cnt = urllib.quote(cnt)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = '''curl -i http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s -X META -H "X-Auth-Token: " ''' % (cnt)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])
    

def segs_get(obj,USERINFO):

    obj = urllib.quote(obj)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    
    cmd = ''' curl -i "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s" -X GET -H "X-Auth-Token: " ''' % (obj)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def manifest_get(obj,USERINFO):

    obj = urllib.quote(obj)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    
    cmd = ''' curl -i "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s?multipart-manifest=get" -X GET -H "X-Auth-Token: " ''' % (obj)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def segs_delete(obj,USERINFO):

    obj = urllib.quote(obj)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    
    cmd = ''' curl -i "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s?multipart-manifest=delete" -X DELETE -H "X-Auth-Token: " ''' % (obj)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def mainfest_delete(obj,USERINFO):
    
    obj = urllib.quote(obj)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s" -X DELETE -H "X-Auth-Token: " ''' % (obj)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])
    
def quota_remove(USERINFO):

    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i -X POST http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + ''' -H "X-Auth-Token: " -H "X-Remove-Account-Meta-Quota-Bytes: 1" '''
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def set_cache_env(email,passwd):

    USERINFO = {'USER_TOKEN': '','ACCOUNT_NAME':''}    

    msg = if_01_get_token(email,passwd)
    if not msg:
        print 'set cache evn faild'
        return None
    USERINFO['USER_TOKEN'] = msg['access_token'] 
    USERINFO['ACCOUNT_NAME'] = 'AUTH_' + email.replace('@','').replace('.','')
   
    return USERINFO
 
def dir_reset(direr,USERINFO):

    direr = urllib.quote(direr)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i -X PUT "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s?op=RESET&ftype=d&recursive=true&type=NORMAL" \
-H "X-Auth-Token: " ''' % (direr)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])
   

def ver1_create(obj,USERINFO):

    obj = urllib.quote(obj)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i -X PUT --data-binary 1 "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s?&overwrite=true" -H "X-Auth-Token: " ''' % (obj)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])
    

def ver2_create(obj,USERINFO):

    obj = urllib.quote(obj)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i -X PUT --data-binary 2 "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s?&overwrite=true" -H "X-Auth-Token: " ''' % (obj)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])
 
