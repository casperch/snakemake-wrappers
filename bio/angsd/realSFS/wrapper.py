__author__ = "Jae-Pil Choi"
__copyright__ = "Copyright 2020, Jae-Pil Choi"
__email__ = "casperch@gmail.com"
__license__ = "MIT"


import os
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)

shell(
    "realSFS "
    "{snakemake.input.idx1} {snakemake.input.idx2} "
    "{extra} > {snakemake.output}"
    "{log}"
)
