#Importing Libraries
from turtle import right
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

#Web Page Title 
st.set_page_config(page_title="Resume-Shiaz Asif", page_icon=":earth_asia:",layout="wide")

#Adding Images & Resizing
My_image = Image.open("images/shiaz_asif.png")
My_image = My_image.resize((300,300),Image.ANTIALIAS)
Tool_image = Image.open("images/Tools.png")
Tool_image = Tool_image.resize((600,600),Image.ANTIALIAS)
#Loading Animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

#headered of My Image & Personal Information
with st.container():
    image_column, text_column = st.columns((1, 1))
    with image_column:
        st.image(My_image)

    with text_column:
        st.subheader("Personal Information")
        st.write(":e-mail: shiazasif.data@gmail.com")
        st.write(":telephone_receiver: +91 91644 56725")
        st.write(":round_pushpin:Local Address - Bangalore, Karnataka, India -5600 45")
        st.write(":round_pushpin:Current Address - Pune, Maharashtra, India -4110 28")
        if st.button('View LinkedIn Profile'):
            st.write("[👀Click here](https://www.linkedin.com/in/shiaz-asif-507a1a191)")
        if st.button('Download Resume'):
            st.write("[:arrow_down:Click here](https://drive.google.com/file/d/1uA_-buh7bXbrSRSWFaYw8LpzCfX_X7AE/view?usp=sharing)")
#Sub Header
with st.container():
    st.title("Hi, Iam Shiaz Asif :wave:")
    st.write(
        f"""
Process oriented data analyst with 5 years of experience.
Experienced in interpreting, analyzing data to drive growth
for a company. By Reducing operating costs. Furnish
insights, analytics, and business intelligence needed to
guide decisions.
        """
        )
    st.write("---")

with st.container():
    left_column, right_column =st.columns((1,1))
    with left_column:
        st.header("Skills & Tools :computer:")
        st.write("""
- Developing, implementing databases & collecting data.
- Identifying, analyzing & interpreting data by
  visualization.
- Minimizing manual handling by automating daily task.
- Data exploration, modeling & deployment.
- Developing & implementing ERP for organization.
- Financial analysis & mid-term planning for budget.
- Planning, developing, controlling & forecasting budget.
- P2P & Inventory management.

        """)
        st.image(Tool_image)

with st.container():
    st.write("###")
    st.write("---")
    st.header("Work Experience")
    st.subheader(" ISS INDIA - Barclays Global Technology Center - Pune")
    st.write("- Senior Executive - MIS, Oct 2021 - Present")
    st.write(f"""
Responsible for ensuring that all demand that
comes through the Team is actioned as per agreed
SOW & Ensure that transactions are processed
quickly and efficiently working with accounts
payable/finance, & to ensure that the credit rating
for business is not impacted. Preparing budget
reports, monitor spending & reconcile of funds,
positions, P&L and MMR reports.
""")        

    st.subheader(" Hatti Food & Beverages Pvt Ltd - Bangalore")
    st.write("""
- Sr. Data Analyst and Controller, Feb-Oct 2021
- Data Analyst and Controller, Oct-Jan 2021
                 """)
    st.write(f"""
Responsible for gathering data from various
sources analyze it & turn into a information,
which helps management to improve business,
reduce operating cost, avoid losses & to take
right business decisions on operations, SCM,
audit at ground level by improving current process
& implementing new process.
Helping team by understanding the current
challenges of operation & to solve challenges
by execution, of ERPNext, Automation & to take
them to completion & drive long standing.
""")        

    with right_column:
        
        st.header("Education:mortar_board:")
        st.write("""
        - Bachelor In Commerce with Computer-Applications - Indian School of Management & Technical Studies
        - SSLC Karnataka Secondary Board - Corporation High School for Boys
        - High School Education - Seventh Day Adventist English High School
        """)
        
        st.header("Certified Courses")
        st.write("""
        - Python for Data Science & data analytics - Udemy
        - Advance MS Excel Workshop, Effective Dashboard - JS Academy
        - Masters In MS Excel Power Query & M Language - Udemy
        - MS Office, Internet & More - Mega Infotech Computers Educational Society
        """)
#Animation Link & Size        
        lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_o6spyjnc.json")
        st_lottie(lottie_coding, height=300, key="coding")      
    
#---Contact Form ---
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documentation
    contact_form = """
    <form action="https://formsubmit.co/shiazasif.data@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column =st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

# ---Use Local Css File to design form---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)

local_css("style/style.css")


