""" turns twitter searches into guesses"""
import twitter_authorization
from twitter_urls import *
import requests
import json
from guess_logic import guess_generator


def twitter_search(hashtag, max_id):
	token = twitter_authorization.get_access_token()
	bearer_token = 'Bearer %s' % token
	payload = {'q': hashtag, 'count': 100, 'max_id': max_id}
	headers = {'Authorization': bearer_token}
	response = requests.get(SEARCH_ENDPOINT, params = payload, headers=headers)
	response_json = json.loads(response.text)
	return response_json

def twitter_statues(response):
	#strips out metadata from twitter search
	statuses = response['statuses']
	return statuses

def single_response_parser(statuses):
	tweet = statuses['text']
	user = statuses['user']['screen_name']
	created_at = statuses['created_at']
	guess = guess_generator(tweet)
	id_str = statuses['id_str'] #twitter id string used to define the max id
	entry = {
	"tweet": tweet,
	"user": user,
	"created_at": created_at,
	"guess": guess,
	'id_str': id_str
	}
	return entry


def response_generator(entry_list, statuses):
	for i in range(0, len(statuses)):
		entry = single_response_parser(statuses[i])
		entry_list.append(entry)
	return entry_list

def response_aggregator(hashtag, initial_max_id):
	entry_list = []

	#perform the first search
	response = twitter_search(hashtag, initial_max_id)
	statuses = twitter_statues(response)
	last_search_count = len(statuses)

	# organize the results
	response_generator(entry_list, statuses)

	while True:
		new_max_id = entry_list[-1]['id_str']
		response = twitter_search(hashtag, new_max_id)
		statuses = twitter_statues(response)
		response_generator(entry_list, statuses)
		last_search_count = len(statuses)
		if last_search_count < 100:
			break
	return entry_list
 
def main():
	entry_list = response_aggregator('#nfpguesses', '')
	print '{} entries today'.format(len(entry_list))
	for entry in entry_list:
		print 'User {} says: {}. Guess = {}'.format(entry['user'], entry['tweet']
			.encode('utf-8'), entry['guess'])

if __name__ == '__main__':
	main()

	