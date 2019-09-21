## search office_hour : when everything goes well
* search_teacher_office_hour{"name": "example"}
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug

* search_teacher_office_hour{"course": "example"}
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug

* search_teacher_office_hour{"course_code": "example"}
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug

## search office_hour : when everything goes well
* search_teacher_office_hour{"name": "example"}
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug
* search_teacher_office_hour{"course": "example"}
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}  
  - utter_debug  
* search_teacher_office_hour{"course_code": "example"}
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug

## search office_hour : when user didn't give an entity
* search_teacher_office_hour
  - utter_ask_teacher_name_or_course
  * inform{"name":"example"}
  - slot{"name":"example"}
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug 

* search_teacher_office_hour
  - utter_ask_teacher_name_or_course
  * inform{"course":"example"}
  - slot{"course":"example"}
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug 

* search_teacher_office_hour
  - utter_ask_teacher_name_or_course
  * inform{"course_code":"example"}
  - slot{"course_code":"example"}
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug

## search office_hour : when user didn't give an entity
* search_teacher_office_hour
  - utter_ask_teacher_name_or_course
  * inform{"name":"example"}
  - slot{"name":"example"}
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug 

* search_teacher_office_hour
  - utter_ask_teacher_name_or_course
  * inform{"course":"example"}
  - slot{"course":"example"}
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug 

* search_teacher_office_hour
  - utter_ask_teacher_name_or_course
  * inform{"course_code":"example"}
  - slot{"course_code":"example"}
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug

## search office_hour : bad story
* search_teacher_office_hour
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_ask_teacher_name_or_course
  * inform{"name":"example"}
  - slot{"name":"example"}
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug
  
* search_teacher_office_hour
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_ask_teacher_name_or_course
  * inform{"name":"example"}
  - slot{"name":"example"}
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug

* search_teacher_office_hour
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_ask_teacher_name_or_course
  * inform{"name":"example"}
  - slot{"name":"example"}
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug

## search office_hour : bad story 2
* search_teacher_office_hour
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_ask_teacher_name_or_course
  * inform{"name":"example"}
  - slot{"name":"example"}
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug

* search_teacher_office_hour
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_ask_teacher_name_or_course
  * inform{"course":"example"}
  - slot{"course":"example"}
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug

* search_teacher_office_hour
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_ask_teacher_name_or_course
  * inform{"course_code":"example"}
  - slot{"course_code":"example"}
  - action_search_office_hour
  - slot{"name":""}
  - slot{"course":""}
  - slot{"course_code":""}
  - utter_debug
