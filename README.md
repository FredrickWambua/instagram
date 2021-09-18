# Instagram Clone
This is a clone to the most famous photo app instagram
## Author
Fredrick Wambua

## User Stories
- Sign in to the application to start using.
- Upload my pictures to the application.
- See my profile with all my pictures.
- Follow other users and see their pictures on my timeline.
- Like a picture and leave a comment on it.

## Set up and Installation Requirements
### Prerequisites
- python 3.8
- django
- pipenv
- dotenv

### Cloning the repository
- Fork the repository
```
$ git clone https://github.com/FredrickWambua/instagram
```
- Navigate to the repository.
### Running the application
- Creating virtual environment
```
$ python3 pipenv shell
$ pip freeze > requirements.txt
$ . .env
```
- Runing application
```
$ make server 
$ make makemigrations (this creates database migrations)
$ make migrate (this performs migrations)
```
## Known bugs
This app uses a custom user for authentication and this has made it hard for a user to login in after signing up. They need to be a super user to use the app. 
The comment and like functionalities are not working as expected.
## Deployment
View the working deployed application [here](https://fredinstaclone.herokuapp.com/)
Follow [heroku documentation](https://devcenter.heroku.com/articles/git) to know more about deployin app to heroku.

## License
Copyright 2021 Fredrick Wambua

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



