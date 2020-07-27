#1.public data download (FASTQ)- sratoolkit
/BiO/Install/sratoolkit.2.9.6-ubuntu64/bin/fastq-dump--split-3 SRR1002940

#2.pre processing (check law  QC reads,  before trimming ) 
/BiO/Install/FastQC_0.10.1/fastqc -t4 --nogroup SRR1002940.r1.trim.fq

#3.Trimming - use Trimmomatic
java -jar /BiO/Install/Trimmomatic-0.38/trimmomatic-0.38.jar PE -threads4 -phred33 SRR1002940.r1.temp.fq SRR1002940.r2.temp.fq SRR1002940.r1.trim.fq SRR1002940.r1.unpair.fq SRR1002940.r2.trim.fq SRR1002940.r2.unpair.fq ILLUMINACLIP:/BiO/Install/Trimmomatic-0.38/adapters/TruSeq3-PE-2.fa:2:151:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36

#4.Reference mapping(re-sequencing) make sam file.
bwa mem -t4 -R '@RG\tPL:illumina\tID:JBK\tSM:SRR1002940\tLB:HiSeq' /BiO/Education/WGS/REF/hg19.fa SRR1002940.r1.trim.fq SRR1002940.r2.trim.fq > SRR1002940.sam

#5.PICARD - Mark Duplicates
        #5-1 Duplication tagging
mkdir TEMP_PICARD  # Make TEMP Forder for PICARD 

java -jar /BiO/Install/picard-tools-2.22.3/picard.jar AddOrReplaceReadGroups TMP_DIR=TEMP_PICARD VALIDATION_STRINGENCY=LENIENT SO=coordinate I=SRR1002940.sam O=SRR10002940_sorted.bam RGID=SRR1002940 RGLB=HiSeq RGPL=Illumina RGPU=unit1 RGSM=SRR1002940 CREATE_INDEX=true

        #5-2 Remove duplicates
java -jar /BiO/Install/picard-tools-2.22.3/picard.jar MarkDuplicates TMP_DIR=tEMP_PICARD VALIDATION_STRINGENCY=LENIENT I=SRR1002940_sorted.bam O=SRR1002940.dedup.sam M=SRR1002940.duplicate_metrics REMOVE_DUPLICATE=true AS=true

        #5-3 Sorting
java -jar /BiO/Install/picard-tools-2.22.3/picard.jar SortSam TMP_DIR=TEMP_PICARD VALIDATION_STRINGENCY=LENIENT SO=coordinatie I=SRR1002940_dedup.sam O=SRR1002940_dedup.bam CREATE_INDEX=true
