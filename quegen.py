# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import streamlit as st
# from jemo import *  
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
        )
    if 'my_dict' not in st.session_state:
        st.session_state.my_dict = {}

    with st.sidebar:
        l1 = []
        st.title("Sectional Details")
        with st.form("Sectional Details",clear_on_submit=True):
            # file = st.file_uploader("Upload Your book", type="pdf",disabled=True)
            Section = st.radio("Select Section Name", ["A", "B", "C"],horizontal = True,index=0,key='section')
            show_A = False
            show_B = False 
            show_C = False
            if Section == "A":
                show_A = True
            elif Section == "B": 
                show_B = True
            else:
                show_C = True
            # print(Section)
            question_type = st.selectbox("Select Question Type", ["MCQS","True / False","Coding Question","Theoritical","Short Question"],placeholder="Ex : mcqs,coding question",index=1)
            question_level = st.selectbox("Select Question Level", ["Easy", "Medium", "Hard"],index=1)
            num_questions = st.number_input("How many questions?", min_value=1,max_value=12, step=1) 
            # Topics = st.text_input("topics",placeholder="ex : machine learning,deep learning")
            countries = ["machine learning", "python", "Computer Vision", "CNN", "AI", "deep learning"]
            Topics = st.multiselect("Choose Topic", countries, ["python"])
            submitted = st.form_submit_button("Submit")
            if submitted:
                l1.append(Section)
                l1.append(question_type)
                l1.append(question_level)
                l1.append(num_questions)
                l1.append(Topics)
                st.session_state.my_dict[Section] = l1
            reset = st.form_submit_button("reset")


    if st.session_state.my_dict:
        with st.expander("See Selected Section details"):
            columns = st.columns(len(st.session_state.my_dict))

            # A list to collect keys to be removed
            keys_to_remove = []
        
        
            # Display data and add "Remove" button for each column 
            for col, (key, value) in zip(columns, st.session_state.my_dict.items()):
                col.subheader(f"Section {key}")
                col.write(value)
                # Use a "Remove" button to add the key to keys_to_remove list
                if col.button(f"Double-Click to Remove {key}"):
                    keys_to_remove.append(key)

            # Remove the selected keys
            for key in keys_to_remove:
                del st.session_state.my_dict[key]

    if st.session_state.my_dict:
        op = st.button("Generate question paper",type='primary',key='dif2')
        if op: 
            input_dict = st.session_state.my_dict
            # question_paper_result = generate_questions(input_dict)
            st.write("Generate Question Paper")
            question_paper_result = "Dio dio"
            st.write(question_paper_result)
            if st.download_button("Download as Text File",data=question_paper_result,type='primary',key='non'): 
                st.success("Text file downloaded!")

if __name__ == "__main__":
    run()




            
    






