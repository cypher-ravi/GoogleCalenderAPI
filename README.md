# GoogleCalenderAPI 
#Points to remember before running application

1. Generate credentials from google console for webapp (client id, client secret) -> credential json file
2. Put credential.json into coreapi folder
3. It is working on external usage from the perspective of google and it is in test mode so to 
get events, developer need to add test user email to the list from google console
4. Use http://localhost:8000/core/v1/calendar/init - first
5. -----> it will redirect you to sign page (if your email is in test users - as mentioned in 3 point)
6. -----> then on http://localhost:8000/core/v1/calendar/redirect endpoint you'll get list of events 
