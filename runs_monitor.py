import time
import json

from google.cloud import firestore

#conf = json.load(open("conf.json"))
COLLECTION = "sequencing_runs"
BUCKET_NAME = "prod_seqruns"


# Project ID is determined by the GCLOUD_PROJECT environment variable
db = firestore.Client()
run_name = "RUN_" + str(int(time.time() * 100))
doc_ref = db.collection(COLLECTION).document(run_name)
doc_ref.set({
    "bucket": BUCKET_NAME,
    "path": run_name
})

users_ref = db.collection(COLLECTION)
docs = users_ref.stream()
for doc in docs:
    print("{} => {}".format(doc.id, doc.to_dict()))
