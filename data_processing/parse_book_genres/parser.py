# the parameters that the script takes is the starting index (from where to scrape)
# and the number of books to scrape at once
import requests
import traceback
import time
import sys
from lxml import html
import datetime


def scrape_genres(start_index, number_of_books_at_once):
    filename = 'books_with_genres' + str(start_index) + '.csv'
    new_file = open(filename, 'w')
    starttime = datetime.datetime.now()
    with open('./../../data/informatik_freiburg/BX-Books.csv', 'r') as t:
        for i in range(start_index+1):
            next(t, None)
        i = 0    
        for line in t:
          if i < number_of_books_at_once:
              parse_genres_from_goodreads(new_file, line)
              i += 1

    print(datetime.datetime.now() - starttime)

def parse_genres_from_goodreads(file_to_write, line):
    try:
        els = line.split(';')
        isbn = els[0].strip('"')
        url = "https://www.goodreads.com/search?q=" + isbn
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
        page = requests.get(url, headers=headers)
        root = html.document_fromstring(page.text)
        # e = root.xpath('.//a[@class="actionLinkLite bookPageGenreLink"]')
        genresList = root.xpath(
            './/a[@class="actionLinkLite greyText bookPageGenreLink"]')
        etexts = [ei.attrib['title'] for ei in genresList]
        # limit the number of genres to 5, because otherwise we have a lot of books
        # with very low membership degree to a certain genre
        if len(etexts) > 5:
            while len(etexts) > 5:
                del etexts[5]
        newline = str(isbn) + ';' + str(etexts) + '\n'
        file_to_write.write(newline)
        time.sleep(0.1)
    except Exception:
        traceback.print_exc()
        file_to_write.close()


if __name__ == '__main__':
    scrape_genres(int(sys.argv[1]), int(sys.argv[2]))
