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

def main():
    fh = open("conf.json")
    conf = json.load(fh)
    GCP_PROJ_ID = conf["gcp"]["project_id"]
    PUB_SUB_TOPIC = conf["gcp"]["pubsub_topic"]
    fh.close()

    parser = get_parser()
    args = parser.parse_args()
    msg = args.message
    attr_list = args.attributes
    attrs = {}
    if attr_list:
        for i in attr_list:
            key, val = i.split("=")
            attrs[key.strip()] = val.strip()

    batch_settings = pubsub_v1.types.BatchSettings(
        max_bytes=0,  # kilobytes
        max_latency=0,  # seconds
    )
    publisher = pubsub_v1.PublisherClient(batch_settings)
    topic_path = publisher.topic_path(GCP_PROJ_ID, PUB_SUB_TOPIC)

    # Data must be a bytestring
    msg = msg.encode('utf-8')
    res = publisher.publish(topic_path, msg, **attrs)
    # res is a google.cloud.pubsub_v1.publisher.futures.Future instance

    print("Published message ID {} to topic {}.".format(res.result(), PUB_SUB_TOPIC))

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
