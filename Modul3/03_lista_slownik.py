workers = [
    {'id': 1, 'job_title': 'junior developer', 'name': 'John', 'programming_language': ['python']},
    {'id': 2, 'job_title': 'senior developer', 'name': 'Mark', 'programming_language': ['python','php']},
    {'id': 3, 'job_title': 'stuff developer', 'name': 'Alex', 'programming_language': ['php', 'javascript', 'python']},
    {'id': 4, 'job_title': 'junior developer', 'name': 'Bart', 'programming_language': ['php', 'javascript']},
    {'id': 5, 'job_title': 'senior developer', 'name': 'Carl', 'programming_language': ['python', 'javascript']},
    {'id': 6, 'job_title': 'senior developer', 'name': 'Martha', 'programming_language': ['php', 'javascript']}
]

prog_langs = dict()

for worker in workers:
    for i in worker.get('programming_language'):
        if prog_langs.get(i) is None:
            prog_langs[i] = {'quantity': 0, 'names': []}

        prog_langs[i]['quantity'] += 1
        prog_langs[i]['names'].append(worker.get('name'))

print(prog_langs)
