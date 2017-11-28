from search import  search_by_block as s_block
from search import  search_by_teacher as s_teacher

# Those are the libraries that are going to be used
# *further
# import clr
# from sql_decl import  Base #,Timetable, Block, Bundle, Time, Week, Teacher, Subject
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm import relationship

from sqlalchemy import create_engine
import argparse

engine = create_engine('sqlite:///schedule.db')
connection = engine.connect()


# *further
# Base.metadata.bind = engine
# DBSession = sessionmaker()
# DBSession.bind = engine
# session = DBSession()

class Display:
    def string_formatter(self, string, variable_type, query_type):
        if query_type is "block":
            if variable_type is "bundle":
                return (string+"  ")[:3] + " |"
            elif variable_type is "time":
                return string[:5] + " |"
            else:
                if len(string) > 15:
                    string = string + "           "
                    string = string[:15]
                    return string + "..|"
                else:
                    string = string + "           "
                    string = string[:15]
                    string = string + "  |"
        elif query_type is "bundle":
            if variable_type is "time":
                return string[:5] + " |"
            else:
                if len(string) > 15:
                    string = string + "           "
                    string = string[:15]
                    return string + "..|"
                else:
                    string = string + "           "
                    string = string[:15]
                    string = string + "  |"

        elif query_type is "teacher":
            if variable_type is "bundle":
                return (string + "  ")[:3] + " |"
            elif variable_type is "time":
                return string[:5] + " |"
            else:
                if len(string) > 15:
                    string = string + "           "
                    string = string[:15]
                    return string + "..|"
                else:
                    string = string + "           "
                    string = string[:15]
                    string = string + "  |"

        return string


class DisplayBlock(Display):
    def __init__(self, blockid):

        self.query_string = f"""
                      select blocks.name, bundles.name, subjects.name, teachers.name, times.start_time, times.end_time, week.name
                      from timetable join blocks  on timetable.belongsto=blocks.id join bundles on timetable.bundleid = bundles.id 
                      join subjects on  timetable.subjectid=subjects.id
                      join teachers on teachers.id=timetable.teacherid
                      join times on timetable.timeid=times.id
                      join week on timetable.weekid=week.id
                      where blocks.id={blockid}"""
        self.timetable_query = connection.execute(self.query_string)
        self.block_query = connection.execute(f"select blocks.name from blocks where blocks.id={blockid}")

    def show(self):
        string_formatter = Display.string_formatter
        last_dayname = "Monday"
        line = " ___________________________________________________________"
        print(line, end="")
        for i in self.block_query:
            print("\n\t\t    GROUP NAME : " + str(i)[2:-3].upper())
            break
        print(line, end="")
        print( "\n MONDAY")
        for blockname, bundlename, subjectname, teachername, timestart, timeend, dayname in self.timetable_query:
            subjectname = string_formatter(self,string=subjectname, variable_type="", query_type="block")
            teachername = string_formatter(self,string=teachername, variable_type="", query_type="block")
            timestart = string_formatter(self,string=timestart, variable_type="time", query_type="block")
            timeend = string_formatter(self,string=timeend, variable_type="time", query_type="block")
            bundlename = string_formatter(self,string=bundlename,variable_type="bundle",query_type="block")

            if last_dayname != dayname:

                print(line, end="")
                print(f"\n {dayname.upper()}")
            last_dayname = dayname

            print(f" {subjectname} {teachername} {timestart} {timeend} {bundlename}")


class DisplayTeacher(Display):
    def __init__(self, teacherid):
        self.teacherid = teacherid
        self.query_string = f"""select blocks.name, bundles.name, subjects.name, times.start_time, times.end_time, week.name
                                from timetable join blocks  on timetable.belongsto=blocks.id join bundles on timetable.bundleid = bundles.id 
                                join subjects on  timetable.subjectid=subjects.id
                                join teachers on teachers.id=timetable.teacherid
                                join times on timetable.timeid=times.id
                                join week on timetable.weekid=week.id
                                where teachers.id = {teacherid}
                                group by week.name, times.start_time, bundles.id
                                order by week.id, times.id
                             """
        self.timetable_query = connection.execute(self.query_string)
        self.teacher_query = connection.execute(f"select teachers.name from teachers WHERE teachers.id = {teacherid}")

    def show(self):
        string_formatter = Display.string_formatter
        last_dayname = "Monday"
        line = " __________________________________________________________"
        print(line, end="")
        for i in self.teacher_query:
            print("\n\t\t  TEACHER NAME : " + str(i)[2:-3].upper())
            break
        print(line, end="")
        print("\n MONDAY")
        for blockname, bundlename, subjectname, timestart, timeend, dayname in self.timetable_query:
            blockname = string_formatter(self, string=blockname, variable_type="", query_type="teacher")
            bundlename = string_formatter(self, string=bundlename, variable_type="bundle", query_type="teacher")
            subjectname = string_formatter(self, string=subjectname, variable_type="", query_type="teacher")
            timestart = string_formatter(self, string=timestart, variable_type="time", query_type="teacher")
            timeend = string_formatter(self, string=timeend, variable_type="time", query_type="teacher")

            if last_dayname != dayname:
                print(line, end="")
                print(f"\n {dayname.upper()}")
            last_dayname = dayname

            print(f" {blockname} {subjectname} {bundlename} {timestart} {timeend}")


class DisplayBundle(Display):
    def __init__(self, bundlename):
        self.bundlename = bundlename
        self.query_string = f"""select blocks.name, subjects.name, teachers.name, times.start_time, times.end_time, week.name
               from timetable join blocks  on timetable.belongsto=blocks.id join bundles on timetable.bundleid = bundles.id 
               join subjects on  timetable.subjectid=subjects.id
               join teachers on teachers.id=timetable.teacherid
               join times on timetable.timeid=times.id
               join week on timetable.weekid=week.id
               where bundles.name 	like "%{bundlename}%"
               group by week.name, times.start_time, bundles.id
               order by week.id, times.id"""
        self.timetable_query = connection.execute(self.query_string)

    def show(self):
        string_formatter = Display.string_formatter
        last_dayname = "Monday"
        line = " _______________________________________________________________________"
        print(line, end="")
        print("\n\t\t    ROOM NAME : " + self.bundlename.upper())
        print(line, end="")
        print("\n MONDAY")
        for blockname, subjectname, teachername, timestart, timeend, dayname in self.timetable_query:
            blockname = string_formatter(self, string=blockname, variable_type="", query_type="bundle")
            subjectname = string_formatter(self, string=subjectname, variable_type="", query_type="bundle")
            teachername = string_formatter(self, string=teachername, variable_type="", query_type="bundle")
            timestart = string_formatter(self, string=timestart, variable_type="time", query_type="bundle")
            timeend = string_formatter(self, string=timeend, variable_type="time", query_type="bundle")

            if last_dayname != dayname:
                print(line, end="")
                print(f"\n {dayname.upper()}")
            last_dayname = dayname

            print(f" {blockname} {subjectname} {teachername} {timestart} {timeend}")


parser = argparse.ArgumentParser(description="iitu.kz cli schedule displayer")
group = parser.add_mutually_exclusive_group()
group.add_argument("-g", "--group", action="store", help="group you want see")
group.add_argument("-t", "--teacher", action="store", help="teacher you want to see")
group.add_argument("-r", "--room", action="store", help="room you want to see")

args = parser.parse_args()

if args.group:
    new_block = DisplayBlock(s_block(args.group))
    new_block.show()
elif args.teacher:
    new_teacher = DisplayTeacher(s_teacher(args.teacher))
    new_teacher.show()
elif args.room:
    new_bundle = DisplayBundle(args.room)
    new_bundle.show()
else:
    print("MAAAAN!")