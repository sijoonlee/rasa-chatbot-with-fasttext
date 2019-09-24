question_with_course = [
'- where is [{}](COURSE_CODE)\'s office?',
'- where is [{}](COURSE_CODE) office?',
'- find me [{}](COURSE_CODE)\'s office',
'- Can I have [{}](COURSE_CODE)\'s office number?',
'- I need to find [{}](COURSE_CODE)\'s office',
'- I want to know where [{}](COURSE_CODE) office is',
'- want to know where [{}](COURSE_CODE)\'s office is',
'- wanna know where [{}](COURSE_CODE)\'s office is',
'- wanna know [{}](COURSE_CODE) office',
'- [{}](COURSE_CODE)\'s office?',
'- [{}](COURSE_CODE) office?',
'- find me [{}](COURSE_CODE) office',
'- find me [{}](COURSE_CODE)\'s office',
'- Could you let me know [{}](COURSE_CODE)\'s office?',
'- Do you know [{}](COURSE_CODE) office number?',
'- Do you know [{}](COURSE_CODE)\'s office?'
]

courses = [
'ADMN1000',
'COMP20',
'COMP206',
'COMP220',
'COMP333',
'GENE60',
]

# split_names = [y for x in full_names for y in x.split() ]

def lowercase_array(arr):
    lowercase_arr = [x.lower() for x in arr]
    return lowercase_arr

lowercase_courses = lowercase_array(courses)

course_data_set = lowercase_courses + courses

print(course_data_set)

import random

sampling_rate = 0.3
no_sample = int(sampling_rate * len(question_with_course))


train_set = []
for course in course_data_set:
    sample_questions = random.choices(question_with_course, k=no_sample)
    for question in sample_questions:
        train_set.append(question.format(course))

print(train_set)


# header = ["## intent:search_teacher_office"]
save_file = open(r"course_code_nlu.md", "w")

# for line in header:
#     save_file.write(line + '\n')
for line in train_set:
    save_file.write(line + '\n' )


