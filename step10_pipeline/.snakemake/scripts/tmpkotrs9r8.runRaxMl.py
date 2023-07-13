
######## snakemake preamble start (automatically inserted, do not edit) ########
import sys; sys.path.extend(['/Users/wanlin/opt/anaconda3/lib/python3.8/site-packages', '/Users/wanlin/Documents/GitHub/bat_coronavirus/step10_pipeline/scripts']); import pickle; snakemake = pickle.loads(b"\x80\x04\x95\xd0\x05\x00\x00\x00\x00\x00\x00\x8c\x10snakemake.script\x94\x8c\tSnakemake\x94\x93\x94)\x81\x94}\x94(\x8c\x05input\x94\x8c\x0csnakemake.io\x94\x8c\nInputFiles\x94\x93\x94)\x81\x94\x8c,results/windows/window_position_3920_4020.fa\x94a}\x94(\x8c\x06_names\x94}\x94\x8c\x12_allowed_overrides\x94]\x94(\x8c\x05index\x94\x8c\x04sort\x94eh\x10\x8c\tfunctools\x94\x8c\x07partial\x94\x93\x94h\x06\x8c\x19Namedlist._used_attribute\x94\x93\x94\x85\x94R\x94(h\x16)}\x94\x8c\x05_name\x94h\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bub\x8c\x06output\x94h\x06\x8c\x0bOutputFiles\x94\x93\x94)\x81\x94(\x8c'results/RAxML/3920_4020.raxml.bestModel\x94\x8c&results/RAxML/3920_4020.raxml.bestTree\x94\x8c(results/RAxML/3920_4020.raxml.bootstraps\x94\x8c!results/RAxML/3920_4020.raxml.log\x94\x8c%results/RAxML/3920_4020.raxml.mlTrees\x94\x8c!results/RAxML/3920_4020.raxml.rba\x94\x8c'results/RAxML/3920_4020.raxml.startTree\x94\x8c%results/RAxML/3920_4020.raxml.support\x94e}\x94(h\x0c}\x94h\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bub\x8c\x06params\x94h\x06\x8c\x06Params\x94\x93\x94)\x81\x94}\x94(h\x0c}\x94h\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bub\x8c\twildcards\x94h\x06\x8c\tWildcards\x94\x93\x94)\x81\x94\x8c\t3920_4020\x94a}\x94(h\x0c}\x94\x8c\x08position\x94K\x00N\x86\x94sh\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94b\x8c\x08position\x94hJub\x8c\x07threads\x94K\x01\x8c\tresources\x94h\x06\x8c\tResources\x94\x93\x94)\x81\x94(K\x01K\x01\x8c0/var/folders/jm/5k15km0505vdkj2xt4zkphy40000gn/T\x94e}\x94(h\x0c}\x94(\x8c\x06_cores\x94K\x00N\x86\x94\x8c\x06_nodes\x94K\x01N\x86\x94\x8c\x06tmpdir\x94K\x02N\x86\x94uh\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bhaK\x01hcK\x01heh^ub\x8c\x03log\x94h\x06\x8c\x03Log\x94\x93\x94)\x81\x94}\x94(h\x0c}\x94h\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bub\x8c\x06config\x94}\x94\x8c\x06params\x94}\x94(\x8c\tstep_size\x94K\n\x8c\x0bwindow_size\x94Kd\x8c\x08seq_file\x94\x8c\x1fconfig/1aln_orf1ab_withID.fasta\x94us\x8c\x04rule\x94\x8c\x08runRaxML\x94\x8c\x0fbench_iteration\x94N\x8c\tscriptdir\x94\x8cF/Users/wanlin/Documents/GitHub/bat_coronavirus/step10_pipeline/scripts\x94ub."); from snakemake.logging import logger; logger.printshellcmds = False; __real_file__ = __file__; __file__ = '/Users/wanlin/Documents/GitHub/bat_coronavirus/step10_pipeline/scripts/runRaxMl.py';
######## snakemake preamble end #########
import os


def runRaxMl(inputfile, prefix):
    # our data type is protein

    os.system("raxml-ng --all --model Blosum62+G --msa " + inputfile + " --prefix results/RaxMl/" + prefix +
              " --msa-format FASTA --tree pars{5} --seed 239 --threads 2 --force --bs-trees 100 --bs-metric fbp")


if __name__ == '__main__':
    runRaxMl(
        snakemake.input[0],
        snakemake.wildcards.position
    )
