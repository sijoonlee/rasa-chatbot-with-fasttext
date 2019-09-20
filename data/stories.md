## greet
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## office
* search_teacher_office{"name": "Donna"}
  - utter_teacher_office
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office{"name": "Donna Graves"}
  - utter_teacher_office
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office{"name": "James"}
  - utter_teacher_office
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office{"name": "James Bond"}
  - utter_teacher_office
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office{"name": "Janis"}
  - utter_teacher_office
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office{"name": "Janis Michael"}
  - utter_teacher_office
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}

* search_teacher_office{"course": "php"}
  - utter_teacher_office
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office{"course": "business"}
  - utter_teacher_office
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office{"course": "database"}
  - utter_teacher_office
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office{"course": "c++"}
  - utter_teacher_office
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office{"course": "database management"}
  - utter_teacher_office
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}

* search_teacher_office{"course_code": "COMP20"}
  - utter_teacher_office
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office{"course_code": "COMP206"}
  - utter_teacher_office
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office{"course_code": "COMP333"}
  - utter_teacher_office
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office{"course_code": "GENE60"}
  - utter_teacher_office
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office{"course_code": "GENE"}
  - utter_teacher_office
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office{"course_code": "ADMN1000"}
  - utter_teacher_office
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}
* search_teacher_office{"course_code": "ADMN"}
  - utter_teacher_office
  - action_search_office
  - slot{"name": ""}
  - slot{"course":""}
  - slot{"course_code":""}

## office hours
* search_teacher_office_hour
  - utter_teacher_office_hour