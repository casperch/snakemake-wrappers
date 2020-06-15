__author__ = "Jae-Pil Choi"
__copyright__ = "Copyright 2020, Jae-Pil Choi"
__email__ = "casperch@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
import os

input_flag = "--vcf"
if snakemake.input[0].endswith(".gz"):
    input_flag = "--gzvcf"

output = os.path.splitext(snakemake.output[0])[0]

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

extra = snakemake.params.get("extra", "")

shell(
    "vcftools "
    "{input_flag} "
    "{snakemake.input} "
    "{extra} "
    "--plink "
    "--out {output} "
    "{log}"
)
