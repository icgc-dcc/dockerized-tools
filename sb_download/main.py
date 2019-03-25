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
    parser.add_argument('--id', dest='id', type=str, help='ID of the file to download', required=True)
    parser.add_argument('--output-dir', dest='output_dir', type=str, help='Output directory', required=True)

    args = parser.parse_args()
    api = sbg.Api()

    f = api.files.get(args.id)
    f.download(os.path.join(args.output_dir,f.name))

if __name__ == "__main__":
    main()