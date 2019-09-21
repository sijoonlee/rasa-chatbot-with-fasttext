# Student Assistant Chatbot Project  
- Chatbot Framework: [Rasa](https://rasa.com) Framework
- Word Vector: Facebook's [Fast Text](https://fasttext.cc/docs/en/english-vectors.html)
- The Chatbot recognizes questions about teacher's **office number**, **office hours** 
- And answers the inquries by retrieving the information from MongoDB

### FastText Word Vector: Download word vector and initialize model for Spacy  
- Download [wiki-news-300d-1M-subword.vec.zip](https://fasttext.cc/docs/en/english-vectors.html) to "fasttext" folder  
- Execute the command below  
```
python -m spacy init-model en ./wiki-news-300d-1M-subword --vectors-loc wiki-news-300d-1M-subword.vec.zip
```

### Intent  
User's intents that the chatbot is trained to recognize  
- greet : For example, "Hello"
- goodbye : For example, "Good bye"
- search_teacher_office : For example, "Where is Donna's office?"
- search_teacher_office_hour : For example, "When is Donna's office hour?"
- inform : For example, "Donna". This is to answer the chatbot when it gives questions to users.

### Three Entities
Words or phrases that the chatbot is trained to recognize  
- Name : For example, "Donna Graves". First name, last name and full name are acceptable for user inputs.  
- Course Name : For example, "Object Oriented Programming with C++". The part of the name is acceptable as user inputs.  
- Course Code : For example, "COMP333". Only fully typed one is acceptable.  

### Stories  
Two main streams to deal with user's questions  
- One for the questions about **Office Number**    
- One for the questions about **Office Hours**    


## MongoDB Schema
Database for Teachers' information  
- name: full name  
- course: the full name of the course  
- course_code: code of the course  
- office_hour: office hour information, sub-document  

- Example  
```
{
    "_id" : ObjectId("5d79462b766bc02060d6575f"),
    "name" : "donna graves",
    "room" : "111",
    "course" : "object oriented programming using c++",
    "course_code" : "comp333",
    "office_hour" : {
        "mon" : "14:00~20:00",
        "tue" : "10:00~12:00"
    },
    "createdAt" : ISODate("2019-09-11T19:08:27.649Z"),
    "updatedAt" : ISODate("2019-09-11T19:08:27.649Z"),
    "__v" : 0
}
```


