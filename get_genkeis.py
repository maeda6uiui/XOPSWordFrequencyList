import argparse
import MeCab
import os
from pathlib import Path
from tqdm import tqdm

def main(args):
    input_dirname:str=args.input_dirname
    output_dirname:str=args.output_dirname

    input_dir=Path(input_dirname)
    text_files=list(input_dir.glob("*.txt"))

    output_dir=Path(output_dirname)
    output_dir.mkdir(parents=True,exist_ok=True)

    tagger=MeCab.Tagger()

    for text_file in tqdm(text_files):
        with text_file.open("r") as r:
            lines=r.read().splitlines()

        genkeis=[]
        for line in lines:
            node=tagger.parseToNode(line)
            while node:
                genkei=node.feature.split(",")[6]
                if genkei!="*":
                    genkeis.append(genkei)
                
                node=node.next

        output_file=output_dir.joinpath(text_file.name)
        with output_file.open("w") as w:
            for genkei in genkeis:
                w.write(genkei)
                w.write("\n")

if __name__=="__main__":
    os.environ["MECABRC"]="/etc/mecabrc"

    parser=argparse.ArgumentParser()
    parser.add_argument("-i","--input_dirname",type=str)
    parser.add_argument("-o","--output_dirname",type=str)
    args=parser.parse_args()

    main(args)
