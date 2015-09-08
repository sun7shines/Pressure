# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import commands
import os

from level01 import *
from level02 import *
from level03 import *
from testlib import *


def user_test(userinfo):
    if_34_user_init(userinfo)
    account_meta(userinfo)
    container_meta('/normal',userinfo)
    container_meta('/private',userinfo)
    container_meta('/backup',userinfo)
    if_02_container_list(userinfo)
  
def container_test(userinfo):

    if_02_container_list(userinfo)
    if_03_container_create('/测 试',userinfo)
    container_meta('/normal',userinfo)
    if_06_object_create('/测 试/文 件1','/root/install.log',userinfo)
    if_06_object_create('/测 试/文 件2','/root/install.log',userinfo)
    if_27_file_meta('/测 试/文 件2',userinfo)
    if_05_object_list('/测 试',userinfo)
    if_07_object_delete('/测 试/文 件1',userinfo)
    if_07_object_delete('/测 试/文 件2',userinfo)
    if_14_dir_create('/测 试/目 录1/目 录5/目 录3',userinfo)
    if_14_dir_create('/测 试/目 录1/目 录5/目 录4',userinfo)
    if_14_dir_create('/测 试/目 录1/目 录5/目 录3/目 录1',userinfo)
    if_14_dir_create('/测 试/目 录1/目 录5/目 录3/目 录1/目 录7',userinfo)
    if_32_file_list('/测 试/目 录1',userinfo)

    if_02_container_list(userinfo)

def object_test(userinfo):

    if_03_container_create('/对 象',userinfo)
    if_05_object_list('/对 象',userinfo)
    if_06_object_create('/对 象/文 件1','/root/install.log',userinfo)
    if_08_object_copy('/对 象/文 件1','/对 象/文 件2',userinfo)
    if_31_file_permission('/对 象/文 件1',userinfo)
    if_27_file_meta('/对 象/文 件1',userinfo)
    if_05_object_list('/对 象',userinfo)
    if_09_object_get('/对 象/文 件1',userinfo)
    if_07_object_delete('/对 象/文 件2',userinfo)
    if_05_object_list('/对 象',userinfo)
    if_07_object_delete('/对 象/文 件1',userinfo)
    if_05_object_list('/对 象',userinfo)
    if_30_rcy_reset(userinfo)
 
def file_test(userinfo):
    if_11_file_upload('/normal/文 件3', '/root/install.log',userinfo)
    if_27_file_meta('/normal/文 件3',userinfo)
    if_19_copy('/normal/文 件3','/normal/文 件5','f',userinfo)
    if_11_file_upload('/normal/文 件5','/root/install.log',userinfo) 
    if_05_object_list('/normal',userinfo)
    if_17_move('/normal/文 件5','/normal/文 件2','f',userinfo)
    if_05_object_list('/normal',userinfo)
    if_21_file_get('/normal/文 件3',userinfo)
    if_26_rename('/normal/文 件3','/normal/文 件7','f',userinfo)
    if_27_file_meta('/normal/文 件7',userinfo)
    if_15_delete('/normal/文 件7','f',userinfo)
    if_30_rcy_reset(userinfo)
    
def segments_test(userinfo):
    if_12_upload_seg('/segments/段 test/1','seg.install.log.syslog',userinfo)
    if_12_upload_seg('/segments/段 test/2','seg.install.log',userinfo)
    
    if_13_upload_manifest('/segments/段 test/1','9951ef01bc03745e6ebf3b50e990bc67','7572',
                    '/segments/段 test/2','8dd16a3d50854caae6a23917d41688f3','27312','段 test',userinfo)
    
    segs_get('/normal/段 test',userinfo)
    manifest_get('/normal/段 test',userinfo)
    mainfest_delete('/normal/段 test',userinfo)
    if_13_upload_manifest('/segments/段 test/1','9951ef01bc03745e6ebf3b50e990bc67','7572',
                          '/segments/段 test/2','8dd16a3d50854caae6a23917d41688f3','27312','段 test',userinfo)
    
    segs_delete('/normal/段 test',userinfo)
    
    if_30_rcy_reset(userinfo)
    return False

def dir_test(userinfo):
    if_14_dir_create('/normal/目 录1',userinfo)
    if_11_file_upload('/normal/文 件10','/root/install.log',userinfo)
    if_05_object_list('/normal',userinfo)
    if_11_file_upload('/normal/目 录1/文 件3', '/root/install.log',userinfo)
    if_14_dir_create('/normal/目 录1/目 录5',userinfo)
    if_14_dir_create('/normal/目 录1/目 录5/目 录3',userinfo)
    if_14_dir_create('/normal/目 录1/目 录5/目 录4',userinfo)
    if_14_dir_create('/normal/目 录1/目 录5/目 录3/目 录1',userinfo)
    if_14_dir_create('/normal/目 录1/目 录5/目 录3/目 录1/目 录7',userinfo)
    if_32_file_list('/normal/目 录1',userinfo)
    if_05_object_list('/normal',userinfo)
    if_11_file_upload('/normal/目 录1/文 件4', '/root/install.log',userinfo)
    if_32_file_list('/normal/目 录1',userinfo)
    if_19_copy('/normal/目 录1','/normal/目 录3','d',userinfo)
    if_17_move('/normal/目 录1','/normal/目 录2','d',userinfo)
    if_26_rename('/normal/目 录3','/normal/目 录4','d',userinfo)
    if_05_object_list('/normal',userinfo)
    dir_reset('/normal/目 录4',userinfo)
    if_15_delete('/normal/目 录4','d',userinfo)
    
def batch_test(userinfo):

    if_11_file_upload('/normal/批量文 件1', '/root/install.log',userinfo)
    if_11_file_upload('/normal/批量文 件2', '/root/install.log',userinfo)
    if_14_dir_create('/normal/批量目 录1',userinfo)
    if_14_dir_create('/normal/批量目 录2',userinfo)
    if_20_batch_copy("/normal/批量文 件1" ,"/normal/批量文 件3" ,"f",
               "/normal/批量目 录1" ,"/normal/批量目 录3", "d",userinfo)
    if_20_batch_copy("/normal/批量文 件2" ,"/normal/批量文 件4" ,"f",
               "/normal/批量目 录2" ,"/normal/批量目 录4", "d",userinfo)
    if_16_batch_delete('/normal/批量文 件1' ,'f',
                 '/normal/批量目 录1' ,'d',userinfo)
    if_16_batch_delete('/normal/批量文 件2' ,'f',
                 '/normal/批量目 录2' ,'d',userinfo)
    
    if_18_batch_move('/normal/批量文 件3', '/normal/批量文 件1', 'f','/normal/批量目 录4', '/normal/批量目 录2', 'd',userinfo)

    if_16_batch_delete('/normal/批量文 件1' ,'f','/normal/批量目 录2' ,'d',userinfo) 
    if_16_batch_delete('/normal/批量文 件4' ,'f','/normal/批量目 录3' ,'d',userinfo)
    
def vers_test(userinfo):
    ver1_create('/normal/版 本12/版 本_object_test',userinfo)
    ver2_create('/normal/版 本12/版 本_object_test',userinfo)
    ver2_create('/normal/版 本12/版 本_object_test',userinfo)
    if_22_file_history('/normal/版 本12/版 本_object_test',userinfo)
    if_15_delete('/normal/版 本12/版 本_object_test','f',userinfo)
    if_32_file_list('/normal/版 本12',userinfo)
    if_22_file_history('/normal/版 本12/版 本_object_test',userinfo)
    if_17_move('/normal/版 本12/版 本_object_test','/normal/版 本12/版 本_object_test11','f',userinfo)
    if_22_file_history('/normal/版 本12/版 本_object_test11',userinfo)
    if_17_move('/normal/版 本12','/normal/版 本13','d',userinfo) 
    if_22_file_history('/normal/版 本13/版 本_object_test11',userinfo)

def rcy_test(userinfo):
    
    if_11_file_upload('/normal/recycle_文 件','/root/install.log',userinfo)
    if_14_dir_create('/normal/recycle_目 录',userinfo)
    if_15_delete('/normal/recycle_文 件','f',userinfo)
    if_15_delete('/normal/recycle_目 录','d',userinfo)
    if_28_rcy_list(userinfo)
  
def quota_test(userinfo):
    if_33_quota_set('100',userinfo)
    if_10_quota_meta(userinfo)
    quota_remove(userinfo)
    if_10_quota_meta(userinfo)
    if_33_quota_set('8000000000',userinfo)
    if_10_quota_meta(userinfo)
 
def chinese_test(userinfo):

    if_02_container_list(userinfo)
    if_03_container_create('/测 试',userinfo)
    if_02_container_list(userinfo)
    container_meta('/normal',userinfo)
    if_06_object_create('/测 试/文 件1','/root/install.log',userinfo)
    if_06_object_create('/测 试/文 件2','/root/install.log',userinfo)
    if_27_file_meta('/测 试/文 件2',userinfo)
    if_05_object_list('/测 试',userinfo)
    if_07_object_delete('/测 试/文 件1',userinfo)
    if_07_object_delete('/测 试/文 件2',userinfo)
    if_04_container_delete('/测 试',userinfo)
    if_02_container_list(userinfo)
     
def rcym_test(userinfo):
    
    pd = [{"hash": "dir", "uuid": "ldfxETcj-hRVgJL-CJL3", "bytes": 0, "ftype": "d", "time": "1437268676.37665", "path": "/normal/recycle_\u76ee \u5f55", "name": "ldfxETcj-hRVgJL-CJL3"}, {"hash": "8dd16a3d50854caae6a23917d41688f3", "uuid": "viEcQv1T-dmEiKr-Tipa", "bytes": 27312, "ftype": "f", "time": "1437268676.26832", "path": "/normal/recycle_\u6587 \u4ef6", "name": "viEcQv1T-dmEiKr-Tipa"}] 
 
    if_29_rcy_batch(pd[0]['uuid'],pd[0]['path'],pd[0]['ftype'],pd[1]['uuid'],pd[1]['path'],pd[1]['ftype'])
             

def link_test(userinfo):

    if_11_file_upload('/normal/linkfile','/root/install.log',userinfo) 
    if_25_link_create('/normal/linkfile','/normal/linktest',userinfo)
    if_32_file_list('/normal',userinfo)

def operation_test(userinfo):

    if_23_user_op_history(userinfo)
    if_24_user_op_delete(userinfo)
    if_23_user_op_history(userinfo)

def io_test(userinfo):
    if_11_file_upload('/normal/文 件3', '/root/openfileresa-2.99.1-x86_64-disc1.iso',userinfo)
    if_19_copy('/normal/文 件3','/normal/文 件5','f',userinfo)
    if_05_object_list('/normal',userinfo)
    if_15_delete('/normal/文 件3','f',userinfo)
    if_15_delete('/normal/文 件5','f',userinfo)
    if_30_rcy_reset(userinfo)

def cp_test(userinfo):

    if_19_copy('/normal/文 件3','/normal/文 件5','f',userinfo)

def del_test(userinfo):

    if_15_delete('/normal/文 件3','f',userinfo)
    if_15_delete('/normal/文 件5','f',userinfo)
    if_30_rcy_reset(userinfo)

  
apicmds = {'token':if_01_get_token,'user':user_test,'container':container_test,
           'object':object_test,'file':file_test,'segments':segments_test,
           'dir':dir_test,'batch':batch_test,'vers':vers_test,'quota':quota_test,
           'rcy':rcy_test,'rcym':rcym_test,'rcyc':if_30_rcy_reset,'chinese':chinese_test,
           'link':link_test,'operation':operation_test,'io':io_test,'del':del_test,'copy':cp_test}

apikeys = ['token','user','container','object','file','dir','segments','batch','vers','quota','link','operation','rcy']

