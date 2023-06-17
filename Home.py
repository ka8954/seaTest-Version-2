import mysql.connector
import streamlit as slt
import random
import pandas as pd

conn = slt.experimental_connection('mysql',type='sql')


def main():
    slt.set_page_config(page_title="seaTest - Instructor Interface", page_icon="✨")
    slt.sidebar.title("")
    options = slt.sidebar.radio('Pages', options=("Entry", "Retreival"))

    def btn_click():
        print("Option Selected")

    def retreive():
        col1, col2, col3 = slt.columns([4.2, 9, 2])

        with col1:
            slt.write("")

        with col2:
            slt.image("srm.jpg", width=300)
            slt.write('Developed By Kaarthik Sai Charan Ayineni')

        with col3:
            slt.write("")
        slt.header('Student Wise Seating Arrangement')
        slt.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        doc = slt.file_uploader("Upload Your Excel Doc Here", type=["csv"])
        if doc is not None:
            df = pd.read_csv(doc)
            slt.dataframe(df)

    def entry():
        col1, col2, col3 = slt.columns([4.2, 9, 2])

        with col1:
            slt.write("")

        with col2:
            slt.image("srm.jpg", width=300)
            slt.write('Developed By Kaarthik Sai Charan Ayineni')

        with col3:
            slt.write("")

        slt.title('TEST SEATING ARRANGEMENT')
        slt.subheader('DEPT OF NETWORKING AND COMMUNICATIONS')
        slt.text('This System Allocates Seating for Students belonging to Cloud Computing, Cyber Security, IT, IOT, Networking Specializations')
        slt.write('# Type Of Exam')
        radio_btr = slt.selectbox(' ',options=("Choose an One", "Internals", "University Practical", "University Theory"))
        slt.write('# Enter the Details')
        df = conn.query('SELECT * FROM seat;', ttl=600)

        for row in df.itertuples():
            slt.write(f"{row.ID} {row.USERNAME} {row.Password} {row.Sysno} {row.Setno} {row.ExamDate}:")

    if options=='Entry':
        entry()


    if options=='Retreival':
        retreive()



if __name__ == '__main__':
    main()
