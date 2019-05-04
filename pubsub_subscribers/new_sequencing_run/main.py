#!/usr/bin/env python3

import base64
import json

from google.cloud import firestore

###
# Nathaniel Watson
# nathanielwatson@stanfordhealthcare.org
# 2019-04-26
###

BUCKET_NAME = "prod_seqruns"
#: GCP Firestore collection
COLLECTION = "sequencing_runs"

def launch_demultiplexing(data, context):
    """
    Background Cloud Function to be triggered via Pub/Sub. Expects attributes to be provided by the
    publisher. The following attributes are required:

        1) run_name - `str`. The name of the sequencing run from the sequencer.

    Args:
         data: `dict`. Contains 'data' and 'attributes' keys.
         context: `google.cloud.functions.Context`. The Cloud Functions event metadata.
    """

    if 'data' in data:
        msg = base64.b64decode(data['data']).decode('utf-8')
        print(msg
    print("Context: {}".format(context))
    attrs = data["attributes"]
    run_name = attrs["run_name"]
    print("Launching demultiplexing pipeline for sequencing run '{}'.".format(run_name))

    # Project ID is determined by the GCLOUD_PROJECT environment variable
    db = firestore.Client()
    doc_ref = db.collection(COLLECTION).document(run_name)
    doc_ref.update({
        "demultiplexing_status": "Initiating request"
    })
    print("Booting node to demultiplex run {}.".format(run_name))
