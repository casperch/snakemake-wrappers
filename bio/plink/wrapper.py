__author__ = "Jae-Pil Choi"
__copyright__ = "Copyright 2020, Jae-Pil Choi"
__email__ = "casperch@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
import os

input_flag = "--file"
if snakemake.input[0].endswith(".bed"):
    input_flag = "--bfile"

input_file = os.path.splitext(snakemake.input[0])[0]

output = os.path.splitext(snakemake.output[0])[0]

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell("plink {snakemake.params} {input_flag} {input_file} --out {output} {log}")
