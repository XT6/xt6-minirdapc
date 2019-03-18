#----------------------------------------------------------------------------------
# minirdapc
#
# (c) carlos@xt6.us
# 
# Changed: 2019-03-14
#----------------------------------------------------------------------------------

import click
import requests
import shelve
import datetime
import time

class rdap_client:

    # Default constructor
    def __init__(self, w_base_url, w_cache_file='var/rdap_cache.db'):
        self.base_url = w_base_url
        self.rdap_cache = shelve.open(w_cache_file)
        self.max_cache_time = 60
    # end default constructor

    # http_get
    def rdap_http_get(self, w_uri):
        r = requests.get(self.base_url + w_uri)
        return r.json()
    # end http_get

    # rdap query
    def rdap_query(self, w_type, w_query):

        if w_type not in ['ip', 'autnum', 'entity']:
            raise ValueError("Wrong query type")

        try:
            rdap_uri = "/"+w_type+"/"+w_query
            # first check if answer is available in local cache and fresh enough
            cached_r = self.rdap_cache.get(rdap_uri, { 'json': None, 'timestamp': 0, 'hits': 0})
            if cached_r['json'] == None or (cached_r['timestamp'] - time.time()) > self.max_cache_time:
                # if not, do an http query
                r = self.rdap_http_get(rdap_uri)
                # store result in cache
                cached_r = { 'json': r, 'timestamp': int(time.time()), 'hits': 0}
                self.rdap_cache[rdap_uri] = cached_r
            else: 
                # return the result available in cache
                r = cached_r['json']
                pass
        except:
            r = False
            raise

        return r
    # end rdap_query

# end class rdap_client

if __name__ == "__main__":
    main()
    

#--END-----------------------------------------------------------------------------