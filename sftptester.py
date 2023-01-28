#!/usr/bin/env python3
"""

A Python command line app to connect to sftp servers and upload a file. 

"""

import argparse
import pysftp
import sys
from paramiko import AuthenticationException, SSHException


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description="sftp command line options",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("-a", "--hostname", metavar="str", help="sftp server address")

    parser.add_argument("-u", "--username", metavar="str", help="sftp username")

    parser.add_argument("-p", "--password", metavar="str", help="sftp password")

    parser.add_argument(
        "-s",
        "--ssh",
        default=False,
        action="store_true",
        help="Indicate if using ssh key",
    )

    parser.add_argument("-f", "--filepath", metavar="str", help="File path to upload")

    parser.add_argument("-k", "--privatekey", metavar="str", help="SSH Key to use")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Get the command line arguments and run the functions"""

    args = get_args()
    host = args.hostname
    user = args.username
    password = args.password
    file_path = args.filepath
    privatekey = args.privatekey
    ssh = args.ssh

    if args.password or (args.privatekey and args.ssh == True):
        user_login(file_path, user, host, password=password, private_key=privatekey)


# --------------------------------------------------
if __name__ == "__main__":
    main()
