import os, re, json, urllib2

user = 'Tsutomu-KKE@github'

def getweb(url):
	fp = urllib2.urlopen(url)
	s = fp.read()
	fp.close()
	return json.loads(s)

fr = open('README.md', 'w')
fr.write('Posts on Qiita\n=====\n\n')
for i in xrange(1, 100):
	url = 'https://qiita.com/api/v1/users/%s/items?page=%s' % (user, i)
	lst = getweb(url)
	if (len(lst) == 0): break
	for dic in lst:
		tit = re.sub('[~`!@#$%^&*=+{}\\|;:"\',<.>/?]', '', re.sub('<[^>]*?>', '', dic['title']))
		url2 = dic['url']
		fr.write(('* [%s](%s  "see on Qiita")\n' % (tit, url2)).encode('utf-8'))
		fp = open(tit.encode('shift_jis') + '.md', 'w')
		url3 = 'https://qiita.com/api/v1/items/%s' % dic['uuid'].encode('utf-8')
		dic2 = getweb(url3)
		fp.write(dic2['raw_body'].encode('utf-8'))
		fp.close()
fr.close()
os.system('git add -A')
os.system('git commit -am "auto"')
os.system('git push origin master')

