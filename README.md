# cli_rasp

Have no total idea how to write README-s.
So, that's going to be first README.
*Note: Python3 required*

Firstly, you need to install reqs.txt
`pip3 install -r reqs.txt` //it needs to be revised in env

Then,you go with launching jsonfetcher.py. It does fetch all json's from schedule.iitu.kz
`python3 jsonfetcher.py`

(You'd better not to do that thing inside of IITU using their WI-Fi, bad practice)

Thirdly, you launch `sql_decl.py`"
`python3 sql_decl.py`

Forthly, you launch `sql_insert.py`:
`python3 sql_insert.py`

Those last two create from `data/\*.json` pretty normal SQLite3-compatible db.

Fifthly you need to launch:
`python3 meta_json_creator.py`

That script creates meta_json_files with which you can search without requesting to the db

After that u launch `main.py` with needed arguments. But you'd better check it with:
`python3 main.py --help`

for example:
```
$ python main.py -g cs1601
 ___________________________________________________________
                    GROUP NAME : CS-1601K
 ___________________________________________________________
 MONDAY
 Theory of datab..| Olzhaev Olzhas   | 13:10 | 14:00 | 902 |
 ААнглийский язык  | каф Яз англ      | 14:10 | 15:00 | 305 |
 ААнглийский язык  | каф Яз англ      | 15:10 | 16:00 | 305 |
 Physical Cultur..| (пусто)          | 16:10 | 17:00 | FK  |
 Physical Cultur..| (пусто)          | 17:20 | 18:10 | FK  |
 ___________________________________________________________
 TUESDAY
 Philosophy       | Doskozhanova Ai..| 13:10 | 14:00 | 608 |
 Theory of datab..| Olzhaev Olzhas   | 14:10 | 15:00 | 402 |
 Theory of datab..| Olzhaev Olzhas   | 15:10 | 16:00 | 402 |
 Discrete Mathem..| Nurtas Marat     | 16:10 | 17:00 | 608 |
 Discrete Mathem..| Nurtas Marat     | 17:20 | 18:10 | 608 |
 Discrete Mathem..| Nurtas Marat     | 18:30 | 19:20 | 801 |
 ___________________________________________________________
 WEDNESDAY
 Algorithms, dat..| Makhanov Nursul..| 11:00 | 11:50 | 604 |
 Algorithms, dat..| Makhanov Nursul..| 12:10 | 13:00 | 604 |
 Algorithms, dat..| Makhanov Nursul..| 13:10 | 14:00 | 801 |
 Theory of datab..| Olzhaev Olzhas   | 14:10 | 15:00 | 407 |
 ___________________________________________________________
 THURSDAY
 Operation syste..| Баекеева ААсель   | 13:10 | 14:00 | 700 |
 Казахский язык   | каф Яз каз       | 14:10 | 15:00 | 707 |
 Казахский язык   | каф Яз каз       | 15:10 | 16:00 | 707 |
 ААнглийский язык  | каф Яз англ      | 16:10 | 17:00 | 305 |
 ___________________________________________________________
 FRIDAY
 Algorithms, dat..| Makhanov Nursul..| 13:10 | 14:00 | 902 |
 Philosophy       | Doskozhanova Ai..| 14:10 | 15:00 | 902 |
 Philosophy       | Doskozhanova Ai..| 15:10 | 16:00 | 902 |
 Operation syste..| Баекеева ААсель   | 16:10 | 17:00 | 407 |
 Operation syste..| Баекеева ААсель   | 17:20 | 18:10 | 407 |
                                                              
```
