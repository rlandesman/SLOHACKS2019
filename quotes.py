import requests

#Returns a random quote in string var type
def get_quote():
    resp = requests.get("http://api.forismatic.com/api/1.0/?method=getQuote&format=text&lang=en")
    if resp.status_code != 200:
        print("There was an issue getting the quote, YIKES")
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    return resp.text
