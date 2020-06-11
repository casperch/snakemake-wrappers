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


# Sample_1	Sample_1	CBM0134	CBM0134
# Sample_11	Sample_11	CBM034-2	CBM034-2
# Sample_4	Sample_4	CBM0144	CBM0144
# Sample_5	Sample_5	CBM0103	CBM0103
# Sample_6	Sample_6	CBM0110	CBM0110
# Sample_7	Sample_7	CBM0111	CBM0111
# Sample_8	Sample_8	CBM0221	CBM0221
# Sample_9	Sample_9	CBM0115	CBM0115
# Sample_10	Sample_10	CBM0128	CBM0128
# Sample_12	Sample_12	CBM0171	CBM0171
# Sample_13	Sample_13	CBM0108	CBM0108
# Sample_2	Sample_2	CBM0212	CBM0212
# Sample_14	Sample_14	CBM0212-2	CBM0212-2
# Sample_15	Sample_15	CBM0212-3	CBM0212-3
# Sample_16	Sample_16	CBM116	CBM116
# Sample_17	Sample_17	CBM116-2	CBM116-2
