#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
from wabr import  WAUtils, WABarcodeReader
from sample_code import  Test

# enable debugging 
import cgitb
cgitb.enable()

# ============  Configure print of UTF8 filenames and barcode data to stdout (optional) 
WAUtils.SetStdoutUTF8()

# ============  Configure server
serverUrl = ""  #  Your server URL (default is wanr.inliteresearch.com)
auth = ""       #  Your Authorization code or  WABR_AUTH environment variable is used

reader = WABarcodeReader(serverUrl, auth)

# ============  Enable diagnostic output (optional)
WAUtils.bShowDiag = True
WAUtils.printDiag("\nSERVER: " + reader._serverUrl  +  "      PYTHON VERSION: " + str(sys.version_info[0]) + "." + str(sys.version_info[1]) + "." + str(sys.version_info[2]) + "\n")

# Run test
Test.Run(reader)


