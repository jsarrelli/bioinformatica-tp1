import os


# Install EMBOSS Mac https://ports.macports.org/port/EMBOSS/


def translate_protein_to_nucleic_sequence(input_file):
    # https://www.ebi.ac.uk/Tools/st/emboss_backtranseq/
    # https://www.bioinformatics.nl/cgi-bin/emboss/help/backtranseq
    # backtranseq reads a protein sequence and writes the nucleic acid sequence it is most likely to have come from.
    os.system(f'backtranseq {input_file} ../output/nucleic_sequence.fasta')


def run_patmatmotifs(input_file):
    os.system(f'patmatmotifs -full -sequence {input_file} -outfile ../output/HTT.patmatmotifs')


if __name__ == '__main__':
    # translate protein sequence (ORF 11 from NM_001388492.1) to nucleic sequence
    translate_protein_to_nucleic_sequence("../output/HTT.fasta")

    run_patmatmotifs("../output/HTT.fasta")
