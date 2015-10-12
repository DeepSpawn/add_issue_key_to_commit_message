#!/usr/bin/env python

import sys, re
from subprocess import check_output

commit_msg_filepath = sys.argv[1]

issue_key_regex = "([A-Z][A-Z]+-\d+)"

branch = check_output(['git', 'symbolic-ref', '--short', 'HEAD']).strip()
issue_key_match = re.match(issue_key_regex, branch)
if issue_key_match:
    issue_key = issue_key_match.group(0)

    with open(commit_msg_filepath, 'r+') as f:
        content = f.read()
    	f.seek(0)
    	f.write("%s: \n%s" % (issue_key,content))        
