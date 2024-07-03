#!/usr/bin/python3
import argparse
import os
from colorama import Fore, Style
from tabulate import tabulate

def report(valid_domains, invalid_domains):
    print("\n")
    print(Fore.GREEN + 'Summery Report:\n' + Style.RESET_ALL)

    num_valid_domains = len(valid_domains)
    num_invalid_domains = len(invalid_domains)


    table = [["Number of valid domains", num_valid_domains],
             ["Number of invalid domains", num_invalid_domains]]

    print(tabulate(table, headers=["Name", "Quantity",], tablefmt="github"))


def validate_domains(domains, valid_tlds, exclude=""):
    valid_domains = []
    invalid_domains = []
    exclude_tld = exclude
    valid_tlds_set = set(valid_tlds)
    for domain in domains:
        if any(domain.endswith(tld) for tld in valid_tlds_set):
            if exclude_tld != None:
                if domain.endswith(exclude_tld):
                    invalid_domains.append(domain)
                else:
                    valid_domains.append(domain)
            else:
                valid_domains.append(domain)
        else:
            invalid_domains.append(domain)
    return valid_domains, invalid_domains

def main():
    parser = argparse.ArgumentParser(description='TLD validation')
    parser.add_argument("-df", "--domains", help="domains file", required=True)
    parser.add_argument("-tf", "--validtld", help="valid TLD file", required=False)
    parser.add_argument("-in", "--invaliddomains", help="invalid domains list in result",action="store_true", required=False)
    parser.add_argument("-ex", "--exclude", help="exclude tld", required=False)
    parser.add_argument("-s", "--silent", help="silent report", action="store_true", required=False)


    args = parser.parse_args()

    try:
        if args.domains:
            with open(args.domains, "r") as file:
                domains = [domain.strip() for domain in file.readlines()]
        else:
            print("Error: Domains file Does not exist or is not readable.")

        if args.validtld:
            with open(args.validtld, "r") as file:
                valid_tlds = [tld.strip() for tld in file.readlines()]
        else:
            with open("valid_tld.txt", "r") as file:
                valid_tlds = [tld.strip() for tld in file.readlines()]  
        
        valid_domains, invalid_domains = validate_domains(domains, valid_tlds,args.exclude)


        if args.invaliddomains:
            for domain in invalid_domains:
                print(f"{domain}")
        else:
            for domain in valid_domains:
                print(f"{domain}")
        if args.silent == True:
            pass
        else:
            report(valid_domains,invalid_domains)
    except (IOError, ValueError) as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
