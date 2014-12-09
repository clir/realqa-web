## RealQA Web Interface

The RealQA web application is an implementation of the Android app RealQA.

Installation:
  1. Download python
  2. Download virtualenv
  3. Create a directory where you will store your virtual environment files. I called mine Virtualenvs
  4. cd Virtualenvs
  5. virtualenv env
  6. source ./env/bin/activate
  7. pip install django
  8. which django-admin.py
  9. pip install requests
  10. cd to a folder where you hold your code base
  11. git clone https://github.com/clir/realqa-web.git
  12. cd realqa-web/src/main/java/edu/emory/clir/realqa/web/realqawebapp
  13. python manage.py runserver --> this is for development, will point to localhost:8000/realqa
  
API documentation to RealQA server

------------- API calls used in “My questions” tab ----------------


Description: Get asked questions (by user)
HTTP Method: GET
Resource: /asked_questions/ 
Data: {}
Result: Question list
Detail: This list is paginated by 10 per page

Description: Get subscribed questions (by user)
HTTP Method: GET
Resource: /subscribed_questions/
Data: {}
Result: Question list
Detail: This list is paginated by 10 per page

Description: Get answered questions (by user)
HTTP Method: GET
Resource: /answered_questions/
Data: {}
Result: Question list
Detail: This list is paginated by 10 per page


-------------------------------------------------------------------------------
-------  API calls used in “Recommended questions” tab -----


Description: Get recommended question by freshness (for user)
HTTP Method: GET
Resource: /recommended_questions_by_freshness/
Data: {}
Result: List of recommended questions
Detail: This list is paginated by 10 per page


Description: Get recommended question by relevance (for user)
HTTP Method: GET
Resource: /recommended_questions_by_relevance/
Data: {}
Result: List of recommended questions
Detail: This list is paginated by 10 per page
Description: Get recommended question by answer count (for user
)HTTP Method: GET
Resource: /recommended_questions_by_answer_count/
Data: {}
Result: List of recommended questions
Detail: This list is paginated by 10 per page

Description: Get recommended question by location (for user)
HTTP Method: GET
Resource: /recommended_questions_by_location/
Data: {}
Result: List of recommended questions
Detail: This list is paginated by 10 per page

Description: Get recommended question by popularity (for user)
HTTP Method: GET
Resource: 
Data: {}
Result: List of recommended questions
Detail: This list is paginated by 10 per page


-------------------------------------------------------------------------------
-------------  API calls used in “Ask question” tab ----------------


Description: Retrieve locations
HTTP Method: GET
Resource: /locations/
Data: {}
Result: List of locations
Detail: 

Description: Recommended tags for specific question body
HTTP Method: POST
Resource: /recommended_tags/
Data: {question_body: “body of the question”}
Result: List of recommended tags
Detail: This list is not paginated



Description: Send question
HTTP Method: POST
Resource: /questions/
Data: {body: “body of the question”, tagnames: “<list of tags separated by spaces>”, time_spent_editing: “<number of seconds that user has spent while writing her question>”, latitude: “<latitude value>”, longitude: “<longitude value>”, location_name: “<location_name>”
Result: {}
Detail: location_name is one of the names that have been retrieved during GET /locations/. If user has not chosen any of them, “asker’s location” is sent as the location_name


-------------------------------------------------------------------------------
----------  API calls used Question List (any of them) -----------


Description: Retrieve question detail
HTTP Method: GET
Resource: /questions/<id>/
Data: {}
Result: Question detail
Detail: 

Description: Retrieve question answers
HTTP Method: GET
Resource: /questions/<id>/answers/
Data: {}
Result: List of answers for question id with <id>
Detail: 

Description: Retrieve questions by tag (after clicking on tag body)
HTTP Method: GET
Resource: /questions/?tag_name=<tagname>/
Data: {}
Result: List of recommended questions
Detail: This list is paginated by 10 per page




-------------------------------------------------------------------------------
-----------------  API calls used Question Thread -----------------


Description: Vote on question
HTTP Method: POST
Resource: /nodes/<node_id>/vote?vote_type=<up|down>
Data: {}
Result: Contains value of current score
Detail: 

Description: Report action (question or answer)
HTTP Method: POST
Resource: /nodes/<node_id>/flag/
Data: {reason: “reason for flagging”}
Result: {}
Detail: 

Description: Remove question/answer
HTTP Method: DELETE
Resource: /questions/<id>/
Data: {}
Result: {}
Detail: 

Description: Send answer
HTTP Method: POST
Resource: /questions/<id>/answers/
Data: {body: “body of the answer”, time_spent_editing: “number of seconds that user has spent while writing her answer”}
Result: {}
Detail: 



------------------------------------------------------------------------------
------------------  API calls used to login/register ------------------


Description: Log in
HTTP Method: POST
Resource: /api-token-auth/
Data: {username: “username”, password: “password”}
Result: token for the user
Detail: 

Description: Retrieve user’s data
HTTP Method: GET
Resource: /users/0/
Data: {}
Result: detail of the user
Detail: 

Description: Register user
HTTP Method: POST
Resource: /users/
Data: {username: “username”, password: “password”, device_id: “device_id”}
Result: result of the api call
Detail: 

Description: Retrieve popular tags
HTTP Method: GET
Resource: /tags/?min_used_count=<count>
Data: {}
Result: List of popular tags
Detail: <count> is minimum tags count

Description: Update user tags
HTTP Method: POST
Resource: /update_profile/
Data: {tagnames: “<list of tags separated by spaces>”}
Result: result of the api call
Detail: 
