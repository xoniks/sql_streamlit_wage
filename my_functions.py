import sqlite3
import pandas as pd 

conn = sqlite3.connect('wages.db')
c = conn.cursor()


def create_table():
    c.execute(
        '''CREATE TABLE IF NOT EXISTS wage_data 
            (Name TEXT, Hours REAL, Rate REAL, Wage REAL)
        '''
    )
    c.commit()

def add_wage_entry(name, hours, rate, wage):
    c.execute(
        '''INSERT INTO wage_data (Name, Hours, Rate, Wage) VALUES (?,?,?,?)''',(name, hours, rate, wage)
    )

def fetch_all_data():
    c.execute(
        '''
            Select * From wage_data
        '''
    )
    data = c.fetchall()
    return pd.DataFrame(data, columns = ['Name','Hours','Rate','Wage'])



def calculate_wage(hours, rate):
    if hours>40:
        wage = (hours - 40) * 1.5 +  40 * rate
    else:
        wage = hours * rate
    return wage


