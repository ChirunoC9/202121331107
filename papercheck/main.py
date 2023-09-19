import sys

import src.papercheck as check

def main():
    if len(sys.argv) != 4:
        print("Usage: python ./main.py original_article_file_path plagiarized_article_file_path answer_file_path")
        return
    
    original_article_file_path, plagiarized_article_file_path, answer_file_path = sys.argv[1], sys.argv[2], sys.argv[3]
    
    try:
        ans = check.calc_similarity_between_two_file(original_article_file_path, plagiarized_article_file_path)
        with open(answer_file_path, 'w', encoding='utf-8') as ans_ouput_file:
            ans_ouput_file.write(f"Answer: {ans:.2f}%")
        print(f"Answer: {ans:.2f}%")
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == '__main__':
    import tests.test
    tests.test.test_check()
    # if (len(sys.argv) == 2):
    #     if sys.argv[1] == 'test':
    #         import tests.test
    #         tests.test.test_check()
    #     else:
    #         print("Usage: python ./main.py test")
    # else:
    #     main()