# Student Assistant Chatbot Project  
- [Rasa](https://rasa.com) Framework used
- Facebook's [Fast Text](https://fasttext.cc/docs/en/english-vectors.html) word vector used
   

### Download word vector and initialize model for Spacy  
- Download [wiki-news-300d-1M-subword.vec.zip](https://fasttext.cc/docs/en/english-vectors.html) to "fasttext" folder  
- Execute the command below  
```
python -m spacy init-model en ./wiki-news-300d-1M-subword --vectors-loc wiki-news-300d-1M-subword.vec.zip
```

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

# TO-DO

### Prepare train data  

### Prepare domain  

### Prepare stories  

### Prepare custom action  



