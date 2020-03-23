import spotipy
import json
from math import ceil as ceil
import sys
import spotipy.util as util



client_id = '17fdd402929e4258880070b501113ccc'
client_secret = '5d71886072c34d9ebd7e3fca09919f92'
redirect_uri = 'http://localhost:8000/index.html'
token_type = 'Bearer'
username = '1265752815'
scope = 'user-library-read'


#if len(sys.argv) > 1:
#    username = sys.argv[1]
#else:
#    print("Usage: %s username" % (sys.argv[0],))
#    sys.exit()

token = util.prompt_for_user_token(username,scope,client_id, client_secret, redirect_uri)

fest = 2

if token:
    with open('festartists.json','r') as json_data:
        #get festival data; get saved tracked        
        jsonData = json.load(json_data)
        sp = spotipy.Spotify(auth=token)

        first_result = sp.current_user_saved_tracks(limit = 50)
        total_count = first_result['total']
        masterArr = []

        for i in range(int(ceil(total_count/50.0))):

            offset = 50*i

            results = sp.current_user_saved_tracks(limit = 50, offset = offset)

            #choose the festival here
            artist_list = jsonData[fest]['artists']

            #iterate through each artist in the lineup
            for art in range(len(artist_list)):
                #iterate through each result from the Spotify dump
                for item in results['items']:
                    track = item['track']
                    #iterate through each artist of each song from the Spotify dump
                    for tot in range(len(track['artists'])):

                        if artist_list[art].lower() == track['artists'][tot]['name'].lower():

                            insert = []

                            matching = {

                                'festival' : jsonData[fest]['festival'],
                                'artist' : track['artists'][tot]['name'],
                                'song' : track['name'],
                                'track_id' : track['id']

                            }

                            if masterArr is None:

                                continue

                            else :

                                masterArr.append(matching)

                            #print(jsonData[fest]['festival'] + ' : ' + track['name'] + ' - ' + track['artists'][tot]['name'] + track['id'])
                        else :
                            continue

        with open('matching.json', 'w') as outfile:
            json.dump(masterArr, outfile, indent = 4)

        #sp_oauth.user_playlist_create(username, jsonData[fest]['festival'], public=True, description='test')

else:
    print("Can't get token for", username)



