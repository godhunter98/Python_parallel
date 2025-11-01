from time import perf_counter
import requests
from test_utils import URLS
from concurrent.futures import ThreadPoolExecutor


def fetch_url(url):
    response= requests.get(url)
    return f"{url} --> {response.status_code}"


if __name__=="__main__":
    a = perf_counter()
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_url,URLS[:4]))

    b = perf_counter() 
    print("Results: ",results,f"\nIt took {(b-a):.2f} seconds to run!")