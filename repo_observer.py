#!/usr/bin/python
# -*- coding:utf-8 -*-
'''

__author__ = 'Qijie Pan'
   9/21/2016

'''


def poll():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dispatcher-server",
                        help="dispatcher host:port, " \
                             "by default it uses localhost:8888",
                        default="localhost:8888",
                        action="store")
    parser.add_argument("repo", metavar="REPO", type=str,
                        help="path to the repository this will observe")
    args = parser.parse_args()
    dispatcher_host, dispatcher_port = args.dispatcher_server.split(":")


while True:
    try:
        # call the bash script that will update the repo and check
        #  for changes. If there's a change, it will drop a .commit_id file
        #  with the latest commit in the current working directory
        subprocess.check_output(["./update_repo.sh"], args.repo)
    except subprocess.CallProcessError as e:
        raise Exception("Could not update and check repository. " + "Reason: %s" % e.output)
