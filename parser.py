import bs4
import requests
import re

domain = 'http://example.com/'

with open('items.list', 'r') as itemsurls:
    for line in itemsurls:

        s=requests.get(line)
        b=bs4.BeautifulSoup(s.text, "html.parser")

        artp=b.find_all('p')
        art=artp[11]
        artnum=re.findall(r'\d+', str(art))
        images=b.select(".img > a")
	
        urls = []
        for i in range(len(images)):
            urls.append(images[i]['href'])
	

        for image in urls:
            url=domain + str(image)
            print('Downloading: ' + url)
            if urls.index(image) == 0:
                filename=artnum[0] + '.jpg'
                f=open(filename, 'wb')
                urlget = requests.get(url)
                f.write(urlget.content)
                print('Saved as: ' + filename)
                f.close()
            else:
                filename=artnum[0] + '_' + str(urls.index(image)) + '.jpg'
                f=open(filename, 'wb')
                urlget = requests.get(url)
                f.write(urlget.content)
                print('Saved as: ' + filename)
                f.close()

