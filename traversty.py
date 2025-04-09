#!/usr/bin/env python3

import requests
import argparse
import sys
import os
import time

def banner():
    anarchy_A = r"""
        /\
       /  \
      / /\ \
     / /__\ \
    /_/    \_\
      / /\ \
     / /__\ \
    /_/    \_\
    """

    print("\033[91m" + anarchy_A + "\033[0m")  # Red color
    print("\033[92m" + r"""
████████╗██████╗  █████╗ ██╗   ██╗███████╗███████╗████████╗██╗   ██╗
╚══██╔══╝██╔══██╗██╔══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝╚██╗ ██╔╝
   ██║   ██████╔╝███████║██║   ██║███████╗█████╗     ██║    ╚████╔╝ 
   ██║   ██╔═══╝ ██╔══██║██║   ██║╚════██║██╔══╝     ██║     ╚██╔╝  
   ██║   ██║     ██║  ██║╚██████╔╝███████║███████╗   ██║      ██║   
   ╚═╝   ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝   ╚═╝      ╚═╝   
""" + "\033[0m")
    print("\033[96m" + "       Made by Arghya Sikdar ©" + "\033[0m")
    print("\n")

def dir_traversal_scan(url, wordlist_file):
    try:
        with open(wordlist_file, "r") as file:
            directory_traversals = file.read().splitlines()
    except FileNotFoundError:
        print("\033[91m[!] Wordlist file not found.\033[0m")
        sys.exit(1)

    print(f"\033[93m[~] Starting scan on {url} with {len(directory_traversals)} entries...\033[0m\n")
    time.sleep(1)

    for traversal in directory_traversals:
        full_url = f"{url.rstrip('/')}/{traversal.lstrip('/')}"
        try:
            response = requests.get(full_url, timeout=5)
            if response.status_code == 200:
                if "Index of" in response.text or "Parent Directory" in response.text:
                    print(f"\033[92m[{response.status_code}] {full_url} - Directory Found\033[0m")
                else:
                    print(f"\033[94m[{response.status_code}] {full_url} - Page Found\033[0m")
            elif response.status_code == 403:
                print(f"\033[95m[{response.status_code}] {full_url} - Forbidden\033[0m")
            else:
                print(f"[{response.status_code}] {full_url}")
        except requests.RequestException:
            print(f"\033[91m[!] Error connecting to {full_url}\033[0m")

def main():
    parser = argparse.ArgumentParser(description="Directory Traversal Scanner - traversty")
    parser.add_argument("-u", "--url", required=True, help="Target URL")
    parser.add_argument("-w", "--wordlist", required=True, help="Wordlist file")

    args = parser.parse_args()

    banner()
    dir_traversal_scan(args.url, args.wordlist)

if __name__ == "__main__":
    main()
