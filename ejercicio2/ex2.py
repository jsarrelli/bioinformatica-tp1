from Bio import SeqIO
from Bio.Blast import NCBIWWW


def execute_blast():
    record = SeqIO.read("../output/HTT.fasta", format="fasta")
    result_handle = NCBIWWW.qblast("blastp", "nr", record.seq)
    with open("../output/blast_result.xml", "w") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()


if __name__ == '__main__':
    execute_blast()
