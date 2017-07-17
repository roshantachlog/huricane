import sqlite3

conn=sqlite3.connect("hurricane.db")
conn.execute('''CREATE TABLE SCHEDULER IF NOT EXIST (SNO INT PRIMARY KEY AUTOINCREMENT,
	                                    STRTIME TEXT,
	                                    ENDTIME TEXT,
	                                    DURATION TEXT,
	                                    NODE1 INT,
	                                    NODE2 INT,
	                                    NODE3 INT,
	                                    NODE4 INT,
	                                    STATUS TEXT 
	                                    RUNSTAT TEXT)''') # STATUS ON/OFF ,RUNSTAT ACTIVE/SLEEP
def Add_To_DB(self,S_no,Start_time,End_time,Durn,Node_1,Node_2,Node_3,Node_4,Stat):
	conn.execute(''' INSERT INTO SCHEDULER[(SNO,STRTIME,ENDTIME,DURATION,NODE1,NODE2,NODE3,NODE4,STATUS  )] VALUES (S_no,Start_time,End_time,Durn,Node_1,Node_2,Node_3,Node_4,Stat) ''')
def Get_MAX_Entry(self):
	return conn.execute('''SELECT MAX(SNO) FROM SCHEDULER''')

def Get_From_DB(self,S_no):
	strtm=conn.execute('''SELECT STARTIME FROM SCHEDLE WHERE SNO=S_no ''')
	endtm=conn.execute('''SELECT ENDTIME FROM SCHEDULER WHERE SNO=S_no''')
	dur=conn.e('''SELECT DURATION FROM SCHEDULE WHERE SNO=S_no''')
	n1=conn.execute('''SELECT NODE1 FROM SCHEDULER WHERE SNO=S_no''')
	n2=conn.execute('''SELECT NODE2 FROM SCHEDULER WHERE SNO=S_no''')
	n3=conn.execute('''SELECT NODE3 FROM SCHEDULER WHERE SNO=S_no''')
	n4=conn.execute('''SELECT NODE4 FROM SCHEDULER WHERE SNO=S_no''')
	stat=conn.execute('''SELECT STATUS FROM SCHEDULER WHERE SNO=S_no''')
	rstat=conn.execute('''SELECT RUNSTAT FROM SCHEDLER WHERE SNO=S_no''')
	SND_BACK={'index':S_no,'start_time':strtm,'end_time':endtm,'node_1':n1,'node_2':n2,'node_3':n3,'node_4':n4,'duration_time':dur,'status':stat,'runningstat':rstat}
	return SND_BACK
def Delete_Row(self,ROW_NUM):	
	conn.execute('''DELETE * FROM SCHEDULER WHERE SNO=ROW_NUM''')




 updateconn.execute('''CREATE TABLE LAMPLIFE(NODE INT PRIMARY KEY,
	                                  BALANCE INT''') #REMAINING LIFE IN MINUTS
#on clicking reset reset values to 1500

def lamplife:
	