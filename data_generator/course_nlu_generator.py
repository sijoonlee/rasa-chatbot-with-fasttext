question_with_course = [
'- where is [{}](COURSE)\'s office?',
'- where is [{}](COURSE) office?',
'- find me [{}](COURSE)\'s office',
'- Can I have [{}](COURSE)\'s office number?',
'- I need to find [{}](COURSE)\'s office',
'- I want to know where [{}](COURSE) office is',
'- want to know where [{}](COURSE)\'s office is',
'- wanna know where [{}](COURSE)\'s office is',
'- wanna know [{}](COURSE) office',
'- [{}](COURSE)\'s office?',
'- [{}](COURSE) office?',
'- find me [{}](COURSE) office',
'- find me [{}](COURSE)\'s office',
'- Could you let me know [{}](COURSE)\'s office?',
'- Do you know [{}](COURSE) office number?',
'- Do you know [{}](COURSE)\'s office?'
]

courses = [
'Introduction to Canadian Business',
'Business',
'Ddatabase Management and Design',
'Database Management',
'Database',
'Enterprise Web Development',
'Web Development',
'Web Dev',
'Php Programming',
'Php',
'Object Oriented Programming Using C++',
'C++',
'Topics in the Contemporary Workplace',
'Contemporary Workplace',
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
save_file = open(r"course_nlu.md", "w")

# for line in header:
#     save_file.write(line + '\n')
for line in train_set:
    save_file.write(line + '\n' )


