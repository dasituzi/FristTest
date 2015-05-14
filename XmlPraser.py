#-*- coding: utf-8 -*-
from xml.etree import ElementTree as ET
import urllib2

testPageName = "SchedulerTest026"
#testUrl = "http://192.168.16.81:2020/SchedulerTest026?suite&format=xml"
testUrl = "http://localhost:9090/MultiverseTest?suite&format=xml"

def openWeb(testUrl):
    req = urllib2.Request(testUrl)
    req.add_header("charset","utf-8")
    resp_stream = urllib2.urlopen(req)
    return resp_stream.read()

def saveResult(testURL):    
    workDir = "e:/"    
    resultFile = workDir + "%s.xml"  %testPageName
    f1 = file(resultFile,'w')
    f1.write(openWeb(testURL))
    f1.flush
    f1.close
    return resultFile 

res=ET.parse(saveResult(testUrl))
results = res.findall("./result")

for result in results:
    counts=result.findall('./counts')
    pageNames = result.findall('./relativePageName')
    
    for page in pageNames:
        pageName = page.text
        print "接口 ：", pageName
        
#    sumOfCases = 0
    for count in counts:  
        for child in count.getchildren():
            print child.tag,':',child.text    
 #           sumOfCases = sumOfCases + int(child.text);
        print '--------------'

sumofRights = 0
rights = res.getiterator('right')
for right in rights:
    sumofRights += int(right.text)

sumofWrongs = 0
wrongs = res.getiterator('wrong')
for wrong in wrongs:
    sumofWrongs += int(wrong.text)

sumofIgnores = 0
ignores = res.getiterator('ignores')
for ignore in ignores:
    sumofIgnores += int(ignore.text)
    
sumofExceptions = 0
exceptions = res.getiterator('exceptions')
for exception in exceptions:
    sumofExceptions += int(exception.text)

finalCounts=res.findall('./finalCounts')
numOfInterfaces = 0
for count in finalCounts: 
    for child in count.getchildren(): 
#        print child.tag,':',child.text
        numOfInterfaces += int(child.text)
    rightOfInterfaces = int(count[0].text)
    wrongOfInterfaces = int(count[1].text)
    ignoresOfInterfaces = int(count[2].text)
    exceptionOfInterfaces = int(count[3].text)

RunTime = res.getiterator('totalRunTimeInMillis')[0].text
print '*' * 30
print "测试用例总数: ", sumofRights - rightOfInterfaces + sumofWrongs - wrongOfInterfaces + sumofIgnores - ignoresOfInterfaces + sumofExceptions - exceptionOfInterfaces
print '-' * 18
print "测试通过用例数：",sumofRights - rightOfInterfaces
print "测试失败用例数：",sumofWrongs - wrongOfInterfaces
print "测试忽略用例数：",sumofIgnores - ignoresOfInterfaces
print "测试异常用例数：",sumofExceptions - exceptionOfInterfaces
print '*' * 30
print "测试接口数: ", numOfInterfaces
print '-' * 18
print "测试通过的接口数：",rightOfInterfaces
print "测试失败的接口数：",wrongOfInterfaces
print "测试忽略的接口数：",ignoresOfInterfaces
print "测试异常的接口数：",exceptionOfInterfaces
print '*' * 30
print "测试执行时间：",RunTime," ms"
print '*' * 30
