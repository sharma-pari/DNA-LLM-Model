# DNA LLM Model

The purpose of this project is to train various large language models (LLMs) to identify key markers in DNA sequences such as promoters vs. non-promoter regions.

---

## Table of Contents

1. [Team Members](#team-members)
2. [Current Tasks](#current-tasks)
3. [Dataset](#dataset)
4. [Goals](#goals)
5. [Tools & Libraries](#tools--libraries)
6. [Getting Started](#getting-started)
7. [Resources](#resources)

---

## Team Members

- Pari Sharma  
- Mahek Kothari

---

## Current Tasks

| Task                                                    | Due Date        | Status      |
|----------------------------------------------------------|------------------|-------------|
| Explore models: BERT, GPT, transformer                   | Friday (2/28)    | Completed   |
| Download EPD and UCSC Genome Browser DB                  | Friday (3/07)    | Completed |
| Preprocess DNA sequences (k-mer tokenization) + baseline | Friday (3/14)    | In Progress |
| Compare self-supervised vs. supervised learning          | Friday (3/21)    | In Progress |
| Evaluate models + create visualizations                  | Friday (3/28)    | In Progress |
| Debug/refine hyperparameters (batch size, learning rate) | Tuesday (4/15)   | In Progress |

---

## Dataset

- **Source**: Human chromosome 1 (`chr1.fa`)
- **Promoters**: 200 bp upstream of transcription start sites
- **Non-promoters**: 200 bp random intergenic regions (non-overlapping)
- **Format**: FASTA → CSV (`sequence`, `label`)
  - Label `1` = Promoter
  - Label `0` = Non-promoter

---

## Goals

- Build a binary classifier to distinguish promoter vs. non-promoter DNA sequences
- Benchmark models:
  - Logistic Regression / Random Forest (baseline)
  - Convolutional Neural Network (CNN)
  - Transformer-based (DNABERT / custom)
- Visualize performance: ROC curves, confusion matrices, etc.

---

## Tools & Libraries

- `bedtools`, `awk` — for genomic interval processing
- `Biopython` — for FASTA parsing
- `Python`, `Pandas`, `NumPy`, `scikit-learn` — for preprocessing and baseline models
- `PyTorch` or `TensorFlow` — for deep learning models

---

## Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/sharma-pari/DNA-LLM-Model.git
   cd DNA-LLM-Model
