import urllib2
import codeskulptor
a_file=urllib2.urlopen (codeskulptor.file2url('assets_sample_text.txt'))
print(a_file.read())
