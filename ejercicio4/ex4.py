import sys

from Bio import Entrez
from Bio import SeqIO
from Bio.Blast import NCBIXML
from Bio.SeqRecord import SeqRecord


def look_for_matches(pattern):
    print(f"Searching for hit with pattern: {pattern}")
    result_handle = open("./output/blast_result.xml")
    blast_record = NCBIXML.read(result_handle)
    for alignment in blast_record.alignments:
        description = alignment.hit_def
        if pattern in description:
            print(f"Hit: {description} / id: {alignment.accession}")
            download_records(alignment.hit_id, description)


def download_records(accession_number, description):
    Entrez.email = "julisarrelli@gmail.com"
    handle = Entrez.efetch(db="protein", id=accession_number, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()
    sequence = SeqRecord(seq=record.seq, id="NP_001375421.1", description=description)
    SeqIO.write(sequence, f"./output/ejercicio4/{description}.fasta", "fasta")


if __name__ == '__main__':
    parameter_pattern = sys.argv[1]
    look_for_matches(parameter_pattern)
