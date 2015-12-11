""" Creating a function that queries the BLS public API
and returns the jobs report data in an organized manner"""

import requests
import json
from bls_api import bls_api_url, bls_api_headers, bls_api_series_id
from bls_key import bls_key
from bls_report_classes import bls_total_jobs

month_list = ['January', 'February', 'March', 'April', 'May',
              'June', 'July', 'August', 'September', 'October',
              'November', 'December']


def bls_api_request(series_id, start_year, end_year):
    headers = bls_api_headers
    data = json.dumps({
        'seriesid': series_id,
        'startyear': start_year,
        'endyear': end_year,
        'registrationKey': bls_key
    })
    url = bls_api_url
    post = requests.post(url, data=data, headers=headers)
    return post


def bls_post_reader(post):
    response = json.loads(post.text)
    results = response["Results"]
    series = results["series"][0]
    data = series["data"]
    return data


def bls_post_parser(data):
    report = {}
    for i in range(0, len(data)):
        month = data[i]
        key_name = month['periodName'] + month['year']
        report[key_name] = int(month['value'])*1000
    return report


def total_jobs(month_numb, year):
    post = bls_api_request(bls_api_series_id, year, year)
    data = bls_post_reader(post)
    report = bls_post_parser(data)
    month = month_list[(month_numb - 1)] + str(year)
    answer = report[month]
    return answer


def last_month(month_numb, year):
    new_month = int()
    new_year = int()
    if month_numb == 1:
        new_month = 12
        new_year = year - 1
    else:
        new_month = month_numb - 1
        new_year = year
    return {'month': new_month, 'year': new_year}


def bls_reader(month_numb, year):
    previous_month = last_month(month_numb, year)
    current_month_jobs = total_jobs(month_numb, year)
    previous_month_jobs = total_jobs(previous_month['month'], previous_month['year'])
    answer = current_month_jobs - previous_month_jobs
    return answer
