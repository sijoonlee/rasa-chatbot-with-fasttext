question_without_name = [
'- find me office',
'- wanna know office',
'- want to know office',
'- I want to know office',
'- I\'d like to know office',
'- office?',
'- looking for teacher\'s room',
'- looking for teacher\'s office',
]

question_with_name = [
'- where is [{}](PERSON)\'s room?', 
'- where is [{}](PERSON)\'s office?',
'- where is [{}](PERSON) office?',
'- find me [{}](PERSON)\'s office',
'- Can I have [{}](PERSON)\'s office number?',
'- I need to find [{}](PERSON)\'s office',
'- I\'d like to know where [{}](PERSON)\'s room is',
'- I want to know where [{}](PERSON) office is',
'- want to know where [{}](PERSON)\'s room is',
'- want to know where [{}](PERSON)\'s office is',
'- wanna know where [{}](PERSON)\'s room is',
'- wanna know where [{}](PERSON)\'s office is',
'- wanna know [{}](PERSON) office',
'- [{}](PERSON)\'s office?',
'- [{}](PERSON) office?',
'- find me [{}](PERSON) office',
'- find me [{}](PERSON)\'s office',
'- Could you let me know [{}](PERSON)\'s office?',
'- Could you let me know [{}](PERSON)\'s room?',
'- Do you know [{}](PERSON) office number?',
'- Do you know [{}](PERSON)\'s office?'
]

full_names = [
    'Donna Graves',
    'Sue Haywood',
    'Bryan Elliott',
    'Janis Michael',
    'Colin Banger',
    'Catherine Bell'
]

split_names = [y for x in full_names for y in x.split() ]

def lowercase_array(arr):
    lowercase_arr = [x.lower() for x in arr]
    return lowercase_arr

lowercase_full_names = lowercase_array(full_names)
lowercase_split_names = lowercase_array(split_names)

name_data_set = full_names + lowercase_full_names + split_names + lowercase_split_names

print(name_data_set)

import random

sampling_rate = 0.3
no_sample = int(sampling_rate * len(question_with_name))


train_set = []
for name in name_data_set:
    sample_questions = random.choices(question_with_name, k=no_sample)
    for question in sample_questions:
        train_set.append(question.format(name))

print(train_set)


header = ["## intent:search_teacher_office"]
save_file = open(r"name_nlu.md", "w")

for line in header:
    save_file.write(line + '\n')
for line in train_set:
    save_file.write(line + '\n' )


