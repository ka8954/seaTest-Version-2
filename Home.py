import streamlit as slt
import random
import pandas as pd


def main():
    slt.set_page_config(page_title="seaTest - Instructor Interface", page_icon="✨")
    slt.sidebar.title("")
    options = slt.sidebar.radio('Pages', options=("Entry", "Retreive"))

    def btn_click():
        print("Option Selected")

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
        slt.text(
            'This System Allocates Seating for Students belonging to Cloud Computing, Cyber Security, IT, IOT, Networking Specializations')
        slt.write('# Type Of Exam')
        radio_btr = slt.selectbox(' ',
                                  options=("Choose an One", "Internals", "University Practical", "University Theory"))
        slt.write('# Enter the Details')
        id = slt.text_input('USER ID', max_chars=15)
        UNAME = slt.text_input('USERNAME', max_chars=6)
        PWORD = slt.text_input('PASSWORD', max_chars=4)
        labcapacity = 50

        a = 1
        x = [i for i in range(a, labcapacity + 1)]
        random.shuffle(x)

        for i in range(0, 50):
            seat = x[i]
            if seat % 2 == 0:
                Setno = "SET-1"
            else:
                Setno = "SET-2"

        exam_date = slt.date_input("SELECT THE DATE OF EXAM")
        print(exam_date)

        if slt.button("SUBMIT"):
            
            conn = slt.experimental_connection('mysql', type='sql')
            df = conn.query("INSERT INTO seat (ID,USERNAME,Password, Sysno, Setno, ExamDate) VALUES(id,UNAME,PWORD,seat,Setno,exam_date);")
            slt.success("Details Saved")

            co1, co2 = slt.columns(2)
            co3, co4 = slt.columns(2)
            co5, co6 = slt.columns(2)
            co1.info('Seat No ')
            co2.success(seat)
            co3.info('Set No ')
            co4.success(Setno)
            co5.info('Date Of Exam ')
            co6.success(exam_date)

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




    if options == 'Entry':
        entry()

    if options == 'Retreive':
        retreive()


if __name__ == '__main__':
    main()
