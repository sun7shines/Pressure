#!/usr/bin/env python
#coding=utf8

import time
import json
from bridge import *
import os
import string

AUTH_HOST = 'https://124.16.141.142'
AUTH_PORT = 443

#AUTH_HOST = 'http://127.0.0.1'
#AUTH_PORT = 8080

def get_client_token():

    client = bridgeUtil()
    user_param = {}

    url = '%s/oauth/access_token' % (AUTH_HOST)

    user_param['client_id'] = 'hnuclient1'
    user_param['client_secret'] = '34ulL811ANtS70Te'
    user_param['grant_type'] = 'client_credentials'
    user_param['scope'] = 'user'

    result = client.get_client_access_token(url, AUTH_PORT,user_param)
    print result
    return result["access_token"]


def regist_user(client_token):

    client = bridgeUtil()
    user_param = {}

    url = '%s/api/register' % (AUTH_HOST)

    user_param['name'] = 'fw109test3'
    user_param['username'] = 'fw109test3'
    user_param['email'] = 'zhu__feng006@163.com'
    user_param['password'] = '123456'
    user_param['password_confirmation'] = '123456'
    user_param['access_token'] = client_token

    result = client.register_user(url,  AUTH_PORT,user_param)
    return result

def get_user_accessToken(user_email,user_passwd):
    # user_email = 'zhu__feng006@163.com'
    # user_passwd = '123456'
    client = bridgeUtil()
    user_param = {}

    url = '%s/oauth/access_token' % (AUTH_HOST)

    user_param['client_id'] = 'hnuclient1'
    user_param['client_secret'] = '34ulL811ANtS70Te'
    user_param['email'] = user_email
    user_param['password'] = user_passwd
    user_param['grant_type'] = 'password'
    user_param['scope'] = 'user'

    result = client.get_user_access_token(url,  AUTH_PORT,user_param)
    import time
    print time.time()
    print str(result)
    return result["access_token"]

def validateToken(token):

    client = bridgeUtil()
    verify_param = {}

    verify_param['resourcename'] = 'SeAgent'
    verify_param['secret'] = '123456'
    verify_param['access_token'] = token

    url = '%s/api/token-validation' % (AUTH_HOST)
    result = {u'status': u'valid', u'scopes': [u'user'], 
              u'ownerType': u'client', u'owner': u'hnuclient1'}
    
    result = client.verify_user(url,  AUTH_PORT,verify_param)
    return result

def user_test():
    # 获取client的token
    client_token = get_client_token()
    # 利用client的token注册用户
    result = regist_user(client_token)
    print result

def token_test():

    user_token = get_user_accessToken('zhu__feng006@163.com','123456')

    user_info = validateToken(user_token)
    print user_info

def curl_test(user_token,user_info):

    x_auth = 'X-Auth-Token:' +  user_token
    tenant = 'AUTH_' + user_info['owner']['email'].replace('@','').replace('.','')
    print 'curl -i -X PUT -T ufw.log "http://IP:Port/v1/' + tenant + '/temp/ufw.log?op=CREATE&overwrite=true&type=NORMAL" -H "' + x_auth + '"'



if __name__ == '__main__':

#    user_test()
    import pdb;pdb.set_trace()
    token_test()


