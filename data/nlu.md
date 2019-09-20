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
- where is [James](name)'s office?
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
- where is [COMP20](course_code) room?
- where is [COMP220](course_code) room?
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

## intent:search_teacher_office_hour
- I want to know [Donna](name)'s office hour
- Could you let me know [James](name)'s office hour
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
- when is [GENE](course_code) professor's office hour?
- when is [GENE60](course_code) prof's office hours?
- when is [ADMN](course_code) prof office hour?
- when is [ADMN1000](course_code) prof office hour?
- When is [C++](course) teacher available hours?
- When is [C++](course) professor available?
- When is [Donna](name) available?
- find me office hours
- let me know office hours
- office hours?
- When can I meet [Donna](name)?
- When can I meet [database](course) teacher?
- When can I meet [database](course) professor?

## lookup:name
-Donna
-Donna graves
-Bryan
-Bryan Elliott
-Janis
-Janis Michael
-James
-James Bond

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