__author__ = "Jae-Pil Choi"
__copyright__ = "Copyright 2020, Jae-Pil Choi"
__email__ = "casperch@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell
import os

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

merlen = snakemake.params.get("merlen", 21)
hashsize = snakemake.params.get("hashsize", "100M")

inputExt = os.path.splitext(snakemake.input[0])[1]


if inputExt == ".gz":
    shell(
        "zcat {snakemake.input} | jellyfish count -C -m {merlen} -s {hashsize} -t {snakemake.threads} -o reads.jf /dev/fd/0 {log}"
    )
else:
    shell(
        "jellyfish count -C -m {merlen} -s {hashsize} -t {snakemake.threads} {snakemake.input} -o reads.jf {log}"
    )

shell("jellyfish histo -t {snakemake.threads} reads.jf > {snakemake.output} {log}")
