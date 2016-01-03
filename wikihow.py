# BeautifulSoup for parsing
from bs4 import BeautifulSoup

# urlopen for downloading
from urllib.request import urlopen

# our site
site = "http://ru.wikihow.com/"

def id_to_url(id):
    " Conver article id to url for this article "

    # api to convert id to url
    api_html = urlopen('{0}/api.php?action=query&prop=info&pageids={1}&inprop=url&format=xml'.format(site,id))\
        .read().decode()

    # parse it!
    root = BeautifulSoup(api_html, "html.parser")

    # return our url
    return root.page['fullurl']



def get_random():
    " Get random id and title of this id "

    # api url to get random page id and title
    api_html = urlopen('%s/api.php?action=query&list=random&rnlimit=1&format=xml' % site).read().decode()

    # parse it!
    root = BeautifulSoup(api_html, "html.parser")

    # get id and title from it
    id, title = root.page['id'],'Как '+root.page['title']

    # return it!
    return id, title

def get_steps(url):
    " get steps by url "

    # api url to get random page id and title
    api_html = urlopen(url).read().decode()

    # parse it!
    root = BeautifulSoup(api_html, "html.parser")

    # get steps (it contain html)
    steps = root.findAll("b", { "class": "whb"})

    # We need to remove html from every step
    for i in range(0,len(steps)):
        steps[i] = steps[i].text

    # return it
    return steps

# Bind id and title
id, title = get_random()

# return title
print(title,"\n")

# return steps
for step in get_steps(id_to_url(id)):
    print(step)

