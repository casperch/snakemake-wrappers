__author__ = "Jae-Pil Choi"
__copyright__ = "Copyright 2020, Jae-Pil Choi"
__email__ = "casperch@gmail.com"
__license__ = "MIT"


from snakemake.shell import shell

## Extract arguments
outdir = snakemake.output[0] if snakemake.output[0] else 'result'
extra = snakemake.params.get("extra", "")

shell("mapDamage " " {extra}" " -i {snakemake.input.bam} -r {snakemake.input.ref} -d {outdir}")
