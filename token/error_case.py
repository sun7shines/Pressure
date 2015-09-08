
import os

def case1():
    os.system(' rm -rf /mnt/cloudfs-object/zhu__feng006163com/normal/*; rm -rf /mnt/cloudfs-object/zhu__feng006163com/normal_versions/*')

    cmd = ''' curl -i "https://localhost:443/v1/AUTH_zhu__feng006163com/normal/apple?overwrite=false&metadata=\{\"size\":\"2346\",\"color\":\"red\"\}&mode=NORMAL&storetype=USER" -X PUT -H "X-Auth-Token: 8KpbsOYLaW2iVxUAL37lJIDEhW5mTQrt5GO9Bmgz " -T /root/install.log  --cacert /root/task/api/ssl/ssl_dir/ca.crt '''
    os.system(cmd)

    cmd = ''' curl -i -X PUT "https://localhost:443/v1/AUTH_zhu__feng006163com/normal/ff?op=MKDIRS&type=NORMAL" -H "X-Auth-Token: 8KpbsOYLaW2iVxUAL37lJIDEhW5mTQrt5GO9Bmgz "   --cacert /root/task/api/ssl/ssl_dir/ca.crt '''
    os.system(cmd)


    cmd = ''' curl -i -X PUT "https://localhost:443/v1/AUTH_zhu__feng006163com/normal/apple?op=MOVE&ftype=f&type=NORMAL" -H "X-Auth-Token: 8KpbsOYLaW2iVxUAL37lJIDEhW5mTQrt5GO9Bmgz "   --cacert /root/task/api/ssl/ssl_dir/ca.crt -H "Destination: /normal/ff/apple" '''
    os.system(cmd)


    cmd = ''' curl -i "https://localhost:443/v1/AUTH_zhu__feng006163com/normal?op=LISTDIR&recursive=true" -H "X-Auth-Token: 8KpbsOYLaW2iVxUAL37lJIDEhW5mTQrt5GO9Bmgz "   --cacert /root/task/api/ssl/ssl_dir/ca.crt '''
    os.system(cmd)

def case2():

    cmd = ''' curl -i "https://localhost:443/v1/AUTH_zhu__feng006163com/normal/quotafile1?overwrite=false&mode=NORMAL&storetype=USER" -X PUT -H "X-Auth-Token: 8KpbsOYLaW2iVxUAL37lJIDEhW5mTQrt5GO9Bmgz " -T /root/CentOS-6.5-x86_64-bin-DVD2.iso  --cacert /root/task/api/ssl/ssl_dir/ca.crt '''
    os.system(cmd)

    cmd = ''' curl -i -X GET "https://localhost:443/v1/AUTH_zhu__feng006163com/quota?op=info&type=NORMAL" -H "X-Auth-Token: 8KpbsOYLaW2iVxUAL37lJIDEhW5mTQrt5GO9Bmgz "  --cacert /root/task/api/ssl/ssl_dir/ca.crt  ''' 
    os.system(cmd)

    cmd = ''' curl -i "http://localhost:8081/v1/AUTH_zhu__feng006163com/normal/quotafile2?overwrite=false&mode=NORMAL&storetype=USER" -X PUT -H "X-Auth-Token: 8KpbsOYLaW2iVxUAL37lJIDEhW5mTQrt5GO9Bmgz " -T /root/CentOS-6.5-x86_64-bin-DVD2.iso  --cacert /root/task/api/ssl/ssl_dir/ca.crt '''
    os.system(cmd)
    
    cmd = ''' curl -i -X DELETE "https://localhost:443/v1/AUTH_zhu__feng006163com/normal/quotafile1?ftype=f" -H "X-Auth-Token: 8KpbsOYLaW2iVxUAL37lJIDEhW5mTQrt5GO9Bmgz "  --cacert /root/task/api/ssl/ssl_dir/ca.crt'''
    os.system(cmd)
  
def case3():

    os.system('rm -rf /mnt/cloudfs-object/zhu__feng006163com/normal/apple /mnt/cloudfs-object/zhu__feng006163com/normal/a*')
    cmd = ''' curl -i "https://localhost:443/v1/AUTH_zhu__feng006163com/normal/apple?overwrite=false&mode=NORMAL&storetype=USER" -X PUT -H "X-Auth-Token: 8KpbsOYLaW2iVxUAL37lJIDEhW5mTQrt5GO9Bmgz " -T /root/install.log  --cacert /root/task/api/ssl/ssl_dir/ca.crt '''
    print cmd
    os.system(cmd)

    cmd = ''' curl -i "https://localhost:443/v1/AUTH_zhu__feng006163com/normal/apple?async=true" -X COPY -H "X-Auth-Token: 8KpbsOYLaW2iVxUAL37lJIDEhW5mTQrt5GO9Bmgz " -H "Destination: /normal/a2"  --cacert /root/task/api/ssl/ssl_dir/ca.crt ''' 
    print cmd
    os.system(cmd)
    cmd = ''' curl -i -X DELETE "https://localhost:443/v1/AUTH_zhu__feng006163com/normal/a2?ftype=f" -H "X-Auth-Token: 8KpbsOYLaW2iVxUAL37lJIDEhW5mTQrt5GO9Bmgz "  --cacert /root/task/api/ssl/ssl_dir/ca.crt'''
#    os.system(cmd)

    cmd = ''' curl -i "https://localhost:443/v1/AUTH_zhu__feng006163com/normal/apple?async=true" -X COPY -H "X-Auth-Token: 8KpbsOYLaW2iVxUAL37lJIDEhW5mTQrt5GO9Bmgz " -H "Destination: /normal/a3"  --cacert /root/task/api/ssl/ssl_dir/ca.crt '''
    os.system(cmd)

    cmd = ''' curl -i -X DELETE "https://localhost:443/v1/AUTH_zhu__feng006163com/normal/a2?ftype=f" -H "X-Auth-Token: 8KpbsOYLaW2iVxUAL37lJIDEhW5mTQrt5GO9Bmgz "  --cacert /root/task/api/ssl/ssl_dir/ca.crt'''
#    os.system(cmd)
    cmd = ''' curl -i -X GET "https://localhost:443/v1/AUTH_zhu__feng006163com?op=GET_OP_TASK&tx_id=10" -H "X-Auth-Token: 8KpbsOYLaW2iVxUAL37lJIDEhW5mTQrt5GO9Bmgz "  --cacert /root/task/api/ssl/ssl_dir/ca.crt '''
    print cmd

if __name__ == "__main__":
    case1()
    case3()
