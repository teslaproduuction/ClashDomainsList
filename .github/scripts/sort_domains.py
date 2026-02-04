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

Usage:
    python3 sort_domains.py <file>               # Sort domains in place
    python3 sort_domains.py --extract <file>     # Extract domains to stdout
"""

import sys
import re


# Regex pattern to match domain entries: "  - 'domain'"
DOMAIN_PATTERN = re.compile(r"\s*-\s*'([^']*)'")


def extract_domain(line):
    """Extract the domain value from a YAML list entry.
    
    Returns the domain string or None if the line doesn't match the pattern.
    """
    match = DOMAIN_PATTERN.match(line)
    if match:
        return match.group(1)
    return None


def extract_domain_for_sorting(line):
    """Extract the domain value from a YAML list entry for sorting purposes."""
    domain = extract_domain(line)
    if domain:
        return domain.lower()
    return line.lower()


def extract_all_domains(input_file):
    """Extract all domains from a YAML payload file."""
    domains = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            domain = extract_domain(line)
            if domain:
                domains.append(domain)
    return domains


def deduplicate_domains(domains):
    """Remove duplicate domain entries (case-insensitive comparison).
    
    Returns a list of unique domain lines, preserving the first occurrence.
    """
    seen = set()
    unique_domains = []
    for line in domains:
        domain = extract_domain(line)
        if domain:
            domain_lower = domain.lower()
            if domain_lower not in seen:
                seen.add(domain_lower)
                unique_domains.append(line)
        else:
            unique_domains.append(line)
    return unique_domains


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
            # Deduplicate first, then sort for better performance
            if current_domains:
                current_domains = deduplicate_domains(current_domains)
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

    # Deduplicate first, then sort for better performance
    if current_domains:
        current_domains = deduplicate_domains(current_domains)
        current_domains.sort(key=extract_domain_for_sorting)
        result.extend(current_domains)

    with open(input_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(result) + '\n')


def print_usage():
    """Print usage information."""
    print(f"Usage: {sys.argv[0]} <file>")
    print(f"       {sys.argv[0]} --extract <file>")
    print()
    print("Options:")
    print("  <file>           Sort domains in the file in place")
    print("  --extract <file> Extract domains from the file to stdout")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    if sys.argv[1] == '--extract':
        if len(sys.argv) != 3:
            print_usage()
            sys.exit(1)
        domains = extract_all_domains(sys.argv[2])
        for domain in domains:
            print(domain)
    else:
        if len(sys.argv) != 2:
            print_usage()
            sys.exit(1)
        sort_yaml_domains(sys.argv[1])
        print(f"Sorted: {sys.argv[1]}")
