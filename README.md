## To-do-List

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/68cbd7b480c047fcb377576670c551bd)](https://www.codacy.com/gh/srisathyamamidala/To-do-List/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=srisathyamamidala/To-do-List&amp;utm_campaign=Badge_Grade)

### Project Description

To-do-List application is to display the to do list of the user which changes from day to day. Here the user initially create an account by registering and login into the account. The welcome page is displayed now to the user. There will be a button of adding the to do's. So the user clicks it and add the to do's for that particular day. The user will be able to update the list. This list will be stored and displayed to the user whenever the user login into the account. When the user completes the task for that day user can just click the check box of that particular task so that task will be eliminated from that list and the remaining tasks will be displayed. The user also gets the number of remaining tasks for that day and that number changes when the user do the task and clicks the check box. After completing all the tasks then the user gets a message. 

---

### Team members 

1. [Sri Sathya Mamidala](https://github.com/srisathyamamidala)-Backend Developer  -  S542298@nwmissouri.edu
2. [Prasanna Arla](https://github.com/prasannaarla)-Frontend Developer  -  S542294@nwmissouri.edu

### Requirements

In order to build the app the we need the following:

1. [Python](https://www.python.org/downloads/)
2. [Visual studio code](https://visualstudio.microsoft.com/)
3. [SQLite](https://www.sqlite.org/index.html)


---

### Setup

After cloning the repo the developer needs to install the requirements which are mentioned in the requirements section. Then the developer can just open up the file and then the developer need to setup the database which is they need to login into the database for the web app to run locally.

#### To run the application locally: 

After opening the app in the IDE :

Initially we need to create the virtual environment and activate it by using the following command:

```

PS C:\Users\S542298\Documents\GitHub\To-do-List> .\venv\bin\activate

```

After creation of the virtual environment install the requirements.txt file by using the following command

```
pip install -r requirements.txt
```

Then we need to run the following commands 

```
python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```

Then we get the application running locally.
Next we need to push the application to the github repo either by using the github desktop or by using the git add push and commit commands.

---



### Deployment

The app needs to be deployed using the heroku. Initially the new app is created in the heroku by giving the name then the github of that project should be connected and the main branch should be deployed and run the app locally. Whenever you make any change in the repo and if their is no progress in heroku do  manual deployment.

After pushing the application to repo and connecting the github to the heroku we need to deploy it.

The below is the link after deploying the application to the repo:

[To-do-list application](https://todolistmamidala.herokuapp.com/)


---

### Links: 

* [Link to proposal](https://github.com/srisathyamamidala/GDP2-proposal)
* [Link to the swagger repo](https://github.com/srisathyamamidala/swagger-to-do-list)
* [Link to wiki](https://github.com/srisathyamamidala/To-do-List/wiki)
* [Link to issues](https://github.com/srisathyamamidala/To-do-List/issues)
* [Link to milestones](https://github.com/srisathyamamidala/To-do-List/milestones)
* [Link to google analytics](https://analytics.google.com/analytics/web/provision/#/provision)

### Documentation
* [swagger](https://srisathyamamidala.github.io/swagger-to-do-list/)

### Security analyses:

* [Codacy](https://app.codacy.com/gh/srisathyamamidala/To-do-List/dashboard)

### Coverage report:

<img src="coveragereport.png" alt="coverage report" style="width:700px;"/>

### Unit test report:

We have written two test cases but we didn't get the report generated and hence we are uploaded the screenshot of vscode

### [Link to the unit test code](https://github.com/srisathyamamidala/To-do-List/blob/main/todos/tests.py)

<img src="Unittest.png" alt="unit test report" style="width:700px;"/>

### Snyk integration report:

<img src="synkreport.png" alt="snyk report" style="width:700px;"/>

### Documentation 
We have tried the documentation using the admin docs and the sphinx but we are not able to do it. We have created the super user but the local host is not getting opened
<img src="documentation.png" alt="documentation report" style="width:700px;"/>












