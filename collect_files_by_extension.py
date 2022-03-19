import argparse
import shutil
from pathlib import Path
from typing import List

def get_files_by_extension(input_root_dir:Path,extension:str)->List[Path]:
    extensions=[extension.lower(),extension.upper()]

    mif_files:List[Path]=[]
    for extension in extensions:
        mif_files.extend(input_root_dir.glob("**/*."+extension))

    return mif_files

def main(args):
    input_root_dirname:str=args.input_root_dirname
    output_dirname:str=args.output_dirname
    extension:str=args.extension

    input_root_dir=Path(input_root_dirname)
    files=get_files_by_extension(input_root_dir,extension)

    output_dir=Path(output_dirname)
    output_dir.mkdir(parents=True,exist_ok=True)
    
    count=0
    for file in files:
        dest_file=output_dir.joinpath(str(count)+".txt")
        shutil.copy(file,dest_file)

        count+=1

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-i","--input_root_dirname",type=str)
    parser.add_argument("-o","--output_dirname",type=str)
    parser.add_argument("-e","--extension",type=str)
    args=parser.parse_args()

    main(args)
