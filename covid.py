import sys
import requests
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(usage='covid.py [options]')
parser.add_argument('--active', default=False, action='store_true', help='Include active cases')
parser.add_argument('--deaths', default=False, action='store_true', help='Include number of deaths')
parser.add_argument('--recovered', default=False, action='store_true', help='Include recovered cases')
args = parser.parse_args()


api_url = 'https://corona.lmao.ninja/v2/all?yesterday'

res = requests.get(api_url)
tonow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if res.status_code == 200:
    data = res.json()
    total_cases = data.get('cases')
    print(f'[{tonow}] {res.status_code} CASES - {total_cases} ', end='')

    # print values of specified options
    for dim in {'active', 'deaths', 'recovered'}:
        if getattr(args, dim):
            print(f"| {dim}: {data.get(dim)} ", end='')
