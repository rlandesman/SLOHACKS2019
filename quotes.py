import requests

resp = requests.get("http://api.forismatic.com/api/1.0/?method=getQuote&format=text&lang=en")
if resp.status_code != 200:
    print("There was an issue getting the quote, YIKES")
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))

print(resp.text) #resp.text is the string! 
