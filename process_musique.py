import os
import json
import jsonlines

paradigm = 'dev'
# ip_fname = 'musique_full_v1.0_{}.jsonl'.format(paradigm)
ip_fname = 'musique_ans_v1.0_{}.jsonl'.format(paradigm)
# op_fname = 'musique_{}.json'.format(paradigm)
op_fname = 'musique_ans_{}.json'.format(paradigm)

if os.path.exists(op_fname):
	os.remove(op_fname)

drop_dict = {}
drop_dict_json = {}
with jsonlines.open(ip_fname) as f:
	for line in f.iter():
		# print(line.keys())
		drop_dict[line['id']] = {}
		drop_dict[line['id']]['passage'] = ' '.join([pg['paragraph_text'] for pg in line['paragraphs']])
		drop_dict[line['id']]['qa_pairs'] = [{'question': line['question'], "answer": {"number": "", "date": { "day": "", "month": "", "year": ""}, "spans": [line['answer']]}, 'query_id': '', 'validated_answers': [{"number": "", "date": { "day": "", "month": "", "year": ""}, "spans": [line['answer']]}]}]
		drop_dict[line['id']]["wiki_url"] = "https://en.wikipedia.org/wiki/Earl's_Court"
		
drop_dict_json = json.dumps(drop_dict)
with open(op_fname, "a") as outfile:
	outfile.write(drop_dict_json)
	# outfile.write(',\n')
