
import BaseHTTPServer  
import urlparse  
import urllib
try:
    import simplejson as json
except ImportError:
    import json

def transDicts(params):
    dicts={}
    if len(params)==0:
        return
    params = params.split('&')
    for param in params:
        dicts[param.split('=')[0]]=param.split('=')[1]
    return dicts

class WebRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):  
    def do_GET(self):  
        """ 
        """  
        parsed_path = urlparse.urlparse(self.path)  
        message_parts = [  
                'CLIENT VALUES:',  
                'client_address=%s (%s)' % (self.client_address,  
                                            self.address_string()),  
                'command=%s' % self.command,  
                'path=%s' % self.path,  
                'real path=%s' % parsed_path.path,  
                'query=%s' % parsed_path.query,  
                'request_version=%s' % self.request_version,  
                '',  
                'SERVER VALUES:',  
                'server_version=%s' % self.server_version,  
                'sys_version=%s' % self.sys_version,  
                'protocol_version=%s' % self.protocol_version,  
                '',  
                'HEADERS RECEIVED:',  
                ]  
        for name, value in sorted(self.headers.items()):  
            message_parts.append('%s=%s' % (name, value.rstrip()))  
        message_parts.append('')  
        message = '\r\n'.join(message_parts)
 
        datas=self.rfile.read(int(self.headers['content-length']))
        datas=urllib.unquote(datas).decode("utf-8",'ignore')
        datas=transDicts(datas)
        xuser = datas['email'].replace('@','').replace('.','')

        if self.path.startswith('/oauth/access_token'):
            http_data = {u'access_token': u'gPDcsIChk0n5F209fXl6gLGzwa0cdIznMKi88CuM'+xuser, u'token_type': u'Bearer', u'expires': 1431328576, u'expires_in': 604800, u'refresh_token': u'XahhuShAedzGmwrnRPfwW4TopIProSICIM3it88e'}
            message = json.dumps(http_data) 

        elif self.path.startswith('/api/token-validation'):
            http_data = {u'status': u'valid', u'scopes': [u'user'], u'ownerType': u'user', u'owner': {u'username': u'fw109test3', u'remember_token': None, u'name': u'fw109test3', u'email': u'zhu__feng006@163.com'}} 
            message = json.dumps(http_data)

        print message
        self.send_response(200)  
        self.end_headers()  
        self.wfile.write(message)  

    def do_POST(self):
        self.do_GET()  

server = BaseHTTPServer.HTTPServer(('0.0.0.0',8080), WebRequestHandler)  
server.serve_forever()  
