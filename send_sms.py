from twilio.rest import Client
from quotes import get_quote
import requests

message = get_quote()

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC4061e8f2577e9ccdf3bd0bee5158b191'
auth_token = 'd078e586a4e7e12cc50321d73b3632d0'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=message,
                     from_='+18315402050',
                     to='+14087592181'
                 )

print(message.sid)
