#!/usr/bin/env python3

import argparse
import json

from google.cloud import pubsub_v1

###
# Nathaniel Watson
# nathanielwatson@stanfordhealthcare.org
# 2019-04-26
###

def get_parser():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-m", "--message", required=True, help="The message to publish")
    parser.add_argument("-a", "--attributes", nargs="+", help="One or more key=value attributes to pass along with the message.")
    return parser

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

if __name__ == "__main__":
    main()
