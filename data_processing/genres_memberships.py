import datetime
# Parse the file with the genres and calculate memberships from 0 to 1 to each genre


def calculate_genre_memberships():
    t = open('../data/books_with_genres.csv', 'r')
    new_file = open('../data/membership_of_genres.csv', 'w')

    starttime = datetime.datetime.now()

    line = t.readline()
    while line:
        # preprocessing of the line to extract the data
        highest_number_of_raters = 0
        elems = line.split(';')
        isbn = elems[1]
        genres = elems[2]
        genres = genres.strip('[').strip(']')

        genres_list = genres.split(', ')
        new_line = []

        # keep the highest number of people that rated this book as a particular genre
        for genre in genres_list:
            elements = genre.split()
            # sometimes the list with genres is empty
            if elements:
                num_people = int(
                    ''.join([i for i in elements[0] if i.isdigit()]))
                if highest_number_of_raters < num_people:
                    highest_number_of_raters = num_people
        # we want the highest rated genre to be with a membership degree of 1, therefore, the
        # normalizer constant is the number of people, rated the highest rated genre
        normalizer = highest_number_of_raters * 1.0
        # for each genre, normalize the value (make it between 0 and 1)
        for genre in genres_list:
            elements = genre.split()
            if elements:
                num_people = int(
                    ''.join([i for i in elements[0] if i.isdigit()]))
                genre_name = elements[-1].strip(']').strip('"')
                new_line.append((genre_name, round(num_people/normalizer, 2)))
        new_file.write(str(isbn) + ';' + str(new_line) + '\n')
        line = t.readline()
    print(datetime.datetime.now() - starttime)


if __name__ == '__main__':
    calculate_genre_memberships()
