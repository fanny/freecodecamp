import mechanicalsoup
import sys

url = sys.argv[1]
extension = sys.argv[2]

browser = mechanicalsoup.StatefulBrowser()
browser.open(url)

page = browser.get_current_page()
challenge_list = page.find("div", {"class": "intro-toc list-group"})
challenge_itens = challenge_list.find_all('a')

filenames = []
for challenge_item in challenge_itens:
    href = challenge_item['href']
    challenge_name = "{name}.{extension}".format(name=(href.split('/')[3]), extension=extension)
    filenames.append(challenge_name)

for filename in filenames:
    open(filename, 'w')