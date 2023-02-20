#!/usr/bin/env python3
"""

A Python command line app to connect to sftp servers and upload a file. 

"""

import argparse
import pysftp
import sys
import paramiko
import os


cnopts = pysftp.CnOpts()
cnopts.hostkeys = None


# --------------------------------------------------

# -------------------------------------------------------
def list_dir(srv):
    """List all folders"""

    directory_structure = srv.listdir_attr()
    for attr in directory_structure:
        print(attr.filename)

# ------------------------------------------------------
def user_login(file_path, user, host, *args, **kwargs):
    """Log user into the server"""

    private_key = kwargs.get('private_key', None)
    password = kwargs.get('password', None)

    if password or os.path.expanduser(private_key):
        try:
            srv = pysftp.Connection(host=host, username=user, password=password, private_key=private_key, cnopts=cnopts)
            print("You have been successfully connected to the server...")
        except AuthenticationException as e:
            print(e)
            sys.exit(1)
        except FileNotFoundError as e:
            print(e)
            sys.exit(1)
    else:
        print("Something is wrong with the password or the ssh key does not exists.")
        sys.exit(1)

    list_dir(srv)
    if srv.exists('EDS837Submissions'):
        srv.chdir('EDS837Submissions')
    else:
        create_folders(srv)
    list_dir(srv)
    srv.put(file_path)
    list_dir(srv)
    srv.close()  


   
# #---------------------------------------------------
# def user_login(file_path, user, host, password=None, private_key=None):
#     cnopts = pysftp.CnOpts()
#     cnopts.hostkeys = None
#     """Connect to sftp server and upload file"""
#     if password:
#         try:
#             with pysftp.Connection(host, username=user, password=password) as sftp:
#                 sftp.put(file_path)
#                 print(f"File uploaded to {host} as {user}")
#         except Exception as e:
#             print(e)
#             sys.exit(1)

#     elif private_key:
#         try:
#             with pysftp.Connection(host=host, username=user, password=password, private_key=private_key, cnopts=cnopts) as sftp:
#                 sftp.put(file_path)
#                 print(f"File uploaded to {host} as {user}")
#         except Exception as e:
#             print(e)
#             sys.exit(1)

#     else:
#         print("No password or private key provided")
#         sys.exit(1)

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
    if args.password or (args.privatekey and args.ssh):
        user_login(file_path, user, host, password=password, private_key=privatekey)


# --------------------------------------------------
if __name__ == "__main__":
    main()
