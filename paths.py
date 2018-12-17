
class GetPaths(object):
    def __init__(self):
        self.picard_path = "/home/bioinformaticslab/Desktop/GenomicsWorks/picard.jar"
        self.gatk_path = "/home/bioinformaticslab/Desktop/GenomicsWorks/GenomeAnalysisTK.jar"
        self.gatk4_path = "/home/bioinformaticslab/Desktop/GenomicsWorks/gatk-4.0.3.0/gatk"
        self.ref_dir = "/home/bioinformaticslab/Desktop/GenomicsWorks/ref_genome_indexes/hg38_bundle/"
        self.varscan_path = "/home/bioinformaticslab/Desktop/GenomicsWorks/VarScan.v2.3.9.jar"
        self.dbsnp = "/home/bioinformaticslab/Desktop/GenomicsWorks/ref_genome_indexes/hg38_bundle/dbsnp_146.hg38.vcf" \
                     ".gz"
        self.mills_indel = "/home/bioinformaticslab/Desktop/GenomicsWorks/ref_genome_indexes/hg38_bundle" \
                           "/Mills_and_1000G_gold_standard.indels.hg38.vcf.gz"
        self.fastqc = "/home/bioinformaticslab/Desktop/GenomicsWorks/FastQC/fastqc"
        self.fastp = "/home/bioinformaticslab/Desktop/GenomicsWorks/fastp/fastp"
        self.cosmic = "/home/bioinformaticslab/Desktop/GenomicsWorks/ref_genome_indexes/hg19_bundle/cosmic_hg19_lifted_over.vcf"
        self.annovar = "/home/bioinformaticslab/Desktop/GenomicsWorks/annovar/"
        self.strelka = "/home/bioinformaticslab/Desktop/GenomicsWorks/strelka-2.9.2.centos6_x86_64/bin/configureStrelkaSomaticWorkflow.py"

        self.one_thousand_g = "/home/bioinformaticslab/Desktop/GenomicsWorks/ref_genome_indexes/hg38_bundle/1000G_phase1.snps.high_confidence.hg38.vcf.gz"
