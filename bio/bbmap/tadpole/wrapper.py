__author__ = "Jae-Pil Choi"
__copyright__ = "Copyright 2020, Jae-Pil Choi"
__email__ = "casperch@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
mode = snakemake.params.get("mode", "contig-building") # correct

shell(
    "(tadpole.sh "
    "in1={snakemake.input.r1} in2={snakemake.input.r2} "
    "out1={snakemake.output.r1} out2={snakemake.output.r2} "
    "mode={mode} "
    "{extra}) {log}"
)
