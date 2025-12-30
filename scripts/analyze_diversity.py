#!/usr/bin/env python3
"""
Script to analyze shark species diversity from sighting data.
Reads the sightings_2020.csv file and prints the total number of unique shark species observed.
"""

import csv
import os

def main():
    # Path to the CSV file relative to this script's location
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'sightings_2020.csv')
    
    unique_species = set()
    
    try:
        with open(csv_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                species = row['species'].strip()
                if species:
                    unique_species.add(species)
        
        print(f"Total unique shark species observed: {len(unique_species)}")
        print("Species list:", ', '.join(sorted(unique_species)))
        
    except FileNotFoundError:
        print(f"Error: Could not find file at {csv_path}")
    except Exception as e:
        print(f"Error reading CSV: {e}")

if __name__ == '__main__':
    main()