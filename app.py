from PyPDF2 import PdfFileMerger
import streamlit as st

st.title('Simple PDF Merger')

st.header('Please enter the number of PDFs you want to merge ')
num = st.number_input(" ",
                      min_value= 2,
                      max_value= 60,
                      step= 1,
                      value = 2)

try:
    pdfs = []
    for n in range(int(num)):
        pdf = st.file_uploader("upload PDF {}".format(n + 1))
        pdfs.append(pdf)

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    name = st.text_input("Enter the name of result file: ")
    if len(name) != 0:
        if st.button('DOWNLOAD'):
            complete_name = name + '.pdf'
            merger.write(complete_name)
            merger.close()

except:
    st.write("", )

st.sidebar.markdown('''
created by Sanket Chavan 
''')

st.sidebar.markdown('''
    Connect on <a href = "https://www.linkedin.com/in/sanket-chavan5595/" target = "_blank"> Linkedin </a>
    ''', True)

