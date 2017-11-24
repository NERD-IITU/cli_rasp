import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sql_decl import Bundle, Block, Subject, Teacher, Timetable, Base, Week, Time

engine = create_engine('sqlite:///schedule.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

days = {1: "Monday",
      2: "Tuesday",
      3: "Wednesday",
      4: "Thursday",
      5: "Friday",
      6: "Saturday",
      7: "Sunday"}

for day in days:
    new_day = Week(id=day, name=days[day])
    try:
        session.add(new_day)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()



list_of_empty_blocks = []
for file in range(13765,14245):
    loaded_json = {}
    with open(f"data/{file}.json", "br") as innerfile:
        loaded_json = json.loads(innerfile.read().decode("utf-8"))
    if not loaded_json["timetable"]:
        print(f"data/{file}.json is empty. I\'m passing!")
        list_of_empty_blocks.append(file)
        continue

    for another_bundle in loaded_json['bundles']:
        for bun in loaded_json['bundles'][another_bundle]:
            if bun == '0':
                print('bundle: '+another_bundle)
                new_bundle = Bundle(id=int(another_bundle), name=loaded_json['bundles'][another_bundle]['0']['name_en'])
                try:
                    session.add(new_bundle)
                    session.commit()
                    print("SUCCESS on bundle")
                except Exception as e:
                    print(e)
                    session.rollback()

            elif bun == 'name':
                bundle_name = ""
                print("bundle: "+another_bundle)
                for innername in loaded_json['bundles'][another_bundle]['name']:
                    bundle_name+=innername['name_en']+" "

                new_bundle = Bundle(id=int(another_bundle), name=bundle_name)
                try:
                    session.add(new_bundle)
                    session.commit()
                    print("SUCCESS on bundle")
                except Exception as e:
                    print(e)
                    session.rollback()

    for another_block in loaded_json['blocks']:
        new_block = Block(id=int(another_block), name=loaded_json['blocks'][another_block]['name'])
        print("block: "+another_block)
        try:
            session.add(new_block)
            session.commit()
            print("SUCCESS on block")
        except Exception as ex:
            print(ex)
            session.rollback()

    for another_subject in loaded_json['subjects']:
        new_subject = Subject(id=int(another_subject), name=loaded_json['subjects'][another_subject]['subject_en'])
        print("subject: "+another_subject)
        try:
            session.add(new_subject)
            session.commit()
            print("SUCCESS on subject")
        except Exception as ex:
            print(ex)
            session.rollback()

    for another_teacher in loaded_json['teachers']:
        new_teacher = Teacher(id=int(another_teacher), name=loaded_json['teachers'][another_teacher]['teacher_en'])
        print("teacher: "+another_teacher)
        try:
            session.add(new_teacher)
            session.commit()
            print("SUCCESS on teacher")
        except Exception as e:
            print(e)
            session.rollback()

    for another_time in loaded_json['times']:
        new_time = Time(id=int(another_time),
                        start_time=loaded_json['times'][another_time]['start_time'],
                        end_time=loaded_json['times'][another_time]['end_time'])
        print("time: "+another_time)
        try:
            session.add(new_time)
            session.commit()
            print("SUCCESS on time")
        except Exception as e:
            print(e)
            session.rollback()

for file in range(13765,14245):
    loaded_json = {}
    if file not in list_of_empty_blocks:
        with open(f"data/{file}.json", "br") as innerfile:
            loaded_json = json.loads(innerfile.read().decode("utf-8"))
        for day in loaded_json['timetable']:
            for liltime in loaded_json['timetable'][day]:
                timetable_id = loaded_json['timetable'][day][liltime][0]['id']
                subject_id = loaded_json['timetable'][day][liltime][0]['subject_id']
                block_id = loaded_json['timetable'][day][liltime][0]['block_id']
                teacher_id = loaded_json['timetable'][day][liltime][0]['teacher_id']
                bundle_id = loaded_json['timetable'][day][liltime][0]['bundle_id']
                week_id = loaded_json['timetable'][day][liltime][0]['day_id']
                time_id = loaded_json['timetable'][day][liltime][0]['time_id']

                new_timetable = Timetable(id=int(timetable_id),
                                          weekid=int(week_id),
                                          blockid=int(block_id),
                                          bundleid=int(bundle_id),
                                          teacherid=int(teacher_id),
                                          subjectid=int(subject_id),
                                          timeid=int(time_id)
                                          )
                try:
                    session.add(new_timetable)
                    session.commit()
                    print("SUCCESS on timetable")
                except Exception as e:
                    print(e)
                    print("TIMETABLE ERROR")
                    session.rollback()
    else:
        continue

# At least somewhere it needs to be closed!
session.close()

