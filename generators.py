"""Following the work done on generators and maintaining them in the course Core Python: Getting Started
@ https://app.pluralsight.com/course-player?clipId=12303ab8-5371-4e07-bf12-68486f261672

Here we watching how generational functions are executed through debugging it.
"""


# the take generator retrieves a specified number of elements from the front of an iterable
def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


# the distinct generator eliminates duplicate items by keeping track of which element has already bee seen in a set
def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue  # continue skips any values that have already bee yielded
        yield item
        seen.add(item)


def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, list(distinct(items))):
        print(item)


run_pipeline()
