#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import sys

PATH_SNPEFF = '/storage/PGO/soft/snpEff/'
SNP_EFFCOMMAND = 'java -jar /home/ruizro/snpEff/snpEff.jar ann -noStats -no-downstream -no-upstream MTB_ANC " + salida_intermedia + " > " + salida_anotada'


def read_lines(in_file: str, out_file:str):
    '''
    Function to generate intermediate file for annotate the snps of vcf file
    '''
    with open(out_file,'w') as outvcf:
        with open(in_file,'r') as inputvcf:
            for line in inputvcf:
                if 'coord' in line:
                    line = '#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n'
                    
                else:
                    l = line.strip("\n").split("\t")
                    
                    line = 'MTB_anc\t' + l[0]+'\t.\t'+l[1]+'\t'+l[2]+'\tPASS\t'+' '.join(l[3:])+'\n'
                outvcf.write(line) 

def main():
    '''
    Function to execute all code
    '''

if __name__ == '__main__':
    main()