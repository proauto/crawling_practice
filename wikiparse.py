#!C:\Python34\python.exe
import xml.etree.ElementTree as etree
import urllib.parse, sys

# for mac
#wikifile = "/Users/ihong-gyu/Downloads/kowiki-latest-pages-articles.xml"
# for window
wikifile = "C://Users/hong/Downloads/kowiki-latest-pages-articles.xml"
ns = "{http://www.mediawiki.org/xml/export-0.10/}"
dcount = 0
dlimit = 10000
if len(sys.argv) > 1:
        dlimit = int(sys.argv[1])
filecount = 1;
idxfilename = "data/kowiki%d.idx"%filecount
for event, elem in etree.iterparse(wikifile,events=('start','end')):
        if event == 'end':
                if elem.tag == ns+"page":
                        if dcount == 0:
                                fidx = open(idxfilename,'w',encoding='UTF-8')
                                print("\nwriting %s"%idxfilename)
                        dcount += 1
                        print("\r%d"%dcount,end="",flush=True)
                        for first in elem.getchildren():
                                if first.tag == ns+"title":
                                        stitle = urllib.parse.quote_plus(first.text)
                                        fidx.write("#DREREFERENCE http://ko.wikipedia.org/wiki/%s\n"%stitle)
                                        fidx.write("#DRETITLE %s\n"%first.text)
                                if first.tag == ns+"id":
                                        fidx.write("#DREFIELD wiki_id=%s\n"%first.text)
                                if first.tag == ns+"revision":
                                        for second in first.getchildren():
                                                if second.tag == ns+"timestamp":
                                                        fidx.write("#DREDATE %s\n"%second.text)
                                                if second.tag == ns+"text":
                                                        fidx.write("#DRECONTENT\n%s\n"%second.text)
                        fidx.write("#DREENDDOC\n")
                        if dcount == dlimit:
                                filecount += 1
                                dcount = 0
                                fidx.write("#DREENDDATANOOP\n")
                                fidx.close()
                                idxfilename = "data/kowiki{}.idx".format(filecount)
                        elem.clear()
if dcount > 0 and dcount < dlimit:
	fidx.write("#DREENDDATANOOP\n")
	fidx.close()

