# DNA LLM Model

The purpose of this project is to train various LLMs to identify key markers in DNA sequences.  

# Table of Contents
1. [Team Members](#team-members)
2. [Current Tasks](#current-tasks)
4. [Resources](#resources)

## Team Members <a name="team-members"></a>

- Pari Sharma 
- Mahek Kothari 
  
## Current Tasks <a name="current-tasks"></a>

| Task :                                         | Due Date:        | Status:     |
| ---------------------------------------------- | ---------------- | ----------- |
| Explore models BERT, GPT, transformer          | Friday (2/28)    | Completed   |
| Download EPD and UCSC Genome Browser DB        | Friday (3/07)    | In Progress |
| Preprocess DNA sequences via k-mer tokenization + train a baseline model| Friday (3/14) | In Progress |
| Self-supervised vs. supervised learning approaches| Friday (3/21) | In Progress |
| Evaluate models, graphs + visulizations        | Friday    (3/28) | In Progress |
| Debug/refine hyperparameters (batch/learning rate) | Tuesday    (4/15) | In Progress |

# DNA Promoter Classification

This project classifies promoter vs. non-promoter regions in the human genome using machine learning.

## 🧬 Dataset

- Extracted from human chromosome 1 (`chr1.fa`)
- 1000 promoter sequences (200 bp upstream of gene start)
- 1000 non-promoter sequences (200 bp random from non-promoter regions)
- Final dataset: `Data/labeled_sequences.csv`

## 🔧 Tools Used

- `bedtools`, `awk` for data extraction
- `Biopython` for FASTA parsing
- Python + scikit-learn or PyTorch/TensorFlow (upcoming)

## 📁 Directory Structure


## Resources <a name="resources"></a>


