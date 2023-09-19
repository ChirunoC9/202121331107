import re

import jieba

def drop_nontext_parts(text : str) -> str:
    """Remove non-word characters from input string."""
    return re.sub('\W*', '', text)


def get_words_lcut_list(text : str) -> list:
    """Get text cut list use jieba."""
    result = jieba.lcut(text, cut_all=True)
    return result


if __name__ == '__main__':
    test_text = '123 . ..。。。。，。   ，；了；开始《》<>结束'
    result = drop_nontext_parts(test_text)
    print(result)