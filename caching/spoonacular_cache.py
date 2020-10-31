import json
import os
import requests

CACHE_FNAME = "spoonacular_cache.json"

try:
    cache_file = open(CACHE_FNAME, 'r') 
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()

except:
    CACHE_DICTION = {}


def fetch_from_cache(identifier):
    # find thing, return if there, 
    # return None if not there 
    pass


def add_to_cache(identifier):
    # Codes here are just to get you started. Please review 
    # This function here needs to add api data to cache.
    CACHE_DICTION[unique_ident] = json.loads(resp.text)
    dumped_json_cache = json.dumps(CACHE_DICTION, indent=2)
    fw = open(CACHE_FNAME,"w")
    fw.write(dumped_json_cache)
    fw.close() 
    pprint(CACHE_DICTION[unique_ident])
    return CACHE_DICTION[unique_ident]