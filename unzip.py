import argparse
import shutil
from pathlib import Path
from tqdm import tqdm

def main(args):
    target_dirname:str=args.target_dirname

    target_dir=Path(target_dirname)
    zip_files=list(target_dir.glob("*.zip"))

    for zip_file in tqdm(zip_files):
        output_dir=target_dir.joinpath(zip_file.stem)
        shutil.unpack_archive(zip_file,output_dir)

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-t","--target_dirname",type=str)
    args=parser.parse_args()

    main(args)
