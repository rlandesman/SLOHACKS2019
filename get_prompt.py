import random

def ask_user_input():
    print("Welcome to the CloseAway platform \n Let's get started! \n")
    name1 = raw_input("What is your first name?")
    email1 = raw_input("Cool, and your email?")
    name2 = raw_input("Sababa, what is the name of your CloseAway friend?")
    email2 = raw_input("And his/her email?")

def get_prompt(filename):
    with open(filename) as my_file:
        prompt_array = my_file.readlines()
    return prompt_array

def pick_prompt(prompt_array):
    prompt_length = len(prompt_array)
    idx = random.randint(0, prompt_length-1)
    return prompt_array[idx]

def main():
    prompts = get_prompt('daily.txt')
    prompt = pick_prompt(prompts)
    print(prompt)

main()
