#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This script is used to automatically download the FASTA by specifying the search key word"""

__author__ = 'Lingjie Meng'

import os
import sys
import time
from Bio import Entrez
from urllib.error import HTTPError, URLError
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description="Download sequences from NCBI")
parser.add_argument("-s", "--search_term", help="Search term for NCBI database", required=True)
args = parser.parse_args()

# Set the email here
Entrez.email = "qdmlj1219@gmail.com"


def get_search(term, extra=''):
    """
    Perform an NCBI database search for proteins matching the specified search term,
    excluding entries with certain keywords in their titles, and using the history feature.
    """
    try:
        handle = Entrez.esearch(db="protein", term=f'({term}[Title]) NOT hypothetical[Title] '
                                                    'NOT putative[Title] AND 50:1000000[SLEN] NOT putitive[Title] '
                                                    'NOT probable[Title] NOT possible[Title] NOT unknown[Title] ' + extra,
                                idtype="acc", usehistory="y")
        search_results = Entrez.read(handle)
        handle.close()
        return search_results
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def download_batch(fetch_handle, file_handle):
    """
    Attempt to download a batch of sequences and write them to a file.
    """
    try:
        data = fetch_handle.read()
        fetch_handle.close()
        file_handle.write(data)
        return True
    except HTTPError as err:
        if 500 <= err.code <= 599:
            print(f"Received error from server {err}")
            time.sleep(15)
    return False

def get_sequences(search_results, out="out.fasta", batch_size = 100, start_batch=0):
    """
    Download sequences based on search results, in batches, and write them to a specified output file.
    """
    webenv = search_results["WebEnv"]
    query_key = search_results["QueryKey"]
    count = int(search_results["Count"])
    
    with open(out, "w") as out_handle:
        for start in range(start_batch * batch_size, count, batch_size):
            end = min(count, start + batch_size)
            print(f"Going to download record {start + 1} to {end} of {count}")
            
            for attempt in range(3):
                try:
                    fetch_handle = Entrez.efetch(db="protein", rettype="fasta", retmode="text",
                                                 retstart=start, retmax=batch_size, webenv=webenv,
                                                 query_key=query_key, idtype="acc")
                    if download_batch(fetch_handle, out_handle):
                        break
                except URLError as e:
                    print(f"URL error ({e.reason}) on attempt {attempt + 1} of 3; retrying...")
                    time.sleep(15)
                except Exception as e:
                    print(f"Failed to download batch {start + 1} to {end}: {e}")
                    break

    print("Download completed.")


search_term = args.search_term
search_results = get_search(search_term)
get_sequences(search_results, out=f'{search_term}.fasta', start_batch=0)