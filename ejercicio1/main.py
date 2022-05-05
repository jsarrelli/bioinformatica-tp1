import Bio
from Bio import SeqIO

#not used
def read_file(file_name):
    for seq_record in SeqIO.parse("/Users/juliansarrelli/Downloads/" + file_name, "genbank"):
        print(seq_record.id)
        print(repr(seq_record.seq))
        print(len(seq_record))
        output = seq_record.id+".fasta"
        SeqIO.write(seq_record.seq, output, "fasta")


def convert() :
    SeqIO.convert("../sequence.gb", "genbank", "HTT.fasta", "fasta")


if __name__ == '__main__':
    #read_file("sequence.gb")
    convert()
