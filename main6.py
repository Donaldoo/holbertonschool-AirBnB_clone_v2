#!/usr/bin/python3
import sys
import requests
from lxml import html
import re
import MySQLdb
import uuid


def add_states_with_cities(number_states=1, number_cities=0):
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()

    for i in range(number_states):
        state_id = str(uuid.uuid4())
        cur.execute("INSERT INTO `states` (id, created_at, updated_at, name) VALUES ('{}','2016-03-25 19:42:40','2016-03-25 19:42:40','state{}');".format(state_id, i))

        for j in range(number_cities):
            city_id = str(uuid.uuid4())
            cur.execute("INSERT INTO `cities` (id, state_id, created_at, updated_at, name) VALUES ('{}', '{}','2016-03-25 19:42:40','2016-03-25 19:42:40','city{}{}');".format(city_id, state_id, i, j))

    conn.commit()
    cur.close()
    conn.close()


def validate_number(numbers):
    # numbers = [2, 3, 4, 0, 2] => number of cities by states
    NO_PROXY = {
        'no': 'pass',
    }

    ## Request
    page = requests.get('http://0.0.0.0:5000/cities_by_states', proxies=NO_PROXY)
    if int(page.status_code) != 200:
        return False, "Status fail: {}".format(page.status_code)

    ## Parsing
    tree = html.fromstring(page.content)
    if tree is None:
        return False, "Can't parse page"

    li_tags_el_states = tree.xpath('//body/ul/li')
    if li_tags_el_states is None or len(li_tags_el_states) != len(numbers):
        return False, "Doesn't find {} LI States tags (found {})".format(len(numbers), len(li_tags_el_states))
        
    state_idx = 0
    for li_tags_el_state in li_tags_el_states:
        cities_li_tags = list(filter(None, [x.replace(" ", "").strip(" ").strip("\n").strip("\t") for x in li_tags_el_state.xpath('ul/li/text()')]))
        if cities_li_tags is None or len(cities_li_tags) != numbers[state_idx]:
            return False, "Doesn't find {} LI Cities tags (found {})".format(numbers[state_idx], len(cities_li_tags))
        state_idx += 1

    return True, None


# Test initial state
res, msg = validate_number([2, 2, 2])
if not res:
    print("ERROR: {}".format(msg))

# Add 1 new states
add_states_with_cities(1, 4)

# Test 6 states
res, msg = validate_number([2, 2, 2, 4])
if not res:
    print("ERROR: {}".format(msg))

print("OK", end="")
