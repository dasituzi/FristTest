#-*- coding: utf-8 -*-
import httplib,json,urllib
import socket,struct,binascii
import select
import time,sys
import logging

'''
http request and response
'''
class HttpConnect():
    '''
    CONST in httplib :
    Httplib.HTTP_PORT = 80
    Httplib.OK = 200
    Httplib.NOT_FOUND = 404
    httplib.responses[httplib.NOT_FOUND] = 'Not Found'
    httplib.responses[httplib.OK] = 'OK'

    '''

    def __init__(self,addr,method,url):
        self.addr = addr
        self.method = method
        self.url = url
        self.return_data = ''

        #{'key1':'value1','key2':'value2' ...}
        self.params = urllib.urlencode("")
        self.headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Encoding':'gzip, deflate',
                        'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
                        'Cache-Control':'max-age=0',
                        'Connection':'keep-alive',
                        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0'
                        }
        try:
            self.conn = httplib.HTTPConnection(self.addr)

            if self.method == "GET":
                self.conn.request('GET',self.url)               
            else:
                self.conn.request('POST',self.url,self.params,self.headers)
                print "use POST"

            self.response = self.conn.getresponse()
            self.return_data = self.response.read()

        except Exception,e:
            print e
        finally:
            if self.conn:
                self.conn.close()

    def getResponse(self):
        return self.return_data

    def getVersion(self):
        return self.response.version

    def getStatus(self):
        return self.response.status

    def getHeader(self):
        return self.response.getheaders()

    def getAllMsg(self):
        return self.response.msg

    def getReason(self):
        return self.response.reason


'''
print log 
'''
class Logger():

    def __init__(self,name,level):
        self.name=name
        self.logger=logging.getLogger(self.name)

        level_dict={'debug':logging.DEBUG,'info':logging.INFO,
                    'warning':logging.WARNING,'error':logging.ERROR,
                    'critical':logging.CRITICAL,'':logging.INFO}
        self.level=level_dict[level]
        self.logger.setLevel(self.level)

        self.formatter = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] [%(message)s]")
        self.ch = logging.StreamHandler(sys.stderr)
        self.ch.setFormatter(self.formatter)
        self.logger.addHandler(self.ch)

    def debug(self,debug):
        self.logger.debug(debug)

    def info(self,info):
        self.logger.info(info)

    def warning(self,warning):
        self.logger.warning(warning)

    def error(self,error):
        self.logger.error(error)

    def critical(self,critical):
        self.logger.critical(critical)

'''
ip: xxx.xxx.xxx.xxx  <-change-> int
'''
class ChangeIP():

    def ip2int(self,ip):
        return socket.ntohl(struct.unpack("I",socket.inet_aton(str(ip)))[0])

    def int2ip(self,int_ip):
        return socket.inet_ntoa(struct.pack('I',socket.htonl(int_ip)))

'''
httpserver for test,receive request and return result
run alone
'''
class TCPServer():

    def __init__(self,host,port):
        self.logger=Logger('TCPServer','debug')
        self.host=host
        self.port=port
        self.addr=(self.host,self.port)
        try:
            self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.sock.bind(self.addr)
            self.sock.listen(100)
            print "start, waiting for connect!"
        except:
            print "create socket error!"
            sys.exit()

    def run(self):
        while True:
            try:
                self.new_sock,self.new_addr=self.sock.accept()
                self.new_sock.send('hello')
                self.recv=self.new_sock.recv(1024)

                #use for 0x
                #self.logger.info(binascii.a2b_hex(self.recv))
                #use for String
                self.logger.info(self.recv)
                self.test()

                self.new_sock.close()
            except KeyboardInterrupt:
                print "close server, see you!"
                self.sock.close()
                sys.exit()
            except Exception,e:
                print e
    def test(self):
        print "test"


if __name__ == "__main__":
    h = HttpConnect("jsonview.com:80","GET","/example.json")
    print h.getVersion()

    
    

        
    