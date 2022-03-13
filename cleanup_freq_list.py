import argparse
import re

def main(args):
    input_filepath:str=args.input_filepath
    output_filepath:str=args.output_filepath

    words=[]
    freqs=[]

    with open(input_filepath,"r") as r:
        for line in r:
            line=line.strip()
            word,freq=line.split("\t")
            freq=int(freq)

            words.append(word)
            freqs.append(freq)

    r1=re.compile('[!"#$%&\'\\\\()*+,-./:;<=>?@[\\]^_`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％※]')

    for word in words:
        if r1.match(word):
            idx=words.index(word)

            words.pop(idx)
            freqs.pop(idx)

    with open(output_filepath,"w") as w:
        for word,freq in zip(words,freqs):
            w.write(f"{word}\t{freq}\n")

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-i","--input_filepath",type=str)
    parser.add_argument("-o","--output_filepath",type=str)
    args=parser.parse_args()

    main(args)
