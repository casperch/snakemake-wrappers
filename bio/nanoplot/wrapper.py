"""Snakemake wrapper for NanoPlot"""

__author__ = "Jae-Pil Choi"
__copyright__ = "Copyright 2020, Jae-Pil Choi"
__email__ = "casperch@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell
from os import path

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

fastq = ""
if snakemake.input.get('fastq', ''):
    fastq = "--fastq {}".format(snakemake.input.fastq)
                        
fasta = ""
if snakemake.input.get('fasta', ''):
    fasta = "--fasta {}".format(snakemake.input.fasta)

assert fastq == "" or fasta == "", "please input a fastq or fasta"

outdir = path.dirname(snakemake.output[0])

shell(
    "NanoPlot "
    "--threads {snakemake.threads} "
    "{fasta} "
    "{fastq} "
    "--outdir {outdir} "
    "{extra} "
    "{log}"
)
