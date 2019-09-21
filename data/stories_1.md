## greet
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## search office : when everything goes well
* search_teacher_office{"name": "example"}
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug

* search_teacher_office{"course": "example"}
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug

* search_teacher_office{"course_code": "example"}
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug

## search office : when everything goes well
* search_teacher_office{"name": "example"}
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug
* search_teacher_office{"course": "example"}
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}  
  - utter_debug  
* search_teacher_office{"course_code": "example"}
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug

## search office : when user didn't give an entity
* search_teacher_office
  - utter_ask_teacher_name_or_course
  * inform{"name":"example"}
  - slot{"name":"example"}
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug 

* search_teacher_office
  - utter_ask_teacher_name_or_course
  * inform{"course":"example"}
  - slot{"course":"example"}
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug 

* search_teacher_office
  - utter_ask_teacher_name_or_course
  * inform{"course_code":"example"}
  - slot{"course_code":"example"}
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug

## search office : when user didn't give an entity
* search_teacher_office
  - utter_ask_teacher_name_or_course
  * inform{"name":"example"}
  - slot{"name":"example"}
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug 

* search_teacher_office
  -utter_ask_teacher_name_or_course
  * inform{"course":"example"}
  - slot{"course":"example"}
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug 

* search_teacher_office
  -utter_ask_teacher_name_or_course
  * inform{"course_code":"example"}
  - slot{"course_code":"example"}
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug

## search office : bad story
* search_teacher_office
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_ask_teacher_name_or_course
  * inform{"name":"example"}
  - slot{"name":"example"}
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug
  
* search_teacher_office
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_ask_teacher_name_or_course
  * inform{"name":"example"}
  - slot{"name":"example"}
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug

* search_teacher_office
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_ask_teacher_name_or_course
  * inform{"name":"example"}
  - slot{"name":"example"}
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug

## search office : bad story 2
* search_teacher_office
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_ask_teacher_name_or_course
  * inform{"name":"example"}
  - slot{"name":"example"}
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug

* search_teacher_office
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_ask_teacher_name_or_course
  * inform{"course":"example"}
  - slot{"course":"example"}
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug

* search_teacher_office
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_ask_teacher_name_or_course
  * inform{"course_code":"example"}
  - slot{"course_code":"example"}
  - action_search_office
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug
