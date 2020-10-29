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
    # store thing in cache 
    pass