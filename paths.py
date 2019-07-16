
class GetPaths(object):
    def __init__(self):
        self.picard_path = "/home/bioinformaticslab2/Desktop/Genomicswork/picard.jar"
        self.gatk_path = "/home/bioinformaticslab2/Desktop/Genomicswork/GenomeAnalysisTK.jar"
        self.gatk4_path = "/home/bioinformaticslab2/Desktop/Genomicswork/gatk-4.1.2.0/gatk"
        self.ref_dir = "/home/bioinformaticslab2/Desktop/Genomicswork/ref_genome_indexes/hg38_bundle/"
        self.varscan_path = "/home/bioinformaticslab2/Desktop/Genomicswork/VarScan.v2.3.9.jar"
        self.dbsnp = "//home/bioinformaticslab2/Desktop/Genomicswork/ref_genome_indexes/hg38_bundle/dbsnp_146.hg38.vcf" \
                     ".gz"
        self.mills_indel = "/home/bioinformaticslab2/Desktop/Genomicswork/ref_genome_indexes/hg38_bundle/Mills_and_1000G_gold_standard.indels.hg38.vcf.gz"
        self.fastqc = "/home/bioinformaticslab2/Desktop/Genomicswork/FastQC/fastqc"
        self.fastp = "/home/bioinformaticslab2/Desktop/Genomicswork/fastp/fastp"
        self.cosmic = "/home/bioinformaticslab2/Desktop/Genomicswork/ref_genome_indexes/hg19_bundle/cosmic_hg19_lifted_over.vcf"
        self.annovar = "/home/bioinformaticslab2/Desktop/Genomicswork/annovar/"
        self.strelka = "/home/bioinformaticslab2/Desktop/Genomicswork/strelka-2.9.10.centos6_x86_64/bin/configureStrelkaSomaticWorkflow.py"
        self.caveman = "/home/bioinformaticslab2/Desktop/Genomicswork/CaVEMan-dev/bin/caveman"
        self.one_thousand_g = "//home/bioinformaticslab2/Desktop/Genomicswork/ref_genome_indexes/hg38_bundle/1000G_phase1.snps.high_confidence.hg38.vcf.gz"
