#!/usr/bin/env python3
"""

A Python command line app to connect to sftp servers and upload a file. 

"""

import argparse
import pysftp
import sys
from paramiko import AuthenticationException, SSHException
