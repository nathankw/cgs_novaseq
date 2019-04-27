import time
import json

from google.cloud import firestore

#conf = json.load(open("conf.json"))
COLLECTION = "sequencing_runs"
BUCKET_NAME = "prod_seqruns"


# Project ID is determined by the GCLOUD_PROJECT environment variable
db = firestore.Client()
run_name = "RUN_" + str(int(time.time() * 100))
coll = db.collection(COLLECTION)
doc_ref = coll.document(run_name)
# Could also reform above as db.document("/".join(COLLECTION, run_name))
doc_ref.set({
    "bucket": BUCKET_NAME,
    "path": run_name
})

# Debug: Print out all documents in bucket
docs = coll.stream()
for doc in docs:
    print("{} => {}".format(doc.id, doc.to_dict()))
