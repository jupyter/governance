# Convert Jupyter Executive Council vote data from CSV to Apache STeVe format.
#
# This script is in the public domain.

from datetime import datetime
import re
import string
import uuid

# Read a file in, line by line, and process it

vote_file = open('votes.csv', 'r')

headerline = vote_file.readline()

# Assign letters to each candidate
candidates = headerline.split(',')

letters = list(string.ascii_lowercase)

with open('board_nominations.ini', 'w') as candidate_file:
    candidate_file.write('[nominees]\n')

    for idx, c in enumerate(candidates):
        # Extract the candidate's name inside the brackets
        candidate_name = re.split(r'[\[\]]', c)[1]
        candidate_file.write('{0}: {1}\n'.format(letters[idx], candidate_name))

with open('votedata.txt', 'w') as vote_output:
    for line in vote_file:
        # Sort in numerical order by index
        candidate_priorities = line.split(',')

        candidate_alphas = [' '] * len(candidate_priorities)

        for idx, c in enumerate(candidate_priorities):
            if (re.search('\d', c)):
                candidate_alphas[int(c) - 1] = letters[idx]
        
        # This is normally to dedupe multiple votes by the same voter,
        # but Google Forms already does that, so we instead assume that
        # every vote is unique and cast at the current time
        timestamp = datetime.now().strftime('[%Y/%m/%d %H:%M:%S]')
        voterhash = uuid.uuid4().hex

        vote_output.write('{0} {1} {2}\n'.format(
            timestamp,
            voterhash,
            ''.join(candidate_alphas).replace(' ', '')))
