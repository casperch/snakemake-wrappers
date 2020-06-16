"""Snakemake wrapper for Racon Consensus module for raw de novo DNA assembly of long uncorrected reads."""

__author__ = "Jae-Pil Choi"
__copyright__ = "Copyright 2020, Jae-Pil choi"
__email__ = "casperch@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell
from os import path

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")
model = snakemake.params.get("model", "r941_min_high_g360")

shell(
    "medaka_consensus {extra} "
    " -i {snakemake.input.basecalls} "
    " -d {snakemake.input.draft_assembly} "
    " -o {snakemake.params.output_dir} "
    " -t {snakemake.threads} "
    " -m {model} {log}"
)
