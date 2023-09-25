#!/usr/bin/python3

from requests import get
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = get(url)
    name = response.json().get('name')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = get(url)
    duties = response.json()
    ready = 0
    ready_tasks = []
    for duty in duties:
        if duty.get('completed'):
            ready_tasks.append(duty)
            ready += 1

    print("Employee {} is done with duties({}/{})"
            .format(name, ready, len(duties)))
    for duty in ready_tasks:
        print("\t {}".format(duty.get('title')))
