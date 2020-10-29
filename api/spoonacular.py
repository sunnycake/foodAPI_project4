import requests
import os
from pprint import pprint
import json
from . import spoonacular_cache


key = os.environ.get('SPOONACULAR_KEY')



def params_unique_combination(baseurl, params, private_key=key):
    alphabetized_keys = sorted(params.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_key:
            res.append("{}-{}".format(k, params[k]))
    return baseurl + "_".join(res)


def get_recipe(search_recipe):
    try:
        url = 'https://api.spoonacular.com/recipes/complexSearch'
        params = {'query': search_recipe, 'addRecipeInformation': 'true','number': '1', 'apiKey': key}
        unique_ident = params_unique_combination(url, params)

        from_cache = spoonacular_cache.fetch_from_cache(unique_ident)
        if from_cache:
        #     print('From cache')
            return from_cache
        # if unique_ident in CACHE_DICTION:
        #     pprint(CACHE_DICTION[unique_ident])
        #     # return CACHE_DICTION[unique_ident]
        else:
            print('From api')
            resp = requests.get(url, params)
            spoonacular_cache.add_to_cache(resp)
            # CACHE_DICTION[unique_ident] = json.loads(resp.text)
            # dumped_json_cache = json.dumps(CACHE_DICTION, indent=2)
            # fw = open(CACHE_FNAME,"w")
            # fw.write(dumped_json_cache)
            # fw.close() 
            # pprint(CACHE_DICTION[unique_ident])
            # return CACHE_DICTION[unique_ident]
    except Exception as e:
        print('Error with your query. ', e)

get_recipe('steak')
