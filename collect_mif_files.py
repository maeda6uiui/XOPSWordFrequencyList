import argparse
import shutil
from pathlib import Path
from typing import List

def get_mif_files(input_root_dir:Path)->List[Path]:
    extensions=["mif","MIF"]

    mif_files:List[Path]=[]
    for extension in extensions:
        mif_files.extend(input_root_dir.glob("**/*."+extension))

    return mif_files

def main(args):
    input_root_dirname:str=args.input_root_dirname
    output_dirname:str=args.output_dirname

    input_root_dir=Path(input_root_dirname)
    mif_files=get_mif_files(input_root_dir)

    output_dir=Path(output_dirname)
    output_dir.mkdir(parents=True,exist_ok=True)
    
    count=0
    for mif_file in mif_files:
        dest_file=output_dir.joinpath(str(count)+".txt")
        shutil.copy(mif_file,dest_file)

        count+=1

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-i","--input_root_dirname",type=str)
    parser.add_argument("-o","--output_dirname",type=str)
    args=parser.parse_args()

    main(args)
