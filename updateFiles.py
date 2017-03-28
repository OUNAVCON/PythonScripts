import urllib2
import re
import os

listOfWPM = ['10','13','15']


# will probably want to check to see if the file exists and if so, do nothing.
def retreiveFile(url, subfolder):
 file_name = url.split('/')[-1]
 u = urllib2.urlopen(url)
 if not os.path.exists(subfolder):
    os.makedirs(subfolder)
 filename = subfolder+ '/' + file_name
 if not os.path.isfile(filename):
  f = open(filename, 'wb')
  meta = u.info()
  file_size = int(meta.getheaders("Content-Length")[0])
  print "Downloading: %s Bytes: %s" % (file_name, file_size)
  file_size_dl = 0
  block_sz = 8192
  while True:
    buffer = u.read(block_sz)
    if not buffer:
        break
    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,
  f.close()



#Get the local path we will be writing to directories below here.
dir_path = os.path.dirname(os.path.realpath(__file__))
print dir_path

for wpm in listOfWPM:
 #get the html from the arrl page. This will contain all the mp3 download links.
 url = "http://www.arrl.org/" + wpm +"-wpm-code-archive"
 u = urllib2.urlopen(url)
 htmlText = u.read()

 #read through the html and get all the mp3 url links.
 # could do something similar for the text files as well.
 m = re.findall('(http://?.*mp3)', htmlText);
 for entry in m:
    retreiveFile(entry, wpm + "WPM")

