#!/usr/bin/env python3

import sys
import logging
import os

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, os.getcwd() + "/src")

from src.anglers_banking.app import app as application
