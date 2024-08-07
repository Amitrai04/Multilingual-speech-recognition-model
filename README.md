Open Command Prompt:

    Navigate to the directory where you want to download the file. For example:

    sh

    cd C:\Users\Administrator\Desktop\Project

Download the File Using curl:

sh

curl -O https://dl.fbaipublicfiles.com/dpr/wikipedia_split/psgs_w100.tsv.gz

This command will download the psgs_w100.tsv.gz file to C:\Users\Administrator\Desktop\Project.

Unzip the File Using Python:

Create a Python script or run the following Python code to unzip the file:

python

import gzip
import shutil

with gzip.open('psgs_w100.tsv.gz', 'rb') as f_in:
    with open('psgs_w100.tsv', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

Save this script as unzip_psgs_w100.py and run it:

sh

    python unzip_psgs_w100.py

    After running this script, you will have psgs_w100.tsv in C:\Users\Administrator\Desktop\Project.

Location of Files

    Downloaded File: C:\Users\Administrator\Desktop\Project\psgs_w100.tsv.gz
    Unzipped File: C:\Users\Administrator\Desktop\Project\psgs_w100.tsv

Converting TSV to PKL Format

    Run the Preprocessing Script:

    sh

python data/wikipedia_split/preprocess.py --source_path C:\Users\Administrator\Desktop\Project\psgs_w100.tsv --output_path C:\Users\Administrator\Desktop\Project\psgs_w100.tsv.pkl

Move the Preprocessed File:

sh

    mkdir C:\Users\Administrator\Desktop\Project\local_dataset
    move C:\Users\Administrator\Desktop\Project\psgs_w100.tsv.pkl C:\Users\Administrator\Desktop\Project\local_dataset\

Final Directory Structure

arduino

Project/
├── main.py
├── transcribe.py
├── query_rag.py
├── unzip_psgs_w100.py (optional, can be deleted after use)
├── psgs_w100.tsv (optional, can be deleted after conversion)
└── local_dataset/
    └── psgs_w100.tsv.pkl
