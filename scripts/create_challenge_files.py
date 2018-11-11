import mechanicalsoup
import sys

def _get_challenge_itens():
    page = browser.get_current_page()
    challenge_list = page.find("div", {"class": "intro-toc list-group"})
    challenge_itens = challenge_list.find_all('a')

    return challenge_itens

def _get_filenames():
    filenames = []
    challenge_itens = _get_challenge_itens()
    for challenge_item in challenge_itens:
        href = challenge_item['href']
        challenge_name = "{name}.{extension}".format(name=(href.split('/')[3]), extension=EXTENSION)
        filenames.append(challenge_name)

    return filenames

def create_files():
    filenames = _get_filenames()
    for filename in filenames: 
        open(PATH + filename, 'w').close()


if __name__ == '__main__':
    PATH = '../javascript_algorithms_and_data_structures_certification/basic-javascript/'
    URL = sys.argv[1]
    EXTENSION = sys.argv[2]

    browser = mechanicalsoup.StatefulBrowser()
    browser.open(URL)
    create_files()