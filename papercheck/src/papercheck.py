
import os, sys

from simhash import Simhash

import src.utils.preprocess as string_preprocess


def calc_similarity_between_two_words_list(words_list1 : list, words_list2 : list, f : int = 64) -> float:
    """
    Calculate similarity between words_list1 and words_list2
    
    `f` is the dimensions of fingerprints, in bits. Must be a multiple of 8.
    """
    list1_simhash = Simhash(words_list1, f)
    list2_simhash = Simhash(words_list2, f)
    return (f - list1_simhash.distance(list2_simhash)) / f


def calc_similarity_between_two_str(str1 : str, str2 : str, f : int = 64) -> float:
    """
    Calculate the similarity of two strings
    
    `f` is the dimensions of fingerprints, in bits. Must be a multiple of 8.
    """
    paper1_notext_str = string_preprocess.drop_nontext_parts(str1)
    paper2_notext_str = string_preprocess.drop_nontext_parts(str2)
    words_list1 = string_preprocess.get_words_lcut_list(paper1_notext_str)
    words_list2 = string_preprocess.get_words_lcut_list(paper2_notext_str)
    return calc_similarity_between_two_words_list(words_list1, words_list2, f=f)


def calc_similarity_between_two_file(file_path1 : str, file_path2 : str, f : int = 64) -> float:
    """
    Calculate the similarity of two file

    `f` is the dimensions of fingerprints, in bits. Must be a multiple of 8.
    """
    if not os.path.isfile(file_path1):
        raise Exception(f"{file_path1} is not a file.")
    if not os.access(file_path1, os.R_OK):
        raise Exception(f"{file_path1} can not be read.")

    if not os.path.isfile(file_path2):
        raise Exception(f"{file_path2} is not a file.")
    if not os.access(file_path2, os.R_OK):
        raise Exception(f"{file_path2} can not be read.")

    with open(file_path1, 'r', encoding='utf-8') as input_file:
        text1 = input_file.read();
    with open(file_path2, 'r', encoding='utf-8') as input_file:
        text2 = input_file.read();
            
    return calc_similarity_between_two_str(text1, text2, f=f)

if __name__ == '__main__':
    print(calc_similarity_between_two_str('`f` is the dimensions of fingerprints, in bits. Must be a multiple of 8.', '`f` is of fingerprints, in bits. Must be a multiple of 8.'))
    pass 