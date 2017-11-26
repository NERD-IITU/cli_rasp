# cli_rasp

Have no total idea how to write README-s.
So, that's going to be first README.
*Note: Python3 required*

Firstly, you need to install reqs.txt
`pip3 install -r reqs.txt`

Then,you go with launching jsonfetcher.py. It does fetch all json's from schedule.iitu.kz
`python3 jsonfetcher.py`

(You'd better not to do that thing inside of IITU using their WI-Fi, bad practice)

Thirdly, you launch `sql_decl.py`
`python3 sql_decl.py`

Forthly, you launch `sql_insert.py`
`python3 sql_insert.py`

Those last two create from `data/\*.json` pretty normal SQLite3-compatible db.

Fifthly you need to launch `python3 meta_json_creator.py`

That script creates meta_json_files with which you can search without requesting to the db

That's what I've got for a while
