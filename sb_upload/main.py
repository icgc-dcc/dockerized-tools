#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sevenbridges as sbg
import os
import argparse
import sys

if 'SB_API_ENDPOINT' not in os.environ:
    os.environ['SB_API_ENDPOINT'] = 'https://cgc-api.sbgenomics.com/v2'
if 'SB_AUTH_TOKEN' not in os.environ:
    sys.exit('Need to set environment variable SB_AUTH_TOKEN with authorization token')

api = sbg.Api()

def main():
    parser = argparse.ArgumentParser(description='Download file from CGC')
    parser.add_argument('--file','-f', dest='f', type=str, help='File to upload', required=True)
    parser.add_argument('--project','-p', dest='project', type=str, help='CGC project directory', required=True)

    args = parser.parse_args()
    api = sbg.Api()

    api.files.upload(args.f, args.project)

if __name__ == "__main__":
    main()