"""Snakemake wrapper for Racon Consensus module for raw de novo DNA assembly of long uncorrected reads."""

__author__ = "Jae-Pil Choi"
__copyright__ = "Copyright 2020, Jae-Pil choi"
__email__ = "casperch@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell
from os import path

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
extra = snakemake.params.get("extra", "")
match = snakemake.params.get("match", 8)
missmatch = snakemake.params.get("missmatch", -6)
gap = snakemake.params.get("gap", -8)
window_length = snakemake.params.get("window_length", -8)

shell(
    "racon -t {snakemake.threads} "
    " -m {match} "
    " -x {missmatch} "
    " -g {gap} "
    " -w {window_length} "
    " {extra} "
    "{snakemake.input.sequences} {snakemake.input.overlaps} {snakemake.input.target_sequences} > {snakemake.output} {log}"
)
