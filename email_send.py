import os
import get_prompt

def get_string():
    prompt_array = get_prompt.get_prompt('weekly.txt')
    return get_prompt(prompt_array)

def email(email1, email2):
    gmail_user = 'closest.away@gmail.com'
    gmail_password = 'choomahMaster'

    sent_from = gmail_user
    users = 2
    send_array =[0]*users

    send_array[0] = email1
    send_array[1] = email2
    SUBJECT = "Your daily CloseAway prompt"
    TEXT = get_prompt.pick_prompt()
    FROM = gmail_user
    TO = [0]*users
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(send_array), SUBJECT, TEXT)
    try:
        print("It worked!")#Email sending

    except:
        print('Something went wrong...')

def main(email1,email2):
    email(email1,email2)
