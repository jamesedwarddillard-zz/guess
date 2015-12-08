""" Identifies the current BLS report Month and Year based on the 
current date and time"""

import datetime
from bls_reader.bls_reader import bls_api_request, bls_post_reader
from bls_reader.bls_api import bls_api_series_id



def current_report():
	#identify the current year
	year = datetime.datetime.now().year

	#determine the number of reports so far this year by calling the bls api
	response = bls_api_request(bls_api_series_id, year, year)
	data = bls_post_reader(response)
	mos = len(data)
	
	return (mos, year)


