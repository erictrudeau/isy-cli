#!/usr/bin/env python
# encoding: utf-8
#
# isy-cli
# Written by Eric Trudeau
#
# This work is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License.
# To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/
#
# ISY API Docs:  http://wiki.universal-devices.com/index.php?title=ISY-99i_Series_INSTEON:REST_Interface
# ISY URL Format:  http://isy/rest/nodes
#
# Python Requests
# http://docs.python-requests.org/en/latest/index.html
# https://github.com/kennethreitz/requests
#


##### START EDITS

server		= 'isy'
username	= 'admin'
password	= 'admin'

devices = {
	'lamp':			'A1 B2 C3 1',
	'fan':			'C3 B2 A1 1',
}

##### END EDITS


import requests
import sys


base_url	= 'http://%s/rest' % server

commands = {
	'on':			'/cmd/DON',
	'off':			'/cmd/DOF',
	'on_fast':		'/cmd/DFON',
	'off_fast':		'/cmd/DFOF',
}


def execute(device, command, base_url=base_url, username=username, password=password):
	url = '%s/nodes/%s%s' % (base_url, device, command)
	print url
	return requests.get(url, auth=(username, password))


try:
	requested_device	= sys.argv[1]
	requested_command	= sys.argv[2]
except IndexError:
	print 'Error: You must supply the device and command.'
	print 'Example: isy fan on'
	exit(1)

if requested_device in devices:
	if requested_command in commands:
		r = execute(devices[requested_device], commands[requested_command])

		if r.status_code == 200:
			print 'OK'
		elif r.status_code == 404:
			print 'Error 404: Page and/or device not found'
		else:
			print r.status_code
		
	elif int(requested_command) in range(0,256):
		r = execute(devices[requested_device], ('%s/%s' % (commands['on'], requested_command)))

		if r.status_code == 200:
			print 'OK'
		elif r.status_code == 404:
			print 'Error 404: Page and/or device not found'
		else:
			print r.status_code
			
	else:
		print 'Command "%s" not found.' % requested_command
	
	
else:
	print 'Error: Device "%s" not found.' % requested_device

