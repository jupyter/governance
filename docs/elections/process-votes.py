#!/usr/bin/env python3
# Convert Jupyter Executive Council vote data from CSV to Apache STeVe format.

from datetime import datetime
import csv
import re
import string
import uuid

def extract_candidate_name(header):
    """Extract candidate name from header column."""
    match = re.search(r'\[(.*?)\]', header)
    if match:
        return match.group(1)
    return None

def main():
    # Read the CSV file
    with open('votes.csv', 'r', encoding='utf-8') as vote_file:
        reader = csv.DictReader(vote_file)
        headers = reader.fieldnames
        
        # Find candidate columns and extract names
        candidate_columns = []
        candidates = []
        for header in headers:
            if '[' in header and ']' in header:
                candidate_name = extract_candidate_name(header)
                if candidate_name:
                    candidate_columns.append(header)
                    candidates.append(candidate_name)

        # Create board_nominations.ini
        letters = list(string.ascii_lowercase)
        with open('board_nominations.ini', 'w', encoding='utf-8') as candidate_file:
            candidate_file.write('[nominees]\n')
            for idx, candidate in enumerate(candidates):
                candidate_file.write(f'{letters[idx]}: {candidate}\n')

        # Process votes and create votedata.txt
        with open('votedata.txt', 'w', encoding='utf-8') as vote_output:
            for row in reader:
                # Skip if they chose not to vote
                if row['Vote or abstain'].lower() != 'i would like to vote!':
                    continue

                # Process candidate rankings
                candidate_priorities = [' '] * len(candidates)
                
                # Fill in priorities
                for idx, col in enumerate(candidate_columns):
                    rank = row[col]
                    if rank and rank.strip() and rank.isdigit():
                        rank_int = int(rank)
                        # Adjust for 0-based indexing
                        candidate_priorities[rank_int - 1] = letters[idx]

                # Filter out empty spaces and join
                vote_string = ''.join(x for x in candidate_priorities if x != ' ')
                
                # This is normally to dedupe multiple votes by the same voter,
                # but Google Forms already does that, so we instead assume that
                # every vote is unique and cast at the current time
                timestamp = datetime.now().strftime('[%Y/%m/%d %H:%M:%S]')
                voterhash = uuid.uuid4().hex

                # Only write if there's actually a vote
                if vote_string:
                    vote_output.write(f'{timestamp} {voterhash} {vote_string}\n')

if __name__ == '__main__':
    main()
