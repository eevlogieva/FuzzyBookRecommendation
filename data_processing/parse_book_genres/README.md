# Parse book genres

The first dataset used for this project is a dataset provided ftom the University of Freiburg (<http://www2.informatik.uni-freiburg.de/~cziegler/BX/>).
However, it contais only the book's ISBN, title and author, and for the purpose of the project we need the book's genres.

Therefore, in the `parser.py` there is a script that for the ISBNs in BX-Books.csv crawls the goodreads.com site and extracts the genres of the book.

It creates a books_with_genres.csv file. Currently in the BX dataset there are over 270 000 books, but due ot the limited amount of time crawling, in books_with_genres.csv we have collected info for about 35 000 of them.
