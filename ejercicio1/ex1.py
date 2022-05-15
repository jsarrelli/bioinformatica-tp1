from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


def read_file(file_name):
    for seq_record in SeqIO.parse(file_name, "genbank"):
        # Usamos ORF-11
        sub_sequence = seq_record.seq[145:9574]
        aa_sequence = SeqRecord(
            Seq(sub_sequence).translate(to_stop=True),
            id="NP_001375421.1"
        )
        SeqIO.write(aa_sequence, "../output/HTT.fasta", "fasta")


if __name__ == '__main__':
    read_file("../input/sequence.gb")
