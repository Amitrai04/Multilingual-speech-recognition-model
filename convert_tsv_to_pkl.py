import pandas as pd
import sys

def convert_tsv_to_pkl(tsv_path, pkl_path):
    # Read the TSV file into a DataFrame
    df = pd.read_csv(tsv_path, sep='\t')
    # Save the DataFrame to a PKL file
    df.to_pickle(pkl_path)
    print(f"Successfully converted {tsv_path} to {pkl_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_tsv_to_pkl.py <input_tsv_path> <output_pkl_path>")
    else:
        tsv_path = sys.argv[1]
        pkl_path = sys.argv[2]
        convert_tsv_to_pkl(tsv_path, pkl_path)
