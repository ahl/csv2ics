#!/usr/bin/python

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# Copyright (c) 2016, Adam H. Leventhal. All rights reserved.

#
# Requires: dateparser, ics, csv
#

from __future__ import print_function
import csv
import sys
from ics import Calendar, Event
import dateparser

def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)

def fail(*objs):
    print(*objs, file=sys.stderr)
    os.exit(1)

# ignore characters I can't print
reload(sys)
sys.setdefaultencoding('utf8')

c = Calendar()


with sys.stdin as csvfile:
	reader = csv.DictReader(csvfile)

	for field in reader.fieldnames:
		if not field in ['summary', 'location', 'dtstart', 'dtend']:
			warning("the field '%s' is ignored" % field)

		for field in ['summary', 'location', 'dtstart', 'dtend']:
			if not field in reader.fieldnames:
				fail("missing field '%s'" % field)

	for row in reader:
		dtstart = dateparser.parse(row['dtstart'])
		dtend = dateparser.parse(row['dtend'])
		e = Event(
			name = row['summary'],
			location = row['location'],
			begin = dtstart.strftime("%Y-%m-%dT%H:%M:00"),
			end = dtend.strftime("%Y-%m-%dT%H:%M:00"),
		)
		c.events.append(e)

with sys.stdout as f:
	f.writelines(c)
