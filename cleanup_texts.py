import argparse
import re
import unicodedata
from pathlib import Path
from tqdm import tqdm

def main(args):
    input_dirname:str=args.input_dirname
    output_dirname:str=args.output_dirname

    input_dir=Path(input_dirname)
    text_files=list(input_dir.glob("*.txt"))

    output_dir=Path(output_dirname)
    output_dir.mkdir(parents=True,exist_ok=True)

    r1=re.compile(r"\d+")
    r2=re.compile('[!"#$%&\'\\\\()*+,-./:;<=>?@[\\]^_`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％※]')

    for text_file in tqdm(text_files):
        with text_file.open("r") as r:
            text=r.read()

        normalized_text=unicodedata.normalize("NFKC",text)
        replaced_text=r1.sub("",normalized_text)
        replaced_text=r2.sub("",replaced_text)

        output_file=output_dir.joinpath(text_file.name)
        with output_file.open("w") as w:
            w.write(replaced_text)

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-i","--input_dirname",type=str)
    parser.add_argument("-o","--output_dirname",type=str)
    args=parser.parse_args()

    main(args)
