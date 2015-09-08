# -*- coding:utf-8 -*-

import commands
import testlib

testcasecmd = testlib.testcasecmd
import urllib

def if_02_container_list(USERINFO):
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = '''curl -i http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + ''' -X GET -H "X-Auth-Token: " '''
    cmd = cmd.encode("utf-8")
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_03_container_create(cnta,USERINFO):

    cnta = urllib.quote(cnta)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s -X PUT -H "X-Auth-Token: " ''' % (cnta)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_04_container_delete(cnta,USERINFO):

    cnta = urllib.quote(cnta)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s -X DELETE -H "X-Auth-Token: " ''' % (cnta)
    flag , output = testcasecmd(cmd,USERINFO)
    
    print '\n'.join(output.split('\n')[3:])

def if_05_object_list(cnt,USERINFO):

    cnt = urllib.quote(cnt)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s?op=LISTDIR&recursive=false"  -H "X-Auth-Token: " ''' % (cnt)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])
    
def if_06_object_create(obj,fnsrc,USERINFO):

    obj = urllib.quote(obj)
    fnsrc = urllib.quote(fnsrc)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s -X PUT -H "X-Auth-Token: " -T %s ''' % (obj,fnsrc)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])


def if_07_object_delete(obj,USERINFO):

    obj = urllib.quote(obj)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s -X DELETE -H "X-Auth-Token: " ''' % (obj)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_08_object_copy(obj,dst,USERINFO):

    obj = urllib.quote(obj)
    dst = urllib.quote(dst)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s -X COPY -H "X-Auth-Token: " -H "Destination: /%s" ''' % (obj,dst)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])


def if_09_object_get(obj,USERINFO):

    obj = urllib.quote(obj)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s -X GET -H "X-Auth-Token: " ''' % (obj)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

