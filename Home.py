import streamlit as slt
import random
import pandas as pd
from deta import Deta

print("Connection Established")


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

            detakey = "d0lc5a51pd8_CRVUTN7yCBRhuBC6ZnwUPctUTEoyG61L"

            deta = Deta(detakey)
            db = deta.Base("seat")

            l1 = []
            l2 = []
            l3 = []

            if id is not None:
                if id not in l1:
                    l1.append(id)
                else:
                    slt.error("Duplicate Entry For ID")
                    
            if UNAME is not None:
                if UNAME not in l2:
                    l2.append(UNAME)
                else:
                    slt.error("Duplicate Entry For Username")
                    
            if seat is not None:
                if seat not in l3:
                    l3.append(seat)
                    db.put({"ID": id, "Username": UNAME, "Password": PWORD, "Seat": seat, "Setno": Setno})
                    slt.success("Details Saved")
                else:
                    slt.error("Seat No Already Allocated")
                    


    if options == 'Entry':
        entry()

    if options == 'Retreival':
        retreive()


if __name__ == '__main__':
    main()
