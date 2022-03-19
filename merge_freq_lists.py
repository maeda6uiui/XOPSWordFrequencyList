import argparse

def main(args):
    input_filepaths:str=args.input_filepaths
    output_filepath:str=args.output_filepath

    input_filepaths=input_filepaths.split(",")

    genkei_freqs={}
    for input_filepath in input_filepaths:
        with open(input_filepath,"r") as r:
            for line in r:
                line=line.strip()
                genkei,freq=line.split("\t")
                freq=int(freq)

                if genkei in genkei_freqs:
                    genkei_freqs[genkei]+=freq
                else:
                    genkei_freqs[genkei]=freq

    genkei_freqs=dict(sorted(genkei_freqs.items(),key=lambda item:item[1],reverse=True))

    with open(output_filepath,"w") as w:
        for genkei,freq in genkei_freqs.items():
            w.write(f"{genkei}\t{freq}\n")

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-i","--input_filepaths",type=str)
    parser.add_argument("-o","--output_filepath",type=str)
    args=parser.parse_args()

    main(args)
