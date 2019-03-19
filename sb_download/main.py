#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sevenbridges as sbg
import os
import argparse

os.environ['SB_API_ENDPOINT'] = 'https://cgc-api.sbgenomics.com/v2'
#os.environ['SB_AUTH_TOKEN'] = ''

api = sbg.Api()

def main():
    parser = argparse.ArgumentParser(description='Download file from CGC')
    parser.add_argument('--id', dest='id', type=str, help='ID of the file to download', required=True)
    parser.add_argument('--output-dir', dest='output_dir', type=str, help='Output directory', required=True)

    args = parser.parse_args()
    api = sbg.Api()

    file = api.files.get(args.id)
    file.download(os.path.join(args.output_dir,file.name))
    return 0

if __name__ == "__main__":
    main()