import argparse
from collections import Counter
from pathlib import Path

def main(args):
    input_dirname:str=args.input_dirname
    output_filepath:str=args.output_filepath

    input_dir=Path(input_dirname)
    input_files=input_dir.glob("*.txt")

    genkeis=[]
    for input_file in input_files:
        with input_file.open("r") as r:
            for line in r:
                genkei=line.strip()
                genkeis.append(genkei)

    counter=Counter(genkeis)

    with open(output_filepath,"w") as w:
        for item in counter.most_common():
            w.write(f"{item[0]}\t{item[1]}\n")

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-i","--input_dirname",type=str)
    parser.add_argument("-o","--output_filepath",type=str)
    args=parser.parse_args()

    main(args)
