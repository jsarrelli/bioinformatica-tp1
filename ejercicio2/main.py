from Bio import SeqIO
from Bio.Blast import NCBIWWW
import ssl


def convert_to_fasta():
    SeqIO.convert("../sequence.gb", "genbank", "HTT.fasta", "fasta")


def buildBlast():
    record = SeqIO.read("HTT.fasta", format="fasta")
    result_handle = NCBIWWW.qblast("blastn", "nt", record.seq)
    with open("my_blast.xml", "w") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()


if __name__ == '__main__':
    convert_to_fasta()
    buildBlast()
