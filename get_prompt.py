import random

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