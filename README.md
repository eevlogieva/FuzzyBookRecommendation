# FuzzyBookRecommendation

This project started as a university project for the course "Fundamentals of Fuzzy Logic" in the University of Amsterdam.
It is an application with a command line interface, used to recommend books to users, based on their book genres preferences.

## Usage

If you want to use the app, clone or download the repo, and run the commands and follow the CLI instructions:

```bash
cd dataProcessing
python3 main.py
```

Here is an example run of the command:

```bash
Hello. If you want us to recommend you a book, please give a grade from 1 to 10 to the following genres:
fiction: 10
non-fiction: 0
Here are some genres that you could choose from and give a grade
['action', 'adventure', 'art', 'biography', 'cartoon', 'chick-lit', 'childrens', 'classics', 'comedy', 'crime', 'drama', 'fantasy', 'history', 'horror', 'mathematics', 'mystery', 'mythology', 'philosophy', 'poetry', 'religion', 'romance', 'science', 'science-fiction', 'short-story', 'thriller']
If you want to see the full list of genres, type 'full', otherwise type <genre>*<grade> <newline>.
when you're done type 'end'
poetry*10
end
{"'fiction'": 10, "'non-fiction'": 0, "'poetry'": 10}
['0345402871', '034540288X', '0425158632', '0425170349', '0060976845']
```

The output of the command `['0345402871', '034540288X', '0425158632', '0425170349', '0060976845']` is a list of ISBNs of books that the app is recommending.
