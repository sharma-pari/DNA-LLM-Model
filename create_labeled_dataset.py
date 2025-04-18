from Bio import SeqIO
import csv

def fasta_to_labeled_list(fasta_path, label):
    records = SeqIO.parse(fasta_path, "fasta")
    return [(str(record.seq), label) for record in records]

# Load promoter and non-promoter sequences
promoters = fasta_to_labeled_list("Data/promoters_sample_5k.fa", 1)
non_promoters = fasta_to_labeled_list("Data/non_promoters_sample_5k.fa", 0)

# Combine and shuffle
all_sequences = promoters + non_promoters

import random
random.shuffle(all_sequences)

# Write to CSV
with open("Data/labeled_sequences.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["sequence", "label"])
    writer.writerows(all_sequences)

print("Labeled dataset saved to Data/labeled_sequences.csv")
