import datetime
import json
from twitter import *
from sportmonks import *
from utils import *

with open('./config.json') as config_file:
    config = json.load(config_file)

soccer_api = f"?api_token={creds['sportmonks']['TOKEN']}"


if __name__ == '__main__':

    #while True:

    new_fixtures_endpoint = f"{config['fixtures_url']}{date_today()}{soccer_api}{config['fixture_includes']}"
    test_fixtures_endpoint = f"{config['fixtures_url']}{'2019-12-26'}{soccer_api}{config['fixture_includes']}"
    get_events_endpoint = f"{config['livescores_url']}{soccer_api}{config['livescores_includes']}"
    test_get_event_fixture = f"GET https://soccer.sportmonks.com/api/v2.0/fixtures/11879660/{soccer_api}{config['livescores_includes']}"

    print(test_get_event_fixture)

    # get new fixtures from endpoint and only return those from specific league id
    fixtures = get_new_fixtures(test_fixtures_endpoint, config['league_id'], check_date())

    # if new fixtures exists then format the returned dictionary ready to tweet
    if fixtures:
        f = format_fixtures_for_twitter(fixtures)
        post_tweet(f) # tweet today's fixtures
        kickoffs = get_kickoffs(fixtures) # get kick-off times from today's matches
        print(time_to_sleep(kickoffs.pop(0))) # calculate sleep time until 1st kickoff
    else:
        print(time_to_sleep("06:00"))


    my_json = prettify_json("./test_livescores.json")
    print(my_json)