import json
import ngram

with open('teachers.json', 'r') as f:
    teachers_dict = json.load(f)

with open('blocks.json', 'r') as f:
    blocks_dict = json.load(f)

with open('bundles.json', 'r') as f:
    bundles_dict = json.load(f)

def search_by_teacher(search_string):
    teacher_search = ngram.NGram(teachers_dict)
    return teachers_dict[teacher_search.find(search_string.lower())]

def search_by_bundle(search_string):
    bundle_search = ngram.NGram(bundles_dict)
    return bundles_dict[bundle_search.find(search_string.lower())]

def search_by_block(search_string):
    block_search = ngram.NGram(blocks_dict)
    return blocks_dict[block_search.find(search_string.lower())]
