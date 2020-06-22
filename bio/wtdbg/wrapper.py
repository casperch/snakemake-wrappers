"""Snakemake wrapper for Wtdbg2"""

__author__ = "Jae-Pil Choi"
__copyright__ = "Copyright 2020, Jae-Pil Choi"
__email__ = "casperch@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell
from os import path

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")

preset = snakemake.params.get("preset", None)
genome_size = snakemake.params.get("genome_size")
assert genome_size is not None, "genome_size require"

prefix = snakemake.output[0].split('.')[0]

if preset:
    param_preset = "-x " + preset

shell(    
    "(wtdbg2 {param_preset} -g {genome_size} -t {snakemake.threads} -i {snakemake.input} -o {prefix};"
    "wtpoa-cns -t {snakemake.threads} -i {prefix}.ctg.lay.gz -o {snakemake.output}) {log}" 
)

