# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd.
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import webnotes
from webnotes.utils import get_base_path
import os

def execute():
	# remove pyc files
	utils_pyc = os.path.join(get_base_path(), "app", "selling", "utils.pyc")
	if os.path.exists(utils_pyc):
		print exists
		os.remove(utils_pyc)
	
	# TODO remove website folder
	