from os import walk, makedirs
from os.path import join, isdir, abspath, split, exists
from shutil import move, copy, rmtree
from converters import g2p, g2sc
from tqdm import tqdm

# Script converts verbatim text to the given transcription and saves the files in a separate folder
def convert_simple(transcription_system='dolgo'):
    if transcription_system == 'original':
        exit('Original would overwrite the verbatim corpus. Aborting.')

    verbatim_directory = "./corpus/original" # Corpus directory with verbatim samples in PAN format
    verbatim_directory = abspath(verbatim_directory)
    dest_directory = join(split(verbatim_directory)[0], transcription_system)

    if exists(dest_directory):
        rmtree(dest_directory)
        print('Removed existing directory: ' + dest_directory)
    makedirs(dest_directory)
    print('Created directory: ' + dest_directory)


    all_child_directories = next(walk(verbatim_directory))[1]
    for child_dir in tqdm(all_child_directories):
        verbatim_pair_directory = join(verbatim_directory, child_dir)
        dest_pair_directory = join(dest_directory, child_dir)
        makedirs(dest_pair_directory)

        with open(join(verbatim_pair_directory, 'known01.txt'), 'r') as input_verbatim,\
            open(join(dest_pair_directory, 'known01.txt'), 'w') as output_verbatim,\
            open(join(verbatim_pair_directory, 'unknown.txt'), 'r') as input_transcription,\
            open(join(dest_pair_directory, 'unknown.txt'), 'w') as output_transcription:
            output_verbatim.write(g2sc(input_verbatim.read(), transcription_system))
            output_transcription.write(g2sc(input_transcription.read(), transcription_system))

def convert_splits(transcription_system='dolgo'):
    pass