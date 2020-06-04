__author__ = "Jae-Pil Choi"
__copyright__ = "Copyright 2020, Jae-Pil Choi"
__email__ = "casperch@gmail.com"
__license__ = "MIT"


import os
from snakemake.shell import shell

extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)


ancestral_genome = snakemake.params.get("anc")
if ancestral_genome:
    ref_cmd = "-anc " + ancestral_genome
else:
    ref_cmd = ""

dosaf = snakemake.params.get('dosaf')
if dosaf:
    dosaf_cmd = "-dosaf " + dosaf
else:
    dosaf_cmd = ""

gl = snakemake.params.get('gl')
if gl:
    gl_cmd = "-gl " + gl
else:
    gl_cmd = ""

outprefix = os.path.splitext(snakemake.output.arg)[0]

if snakemake.threads:
    thread_cmd = "-nThreads {}".format(snakemake.threads)
else:
    thread_cmd = ""

shell(
    "angsd "   
    "-b {snakemake.input.bamlist} "
    "-anc {snakemake.input.ancestral} "
    "-out {outprefix} "
    "-dosaf 1 "
    "{gl_cmd} "
    "{extra} "
    "{thread_cmd} "
    "{log}"
)
