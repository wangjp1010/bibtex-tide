from pybtex.database.input import bibtex
import re
from RULES import rules, keep_keys

def key_filter(bib_file_path:str):
    '''
    Only retain specific keys from the reference dict
    Args:
        bib_file_path: path to the original bib file
        keep_keys: keys to keep, defined in RULES.py
    '''
    parser = bibtex.Parser()
    bib_data = parser.parse_file(bib_file_path)

    # 遍历每个参考文献条目
    for entry_key, entry in bib_data.entries.items():
        # 遍历每个字段，删除不在保留列表中的字段
        fields_to_delete = []
        for field in entry.fields:
            if field not in keep_keys:
                fields_to_delete.append(field)

        # 删除不在保留列表中的字段
        for field in fields_to_delete:
            del entry.fields[field]

    with open(bib_file_path, 'w', encoding='utf-8') as bibfile:
        bibfile.write(bib_data.to_string('bibtex'))


def unify_arxiv_format_(bib_file_path:str):
    '''
    Unify the format of arxiv entries.Translate CoRR to arXiv preprint arXiv:.
    Args:
        bib_file_path: path to the original bib file
    '''
    parser = bibtex.Parser()
    bib_data = parser.parse_file(bib_file_path)

    # 遍历每个参考文献条目
    for entry_key, entry in bib_data.entries.items():
        if 'journal' in entry.fields:
            # TODO: 有些CoRR的文章没有volume字段,print出来
            if entry.fields['journal'] == 'CoRR':
                try:
                    volume = entry.fields['volume']
                    volume = volume[volume.find('/') + 1:]
                    entry.fields['journal'] = 'arXiv preprint arXiv:' + volume
                    del entry.fields['volume']
                except KeyError:
                    print(entry_key + ' :CoRR without volume')

    # for entry_key, entry in bib_data.entries.items():
    #     if 'journal' in entry.fields:
    #         print(entry.fields['journal'])

    with open(bib_file_path, 'w', encoding='utf-8') as bibfile:
        bibfile.write(bib_data.to_string('bibtex'))


    
def abbreviate_conference(bib_file_path: str):
    '''
    Abbreviate the conference names in the bib file.
    Args:
        file_path: path to the original bib file
        rules: regex rules to abbreviate the conference names, defined in RULES.py
    '''
    parser = bibtex.Parser()
    bib_data = parser.parse_file(bib_file_path)

    # 遍历每个参考文献条目
    for entry_key, entry in bib_data.entries.items():
        if 'booktitle' in entry.fields:
            for abbreviation, name_patterns in rules.items():
                for name_pattern in name_patterns:
                    entry.fields['booktitle'] = re.sub(name_pattern, abbreviation, entry.fields['booktitle'])

    with open(bib_file_path, 'w', encoding='utf-8') as bibfile:
        bibfile.write(bib_data.to_string('bibtex'))



if __name__ == '__main__':
    file_path = 'test.bib'
    key_filter(file_path)
    unify_arxiv_format_(file_path)
    abbreviate_conference(file_path)