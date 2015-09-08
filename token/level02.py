# -*- coding:utf-8 -*-

import commands
import testlib
import simplejson as json
import urllib
testcasecmd = testlib.testcasecmd
import traceback

def if_01_get_token(email,passwd):

    cmd = ''' curl -X POST -d '{"password": "%s", "email":"%s"}' https://localhost:443/oauth/access_token --cacert /root/task/api/ssl6/ca.crt'''  % (passwd,email)
    print cmd    
    flag,output = commands.getstatusoutput(cmd)
    output1 =  '\n'.join(output.split('\n')[3:])
    message = ''

    try:
        message = json.loads(output1)
    except:
        print str(traceback.format_exc())
    print output1

    return message 

def if_10_quota_meta(USERINFO):

    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i -X GET "http://localhost:443/v1/%s/quota?op=info&type=NORMAL"''' % (ACCOUNT_NAME) + ''' -H "X-Auth-Token: " '''
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_11_file_upload(obj,src,USERINFO):

    obj = urllib.quote(obj)
    src = urllib.quote(src)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')

    cmd = ''' curl -i "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + \
'''%s?op=CREATE&overwrite=true&type=NORMAL&metadata=helloworld&mode=ENCRYPT&storetype=USER" \
-X PUT -H "X-Auth-Token: " -T %s ''' % (obj,src)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])


def if_12_upload_seg(obj,src,USERINFO):

    obj = urllib.quote(obj)
    src = urllib.quote(src)
    
    if_11_file_upload(obj,src,USERINFO)

def if_13_upload_manifest(path1,etag1,size1,path2,etag2,size2,dst,USERINFO):

    path1 = urllib.quote(path1)
    path2 = urllib.quote(path2)
    dst = urllib.quote(dst)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')

    cmd = ''' curl -i -X PUT -d '[\
{"path": "%s","etag":"%s","size_bytes": %s},\
{"path":"%s","etag":"%s","size_bytes": %s}]' \
"http://localhost:443/v1/%s''' % (path1,etag1,size1,path2,etag2,size2,ACCOUNT_NAME) + '''/normal/%s?multipart-manifest=put&overwrite=true"  \
-H "X-Auth-Token: " -H "X-Static-Large-Object: True" ''' % (dst)

    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_14_dir_create(direr,USERINFO):

    direr = urllib.quote(direr)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i -X PUT "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s?op=MKDIRS&ftype=d&type=NORMAL" -H "X-Auth-Token: " ''' % (direr)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_15_delete(direr,ftype,USERINFO):

    direr = urllib.quote(direr)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i -X DELETE "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s?op=DELETE&ftype=%s&recursive=true&type=NORMAL&cover=true" \
-H "X-Auth-Token: " ''' % (direr,ftype)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_16_batch_delete(p1,ft1,p2,ft2,USERINFO):
    
#    p1 = urllib.quote(p1)
#    p2 = urllib.quote(p2)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i -X POST -d '{"list":[{"path":"%s","ftype":"%s"},{"path":"%s","ftype":"%s"}]}' \
"http://localhost:443/v1/%s''' % (p1,ft1,p2,ft2,ACCOUNT_NAME) + '''/batch?op=DELETE&type=NORMAL" -H "X-Auth-Token: " '''
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_17_move(direr,dst,ftype,USERINFO):

    direr = urllib.quote(direr)
    dst = urllib.quote(dst)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i -X PUT "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s?op=MOVE&ftype=%s&type=NORMAL" -H "X-Auth-Token: " \
-H "Destination: %s" ''' % (direr,ftype,dst)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_18_batch_move(f1,t1,ft1,f2,t2,ft2,USERINFO):

#    f1 = urllib.quote(f1)
#    f2 = urllib.quote(f2)
#    t1 = urllib.quote(t1)
#    t2 = urllib.quote(t2)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i -X POST -d '{"list":[{"from":"%s","to":"%s","ftype":"%s"},{"from":"%s","to":"%s","ftype":"%s"}]}' \
"http://localhost:443/v1/%s''' % (f1,t1,ft1,f2,t2,ft2,ACCOUNT_NAME) + '''/batch?op=MOVE&type=NORMAL" -H "X-Auth-Token: " '''
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])


def if_19_copy(direr,dst,ftype,USERINFO):

    direr = urllib.quote(direr)
    dst = urllib.quote(dst)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i -X PUT "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s?op=COPY&ftype=%s&type=NORMAL" -H "X-Auth-Token: " \
-H "Destination: %s" ''' % (direr,ftype,dst)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])


def if_20_batch_copy(f1,t1,ft1,f2,t2,ft2,USERINFO):

#    f1 = urllib.quote(f1)
#    f2 = urllib.quote(f2)
#    t1 = urllib.quote(t1)
#    t2 = urllib.quote(t2)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i -X POST -d \
'{"list":[{"from":"%s","to":"%s","ftype":"%s"},{"from":"%s","to":"%s","ftype":"%s"}]}' \
"http://localhost:443/v1/%s''' % (f1,t1,ft1,f2,t2,ft2,ACCOUNT_NAME) + '''/batch?op=COPY&type=NORMAL" -H "X-Auth-Token: " '''
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_21_file_get(obj,USERINFO):

    obj = urllib.quote(obj)
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i -L "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s?op=OPEN&offset=0&length=10&type=NORMAL&version=LATEST&mode=NORMAL" -X GET -H "X-Auth-Token: " ''' % (obj)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_22_file_history(obj,USERINFO):

    obj = urllib.quote(obj)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i -L "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s?op=GETHISTORY&type=NORMAL" -H "X-Auth-Token: " ''' % (obj)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_23_user_op_history(USERINFO):

    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i -X GET "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''?op=GET_OP_HISTORY&recent=10" -H "X-Auth-Token: " ''' 
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_24_user_op_delete(USERINFO):

    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i -L GET "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''?op=DELETE_HISTORY&recent=5" -H "X-Auth-Token: " ''' 
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_25_link_create(direr,dst,USERINFO):

    direr = urllib.quote(direr)
    dst = urllib.quote(dst)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i -X PUT "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s?op=CREATESYMLINK&destination=%s&type=NORMAL" \
-H "X-Auth-Token: " ''' % (direr,dst)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_26_rename(direr,dst,ftype,USERINFO):

    direr = urllib.quote(direr)
    dst = urllib.quote(dst)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i -X PUT "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s?op=RENAME&destination=%s&ftype=%s&type=NORMAL" -H "X-Auth-Token: " ''' % (direr,dst,ftype)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_27_file_meta(obj,USERINFO):

    obj = urllib.quote(obj)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')

    cmd = ''' curl -i "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s?op=GETFILEATTR&type=NORMAL&overwrite=LATEST" -H "X-Auth-Token: " ''' % (obj)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_28_rcy_list(USERINFO):

    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''/recycle/user?op=GETRECYCLER&start=0&limit=10&type=NORMAL" -H "X-Auth-Token: " ''' 
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_29_rcy_batch(u1,p1,f1,u2,p2,f2,USERINFO):

#    p1 = urllib.quote(p1)
#    p2 = urllib.quote(p2)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')

    cmd = ''' curl -i -X POST -d '{"list":[{"uuid":"%s","path":"%s","ftype":"%s"},\
{"uuid":"%s","path":"%s","ftype":"%s"}]}' \
"http://localhost:443/v1/%s''' % (u1,p1,f1,u2,p2,f2,ACCOUNT_NAME) + '''/batch?op=MOVERECYCLE&type=NORMAL&overwrite=true" \
-H "X-Auth-Token: " '''
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_30_rcy_reset(USERINFO):

    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')

    cmd = ''' curl -i -X POST "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''/clearrecycle?op=RECYCLER&type=NORMAL" -H "X-Auth-Token: "  '''
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_31_file_permission(obj,USERINFO):

    obj = urllib.quote(obj)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')

    cmd = ''' curl -i -X PUT "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s?op=SETPERMISSION&type=NORMAL"  -H "X-Auth-Token: " -H "X-Object-Permisson: 500" ''' % (obj)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_32_file_list(cnt,USERINFO):

    cnt = urllib.quote(cnt)
    
    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')

    cmd = ''' curl -i "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''%s?op=LISTDIR&recursive=true&type=NORMAL&ftype=d" -X GET -H "X-Auth-Token: " ''' % (cnt)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_33_quota_set(qbytes,USERINFO):

    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i -X POST "http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''/quota?op=createstorage" -H "X-Auth-Token: " -H "X-Account-Meta-Quota-Bytes: %s" ''' % (qbytes)
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])

def if_34_user_init(USERINFO):

    ACCOUNT_NAME = USERINFO.get('ACCOUNT_NAME')
    cmd = ''' curl -i http://localhost:443/v1/%s''' % (ACCOUNT_NAME) + '''/register  -X PUT -H "X-Auth-Token: " '''
    flag , output = testcasecmd(cmd,USERINFO)
    print '\n'.join(output.split('\n')[3:])


