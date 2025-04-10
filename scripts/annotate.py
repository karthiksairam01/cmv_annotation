#!/usr/bin/env python3
import json
import sys
import os
import argparse
from pathlib import Path

def main():

    parser = argparse.ArgumentParser(description="Annotate CMV comment relationships")
    parser.add_argument("--annotator", "-a", type=str, required=True,
                        help="Name of the annotator (used in output filename)")
    parser.add_argument("--max", "-m", type=int, default=5,
                        help="Maximum number of annotations in this session (default: 5)")
    parser.add_argument("--input", "-i", type=str, default="data/raw/cmv_usable.jsonl",
                        help="Input data file path (default: data/raw/cmv_usable.jsonl)")
    parser.add_argument("--output-dir", "-o", type=str, default="data/processed/annotations",
                        help="Output directory for annotations (default: data/processed/annotations)")
    parser.add_argument("--middleware", "-w", type=str, 
                        default="data/processed/middleware_data.json",
                        help="Middleware data file path (default: data/processed/middleware_data.json)")
    
    args = parser.parse_args()
    
    # Ensure output directories exist
    os.makedirs(os.path.dirname(args.middleware), exist_ok=True)
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Construct output file path based on annotator name
    output_file = os.path.join(args.output_dir, f"cmv_relations_{args.annotator}.json")
    
    # Function to save all current progress
    def save_progress():
        # Add new annotations to existing data
        existing_annotations.extend(annotated)
        
        # Save updated annotations
        with open(output_file, 'w') as outfile:
            json.dump(existing_annotations, outfile, indent=4)
        
        # Update middleware data
        middleware_data = {
            'roots': roots,
            'replies': replies
        }
        with open(args.middleware, 'w') as outfile:
            json.dump(middleware_data, outfile, indent=4)
        
        print(f"Saved {len(annotated)} new annotations. Total: {len(existing_annotations)}")

    # Check if input file exists
    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' not found.")
        return 1

    # Load the utterances to annotate
    with open(args.input, 'r') as infile:
        try:
            utterances = json.load(infile)
        except json.JSONDecodeError:
            print("Error: Input file is not valid JSON.")
            return 1

    print(f'Loaded {len(utterances)} utterances.')

    if os.path.exists(args.middleware):
        with open(args.middleware, 'r') as infile:
            try:
                annotation_middleware_data = json.load(infile)
                roots = annotation_middleware_data.get('roots', {})
                replies = annotation_middleware_data.get('replies', {})
            except json.JSONDecodeError:
                print("Warning: Middleware file is not valid JSON. Creating new middleware data.")
                roots = {}
                replies = {}
    else:
        print("No middleware data found. Starting with empty data.")
        roots = {}
        replies = {}

    #load existing annotations
    try:
        with open(output_file, 'r') as infile:
            existing_annotations = json.load(infile)
        print(f"Loaded {len(existing_annotations)} existing annotations for {args.annotator}.")
    except (FileNotFoundError, json.JSONDecodeError):
        existing_annotations = []
        print(f"No existing annotations found for {args.annotator}. Starting fresh.")

    # build a set of IDs that have already been annotated
    annotated_ids = set()
    for annotation in existing_annotations:
        annotated_ids.add(annotation.get('id', annotation['text']))

    annotated = []
    processed_count = 0
    annotation_count = 0
    max_annotations = args.max

    print("\nStarting annotation session...")
    print(f"Annotator: {args.annotator}")
    print(f"Maximum annotations this session: {max_annotations}")
    print("\nAnnotation Guide:")
    print("  a - Agree with parent")
    print("  s - Disagree with parent")
    print("  n - Neutral/Other relation to parent")
    print("  exit - Save and quit the session")
    print("\n" + "-" * 80 + "\n")
    
    for utterance in utterances:
        processed_count += 1
        
        if utterance['id'] == utterance['root']:
            roots[utterance['id']] = utterance['text']
            replies[utterance['id']] = utterance['text']
            continue
        
        if utterance['id'] in annotated_ids or utterance['text'] in annotated_ids:
            replies[utterance['id']] = utterance['text']
            continue
        
        text = utterance['text']
        print('\nTEXT TO ANNOTATE: ')
        print(text)
        print()
        
        reply_relation = None
        reply_to = None
        
        if utterance['reply-to']:
            try:
                reply_to = replies[utterance['reply-to']]
                print('PARENT COMMENT:')
                print(reply_to)
                print('Relation to parent comment (a/s/n) or "exit" to save and quit: ')
                user_input = input().strip().lower()
                
                if user_input == 'exit':
                    print("\nExiting annotation session...")
                    save_progress()
                    return 0
                    
                while user_input not in ['a', 's', 'n', 'exit']:
                    print("Invalid input. Please enter 'a' (agree), 's' (disagree), 'n' (neutral), or 'exit':")
                    user_input = input().strip().lower()
                    if user_input == 'exit':
                        print("\nExiting annotation session...")
                        save_progress()
                        return 0
                
                reply_relation = user_input
                print()
            except KeyError:
                print('Parent comment not available at this time.')
                print()
        else:
            print('No parent comment found for this utterance.')
        
        replies[utterance['id']] = text
        
        annotated.append({
            'id': utterance['id'],  # Store ID for easier resumption
            'text': text,
            'reply_relation': reply_relation,
            'reply_to_text': reply_to,
            'annotator': args.annotator  # Track who did this annotation
        })
        
        annotation_count += 1
        print()    
        print('-' * 80)
        print()
        
        if annotation_count >= max_annotations:
            print(f"Reached {max_annotations} annotations for this session.")
            break

    #save progress at the end of the session
    save_progress()

    print(f"Processed {processed_count} utterances, annotated {annotation_count} comments in this session.")
    print(f"Total annotations by {args.annotator}: {len(existing_annotations)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
