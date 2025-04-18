import random

# Load all non-promoter regions
with open("Data/complement_200bp.bed") as f:
    lines = f.readlines()

# Sample 10,000
sample_size = min(len(lines), 10000)  # in case there are fewer than 10k
sampled = random.sample(lines, sample_size)

# Save
with open("Data/non_promoters_sample_10k.bed", "w") as f:
    f.writelines(sampled)

print(f"Sampled {len(sampled)} non-promoter regions.")
