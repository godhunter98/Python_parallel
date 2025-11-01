from time import perf_counter
import requests
from test_utils import URLS


def fetch_url(url):
    response= requests.get(url)
    return f"{url} --> {response.status_code}"


if __name__=="__main__":
    a = perf_counter()
    results = [fetch_url(url) for url in URLS[:4]]
    b = perf_counter() 
    print("Results: ",results,f"\nIt took {(b-a):.2f} seconds to run!")