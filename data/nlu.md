## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there
- hi hi
- hello there
- heeey
- hi bot
- what's up
- how is it going?
- how are you?

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:search_teacher_office
- where is [Donna](name)'s room?
- where is [Janis](name) room?
- where is [James](name)' office?
- where is [Donna Graves](name)'s office?
- where is [Hanna](name) office?
- where is [C++](course) teacher's room?
- where is [web development](course) teacher room?
- where is [database](course) teacher's office?
- where is [business](course) professor's office?
- where is [php](course) prof's office?
- where is [php programming](course) prof office?
- where is [COMP20](course_code) teacher's room?
- where is [COMP220](course_code) teacher room?
- where is [COMP206](course_code) teacher's office?
- where is [GENE](course_code) professor's office?
- where is [GENE60](course_code) prof's office?
- where is [ADMN](course_code) prof office?
- where is [web development](course) office?
- where is [database](course) office?
- where is [business](course) office?
- where is [php](course) office?
- where is [php programming](course) office?
- where is [COMP206](course_code) office?
- where is [GENE](course_code) office?
- where is [GENE60](course_code) office?
- where is [ADMN](course_code) office?
- where is my teacher's room?
- where is my professor's office?
- find me [Donna](name)'s office
- looking for teacher's room
- Can I have [Donna](name)'s room number?
- Can I have [Donna](name)'s office number?
- I need to find [Donna](name)'s room
- I need to find [Donna](name)'s office
- I'd like to know where [Donna](name)'s room is
- I want to know where [Donna](name)'s room is
- I want to know where [Donna](name)'s office is
- want to know where [Donna](name)'s room is
- want to know where [Donna](name)'s office is
- wanna know where [Donna](name)'s room is
- wanna know where [Donna](name)'s office is
- wanna know [Janis](name) office
- wanna know [database](course) office
- wanna know [COMP20](course_code) office
- wanna know office
- want to know office
- I want to know office
- I'd like to know office
- office?
- find me office
- find me [Janis](name) office
- find me [database](course) office
- find me [COMP20](course_code) office

## intent:search_teacher_office_hour
- I want to know [Donna](name)'s office hour
- Could you let me know [James](name)'s office hour?
- when is [Hanna](name)'s office hours?
- when is [Janis](name) office hours?
- when is [web development](course) teacher's office hour?
- when is [database](course) teacher's office hours?
- when is [business](course) professor's hours?
- when is [php](course) prof's office hour?
- when is [php programming](course) prof hours?
- when is [COMP20](course_code) teacher's office hours?
- when is [COMP220](course_code) teacher office hour?
- when is [COMP206](course_code) teacher's office hours?
- when is [GENE60](course_code) prof's office hours?
- when is [ADMN](course_code) prof office hour?
- When is [C++](course) teacher available hours?
- When is [C++](course) professor available?
- When is [Donna](name) available?
- find me office hours
- find me [Janis](name) office hour
- find me [database](course) office hours
- find me [COMP20](course_code) office hour
- let me know office hours
- wanna know office hour
- wanna know [Janis](name) office hours
- wanna know [database](course) office hour
- wanna know [COMP20](course_code) office hours
- want to know office hours
- I want to know office hour
- I'd like to know office hours
- office hours?
- office hour?
- hour?
- When can I meet [Donna](name)?
- When can I meet [database](course) teacher?
- When can I meet [database](course) professor?

## intent:inform
- Her name is [Donna](name)
- The name is [Janis](name)
- His name is [Bryan](name)
- name is [James](name)
- [Donna Graves](name)
- [Donna Graves](name)?
- It is [Donna Graves](name)
- The course is [C++](course)
- course is [database](course)
- It is [web dev](course)
- It's [web development](course)
- [business](course)
- [business](course)?
- It's [COMP220](course_code)
- The course is [GENE60](course_code)
- course is [COMP20](course_code)
- Program is [ADMN1000](course_code)

## lookup:name
-Donna
-donna
-Donna Graves
-donna graves
-Bryan
-Bryan Elliott
-bryan
-bryan elliott
-Janis
-Janis Michael
-janis
-janis michael
-James
-James Bond
-james
-james bond

## lookup:course
-Introduction to Canadian business
-canadian business
-canada business
-business
-database management and design
-database management & design
-database management
-database
-enterprise web development
-web development
-web dev
-php programming
-php
-object oriented programming using c++
-OOP c++
-c++
-cpp
-Topics in the contemporary workplace
-contemporary workplace
-workplace

## lookup:course_code
-ADMN1000
-COMP20
-COMP206
-COMP220
-COMP333
-GENE60

## regex:course_code
- \b[A-Za-z]{1,4}[0-9]{2,4}\b

## regex:search_teacher_office_hour
- \boffice hours?\b
- \bhours?\b