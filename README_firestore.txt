2019-04-26
Nathaniel Watson

Create a Firestore database in us-west2 (Los Angeles). There isn't a us-central option.
I created a service account with a role of Cloud Firestore Editor, but when I ran my script to add
data to Firestore, I got an insufficient permissions error. The only way I could get around this was
by using a service account with the project role. 

