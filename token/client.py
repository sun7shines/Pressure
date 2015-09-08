
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import commands
import os

from level01 import *
from level02 import *
from level03 import *
from testlib import *
from cnlib import apicmds,apikeys

import multiprocessing
import thread
import time

def test(email,passwd,action):


    tenant = email.replace('@','').replace('.','')
    testobj = action

    userinfo = {}

    if testobj != 'token':
        userinfo = set_cache_env(email,passwd)
        if not userinfo:
            print '######################################## faild get user %s token ##########################################' % (tenant)
            return

    testfn = apicmds.get(testobj)
    if testobj == 'token':
        testfn(email,passwd)

    elif testobj != 'all':
        testfn(userinfo)

    if testobj == 'all':
        for key in apikeys:
            if key == 'token':
                continue
            testfn = apicmds.get(key)
            testfn(userinfo)

def thtest(email,passwd,action):

    p = multiprocessing.Process(target=test, name=email,args=(email,passwd,action))
    p.start()
    p.join()
    print '%15s.exitcode = %s' % (p.name, p.exitcode)
 
def main(argv):

    action = 'token'
    num = 2
    if len(argv) == 3:
        action = argv[1]               
        num = int(argv[2])

    if action in ['all','user']:
        cmd = 'rm -rf /home/cloudfs-object/* ; rm -rf /root/log/*'
        print cmd
        os.system(cmd)
        time.sleep(2)

    else:
        cmd = 'rm -rf /root/log/*'
        print cmd
        os.system(cmd)
        time.sleep(2)

    for n in range(0,num):
        email = 'zhu__feng%05dcom' % n
        print email
        passwd = '123456'
        thread.start_new_thread(thtest, (email,passwd,action)) 

    while True:
        print 'sleep\n\n\n'
        time.sleep(5)

if __name__ == '__main__':

    main(sys.argv)

