import time
import sys
import giphy_client
from giphy_client.rest import ApiException

# create an instance of the API class
api_instance = giphy_client.DefaultApi()
api_key = 'nlK8AkkJbGTC0IQv4Osj1rEQr6aIZlPc'
limit = 30
offset = 0
rating = 'g'
lang = 'tw'
fmt = 'json'

def query(query_string):
    try:
        # Search Endpoint
        api_response = api_instance.gifs_search_get(api_key, query_string, limit=limit, offset=offset, rating=rating, lang=lang, fmt=fmt)
        gif_list = api_response.data
        url_list = []
        for gif in gif_list:
            url_list.append("https://i.giphy.com/media/{}/200w.gif".format(gif.id))
        return url_list
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

if __name__ == "__main__":
   query(sys.argv[1:])
