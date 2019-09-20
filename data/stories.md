## greet
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## office
* search_teacher_office
  - utter_ask_teacher_name_or_course
  * inform{"name":"example"}
  - slot{"name":"example"}
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office
  - utter_ask_teacher_name_or_course
  * inform{"course":"example"}
  - slot{"course":"example"}
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office
  - utter_ask_teacher_name_or_course
  * inform{"course_code":"example"}
  - slot{"course_code":"example"}
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}

* search_teacher_office{"name": "example"}
  - utter_teacher_office
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office{"course": "example"}
  - utter_teacher_office
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office{"course_code": "example"}
  - utter_teacher_office
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}

## office hours
* search_teacher_office_hour
  - utter_ask_teacher_name_or_course
  * inform{"name":"example"}
  - slot{"name":"example"}
  - action_search_office_hour
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office_hour
  - utter_ask_teacher_name_or_course
  * inform{"name":"example"}
  - slot{"name":"example"}
  - action_search_office_hour
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office_hour
  - utter_ask_teacher_name_or_course
  * inform{"name":"example"}
  - slot{"name":"example"}
  - action_search_office_hour
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office_hour{"name":"example"}
  - utter_teacher_office_hour
  - action_search_office_hour
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office_hour{"course": "example"}
  - utter_teacher_office_hour
  - action_search_office_hour
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office_hour{"course_code": "example"}
  - utter_teacher_office_hour
  - action_search_office_hour
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}