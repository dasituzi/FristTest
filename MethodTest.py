from fit.ColumnFixture import ColumnFixture

from common import *

'''
when code from windows to linux, use following 
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class MethodTest(ColumnFixture):

    _typeDict={"yourName":"String",
               "sayHi":"String",
               "connect":"String",
               "res":"String",
               "addr":"String",
               "method":"String",
               "url":"String",
               "testJson":"String"}
                       
    def sayHi(self):
        return "hi "+self.yourName

    def connect(self):
        self.conn = HttpConnect("192.168.16.49:3331","GET","/mgmt?cmd=getms")
        self.res = self.conn.getResponse()
        return self.res.strip().replace("\r","")

    def testJson(self):
        self.conn = HttpConnect(self.addr,self.method,self.url)
        self.res = self.conn.getResponse()
        return self.res.strip().replace("\r","")

#a = MethodTest()
#print a.testJson("pm.funshion.com:80","GET","/v5/media/profile?id=109725&cl=iphone&ve=1.1.1.1&uc=1")
#print a.testJson("jsonview.com:80","GET","/example.json")
#print a.testJson("www.baidu.com","GET","/")
#print a.testJson("192.168.16.49:3331","GET","/mgmt?cmd=getms").strip().replace("\r","")
