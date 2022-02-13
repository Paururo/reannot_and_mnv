#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import os

PATH_SNPEFF = '/storage/PGO/soft/snpEff/'

def read_gnumbers(in_file: str):
    '''
    Function to read gnums to process
    '''
    list_gnums = []
    with open(in_file,'r') as i_input:
        for line in i_input:
            line = line.strip('\n')
            list_gnums.append(line)
    return list_gnums

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
                    if "#" not in line:
                        l = line.strip("\n").split("\t")
                        inf_l = ';'.join(l[7].split('|')[0].split(";")[0:5])
                        line = 'MTB_anc\t' + l[1] + '\t.\t' + l[3] + '\t' + l[4] + '\tPASS\t' + inf_l +'\t\t'+l[8] +'\t\t' +l[9] + '\n'
                outvcf.write(line)
def main():
    '''
    Function to execute all code
    '''
    parser = argparse.ArgumentParser(description = 'script to reannotate and put MNVs')
    parser.add_argument('-p', dest = 'path', required =True, help = 'Path to vcf files')
    parser.add_argument('-g', dest = 'gnums', required = True, help = 'File with gnumbers')
    args = parser.parse_args()
    l_gnums = read_gnumbers(args.gnums)
    for gnumber in l_gnums:
        generate_path = args.path + gnumber[0:3] + '/' + gnumber[3:5] + '/' + gnumber[5] + '/' + gnumber
        
        try:
            read_lines(generate_path + '.var.snp.vcf', generate_path + '.intermediate.file')
            os.system('java -jar ' + PATH_SNPEFF +'snpEff.jar ann -noStats -no-downstream -no-upstream MTB_ANC -interval ' + PATH_SNPEFF +'additionnal_annotations.bed ' + generate_path + '.intermediate.file > '+ generate_path +'.re.var.snp.vcf')
            os.system('rm '+ generate_path + '.intermediate.file')
            os.system('perl -pi -e "s/\tANN/;ANN/g" '+ generate_path+'.re.var.snp.vcf')
            os.system('perl -pi -e "s/\t0.0\t/\t.\tPASS\t/g" '+ generate_path+'.re.var.snp.vcf')
            print('Processing', gnumber)
            os.system('python3 get_mnv.py -f MTB_ancestor.fas -g anot_genes.3.txt -v ' + generate_path + '.re.var.snp.vcf')
        
        except:
            print('Gnumber not working', gnumber)

if __name__ == '__main__':
    main()