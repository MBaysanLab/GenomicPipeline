
class GetPaths(object):
    def __init__(self):
        # Path of tools
        self.picard_path = "/home/.../Desktop/Genomicswork/picard.jar"
        self.gatk_path = "/home/.../Desktop/Genomicswork/GenomeAnalysisTK.jar"
        self.gatk4_path = "/home/.../Desktop/Genomicswork/gatk-4.1.2.0/gatk"
        self.ref_dir = "/home/.../Desktop/Genomicswork/ref_genome_indexes/hg38_bundle/"
        self.varscan_path = "/home/.../Desktop/Genomicswork/VarScan.v2.3.9.jar"
        self.dbsnp = "/home/.../Desktop/Genomicswork/ref_genome_indexes/hg38_bundle/dbsnp_146.hg38.vcf" \
                     ".gz"
        self.mills_indel = "/home/.../Desktop/Genomicswork/ref_genome_indexes/hg38_bundle/Mills_and_1000G_gold_standard.indels.hg38.vcf.gz"
        self.fastqc = "/home/.../Desktop/Genomicswork/FastQC/fastqc"
        self.fastp = "/home/.../Desktop/Genomicswork/fastp/fastp"
        self.cosmic = "/home/.../Desktop/Genomicswork/ref_genome_indexes/hg19_bundle/cosmic_hg19_lifted_over.vcf"
        self.annovar = "/home/.../Desktop/Genomicswork/annovar/"
        self.strelka = "/home/.../Desktop/Genomicswork/strelka-2.9.10.centos6_x86_64/bin/configureStrelkaSomaticWorkflow.py"
        self.caveman = "/home/.../Desktop/Genomicswork/CaVEMan-dev/bin/caveman"
        self.one_thousand_g = "/home/.../Desktop/Genomicswork/ref_genome_indexes/hg38_bundle/1000G_phase1.snps.high_confidence.hg38.vcf.gz"
