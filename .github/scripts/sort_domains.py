#!/usr/bin/env python3
"""
Sort domains in YAML payload files alphabetically.

Expected file format:
    payload:
      # Section header (optional comment)
      - '+.domain1.com'
      - '+.domain2.com'
      
      # Another section (optional)
      - 'www.domain3.com'

The script:
- Preserves the 'payload:' header
- Preserves section headers (lines starting with #)
- Sorts domain entries (lines starting with "- '") within each section alphabetically
- Domain entries must be enclosed in single quotes
"""

import sys
import re


def extract_domain_for_sorting(line):
    """Extract the domain value from a YAML list entry for sorting purposes."""
    # Match pattern: optional whitespace, -, whitespace, 'domain'
    match = re.match(r"\s*-\s*'([^']*)'", line)
    if match:
        return match.group(1).lower()
    return line.lower()


def sort_yaml_domains(input_file):
    """Sort domains in a YAML payload file while preserving structure."""
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    result = []
    current_section_header = None
    current_domains = []
    in_payload = False

    for line in lines:
        stripped = line.rstrip()

        # Handle payload header
        if stripped == 'payload:':
            result.append(stripped)
            in_payload = True
            continue

        if not in_payload:
            result.append(stripped)
            continue

        # Check if it's a comment line (section header)
        if stripped.lstrip().startswith('#'):
            # Sort and add previous section's domains
            if current_domains:
                current_domains.sort(key=extract_domain_for_sorting)
                result.extend(current_domains)
                current_domains = []

            # Handle empty line before comment
            if current_section_header is not None or len(result) > 1:
                result.append('')
            current_section_header = stripped
            result.append(current_section_header)
            continue

        # Check if it's a domain entry
        if stripped.lstrip().startswith("- '"):
            current_domains.append(stripped)
            continue

        # Handle empty lines (skip them, we'll add them back between sections)
        if not stripped:
            continue

        # Other lines (shouldn't happen but keep them)
        result.append(stripped)

    # Sort and add remaining domains
    if current_domains:
        current_domains.sort(key=extract_domain_for_sorting)
        result.extend(current_domains)

    with open(input_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(result) + '\n')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <yaml_file>")
        sys.exit(1)
    
    sort_yaml_domains(sys.argv[1])
    print(f"Sorted: {sys.argv[1]}")
