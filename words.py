""" This follows the words.py work in Core Python: Getting Started: https://app.pluralsight.com/course-player?clipId=d9831185-9fc1-4707-8d8d-b6a7608feb12"""

# imports
import sys
from urllib.request import urlopen


# creating a function fetching the words
def fetch_words(url):
    # open story
    story = urlopen(url)

    # get each word in story
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


# dunder name
# print(__name__)  # __name__ here is the name of the file either as words or main, depending on how you're running it
#
# # testing the value of the dunder name
# if __name__ == '__main__':
#     fetch_words()

# print one word per line
def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    url = ''
    indicator = sys.argv[1]
    if indicator == 1:
        url = 'http://sixty-north.com/c/t.txt'
        main(url)
