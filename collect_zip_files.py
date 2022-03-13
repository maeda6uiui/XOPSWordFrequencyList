import argparse
import shutil
from pathlib import Path
from typing import List

def get_zip_files(input_root_dir:Path)->List[Path]:
    extensions=["zip","ZIP"]

    zip_files:List[Path]=[]
    for extension in extensions:
        zip_files.extend(input_root_dir.glob("**/*."+extension))

    return zip_files

def main(args):
    input_root_dirname:str=args.input_root_dirname
    output_dirname:str=args.output_dirname

    input_root_dir=Path(input_root_dirname)
    zip_files=get_zip_files(input_root_dir)

    output_dir=Path(output_dirname)
    output_dir.mkdir(parents=True,exist_ok=True)
    
    count=0
    for zip_file in zip_files:
        #駄場のアドオンについては複数バージョンのZIPファイルが存在するため、手動でコピーする
        if "駄場"in str(zip_file):
            continue

        dest_file=output_dir.joinpath(str(count)+".zip")
        shutil.copy(zip_file,dest_file)

        count+=1

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-i","--input_root_dirname",type=str)
    parser.add_argument("-o","--output_dirname",type=str)
    args=parser.parse_args()

    main(args)
