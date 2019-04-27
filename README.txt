2019-04-25

Follow tutorial at 
https://cloud.google.com/functions/docs/tutorials/storage#functions-update-install-gcloud-python
in order to learn cloud functions. 

# Download github repo mentioned in tuturial:
git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git

#Change to the directory that contains the Cloud Functions sample code:
  cd python-docs-samples/functions/gcs/

# List default GCP project
gcloud config list --format='text(core.project)'

# See what events can trigger a GCP Function
gcloud functions event-types list

# Set default project:
gcloud config set project cloudfunctions

# Deploy GCP Function
gcloud functions deploy hello_gcs_generic --runtime python37 --trigger-resource cloudfunctionstesta --trigger-event google.storage.object.finalize --project cloudfunctions-238722

# Or can make an http triggered GCP function (https://cloud.google.com/functions/docs/calling/http):
gcloud functions deploy http_trigger_hello_gcs_generic --runtime python37 --trigger-http --project cloudfunctions-238722
# output will contain the HTTP URI for triggering via POST, GET, PUT, DELETE, and OPTIONS.
# i.e. curl https://us-central1-cloudfunctions-238722.cloudfunctions.net/http_trigger_hello_gcs_generic  -H "Content-Type:application/json" --data '{"name":"Keyboard Cat", "run": "first"}'

# Or can make a Pub/Sub triggered function:
# First create a Pub/Sub topic, say foreign-languages. Then deploy function:
gcloud functions deploy hello_pubsub --runtime python37 --trigger-topic foreign-languages
# Publish a message on CLI (Or Python API https://cloud.google.com/pubsub/docs/publisher#publish):
DN527ud3:helloworld nathankw$ gcloud pubsub topics publish foreign-languages --message Nathaniel
messageIds:
- '530523645918731'

Download BaseSpace NovaSeq run. First need to authenticate with BaseSpace

  bs auth

Download 

  bs download run -i 156608452 -o NovaSeq_TruSeq-stranded-mRNA_156608452

This is a 38 GB run. 

