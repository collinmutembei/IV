[![Build Status](https://travis-ci.org/collinmutembei/IV.svg?branch=master)](https://travis-ci.org/collinmutembei/IV)
[![Coverage Status](https://coveralls.io/repos/andela-cmutembei/IV/badge.svg?branch=develop)](https://coveralls.io/github/andela-cmutembei/IV?branch=develop)
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/9e68169eaae44b4ea781295f597949dd/snapshot/origin:develop:HEAD/badge.svg)](https://www.quantifiedcode.com/app/project/9e68169eaae44b4ea781295f597949dd)

## [PHEDIT](https://phedit.herokuapp.com)

> A picture is worth a thousand words - [English idiom](https://en.wikipedia.org/wiki/A_picture_is_worth_a_thousand_words)

Phedit is a modern photo editing application that lets you express yourself through pictures. Users can upload images to Phedit and apply any of the close to a dozen effects. The edited images can be shared to facebook or twitter through a public url. To view what other people have shared as well as share your edits on twitter use the hashtag [#phedited](https://twitter.com/search?f=tweets&q=%23phedited%20since%3A2016-02-23%20include%3Aretweets&src=typd)

#### Depedencies
Phedit is built using the following technologies:
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](http://www.django-rest-framework.org/)
- [Pillow](http://pillow.readthedocs.org/en/3.1.x/)
- [Postgresql](http://www.postgresql.org/)
- [AngularJS](https://angularjs.org/)

#### Installation
To setup Phedit locally follow the following instructions:

1 . Clone the repo and navigate to the project directory
```shell
$ git clone https://github.com/collinmutembei/IV.git && cd IV
```


2 . Install the project dependencies
```shell
$ pip3 install -r requirements.txt
```

3 . Create a database called `phedit` and configure the following environment variables
```shell
export SECRET=classified
export DATABASE_URL=postgres://<db-username>:@127.0.0.1:5432/phedit
```


4 . Run the projects migrations and initialize the projects data
```shell
$ python3 manage.py migrate
$ python3 manage.py loaddata init-data.json
```  


5 . Start the server for the project
```shell
$ python3 manage.py runserver
```

6 . Open http://127.0.0.1:8000 on your favorite web browser

#### Running tests

To run the projects' tests
```shell
$ python3 manage.py test
```

#### License
Copyright &copy; 2016 - Collin Mutembei

This project is licensed under the terms of the [MIT license.](https://github.com/andela-cmutembei/IV/blob/master/LICENSE)
