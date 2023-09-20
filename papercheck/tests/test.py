import os, sys

import src.papercheck as check

# from main import check

def test_check():
    original_article_file_path, plagiarized_article_file_path, answer_file_path = './tests/origin.txt', './tests/plag.txt', './tests/answer.txt'
        
    try:
        ans = check.calc_similarity_between_two_file(original_article_file_path, plagiarized_article_file_path)
        ans *= 100
        with open(answer_file_path, 'w', encoding='utf-8') as ans_ouput_file:
            ans_ouput_file.write(f"Answer: {ans:.2f}%")
        print(f"Answer: {ans:.2f}%")
    except Exception as e:
        print(f"Error: {e}")    

if __name__ == '__main__':
    # sys.path.append('..')
    test_check()

    # pass