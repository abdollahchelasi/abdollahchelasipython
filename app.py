import streamlit as st
import requests

st.set_page_config(page_title="Abdollah Chelasi - designer and programmer",page_icon="https://abdollahchelasi.vercel.app/a.jpg",layout="wide")

with open('c.css') as f:
    st.markdown(f"<style> {f.read()} </style>",unsafe_allow_html=True)






with st.container():
        left_column,right_column = st.columns(2)
        with left_column:
            st.subheader("""
طراحی سایت با بهترین کیفیت در کمترین زمان    """)
            st.write("##")
            st.write("""
            """)

        with right_column:
            st.image("https://cdn.dribbble.com/users/1118376/screenshots/3604186/developer-dribbble.gif",width=300)


with st.container():

    

    st.write("---")

    st.header("About Me")

    imgabdollah , abdollah = st.columns(2)

    with imgabdollah:

        st.image("images/a.jpg",caption="00989335825325",width=200)

    with abdollah:

        st.header("ABDOLLAH CHELASI")

        st.write("""
من متولد 1373 قشم - روستای گربدان هستم که در زمینه طراحی وب , دسکتاپ و برنامه نویسی موبایل فعالیت دارم و به صورت آزاد یا همون فریلنسینگ کار میکنم, یکی از اتفاقات جالب زندگیم اینه که تفریحم و شغلم یکی هستند و اونم چیزی نیست جز توسعه وب و اپلیکیشن , این داستان از سال 1391 شروع شد که به سمت تکنولوژی و دنیای برنامه نویسی پا گذاشتم همچنان این سابقه با گذر زمان همچنان بیشتر و بیشتر میشه، چون برنامه نویسی چیزی هست که من باهاش دنیا رو می بینم، می سنجم و حس میکنم،و سعی ام بر این است که با همین روند پیش برم و روز به روز با تکنولوژی های جدید دنیای برنامه نویسی کار کنم و تجربیات جدیدی کسب کنم         """)

  



with st.container():
    st.write("---")
    st.header("My Project")
    st.write("##")

    col1,col2,col3,col4=st.columns((4))

    with col1:
        with st.expander("Website Rose jewelry" ,expanded=True):
            st.image("images/roz.png")
            st.write("""
        Rose jewelry is one of the best jewelry and gold shops with the best products and the most reasonable prices in the beautiful island of Qeshm.
    """)
            st.markdown("[Rose jewelry](https://roz.vercel.app)")
    with col2:

        with st.expander("وب سایت خدمات پی وی سی - رمکان",expanded=True):
            st.image("images/pvc.png")
            st.write("""
اجرای نصب پی وی سی در سراسر جزیره قشم        """)
            st.markdown("[پی وی سی - رمکان](https://pvcahmad.iran.liara.run/)")
        
   
    with col3:
            with st.expander("دکوراسیـون شادمان - رمکان" ,expanded=True):
                st.image("images/upvc.png")
                st.write("""
تولیدی درب و پنجره UPVC نوین ترک , فروش و نصب PVC , طراحی یا ساخت و اجرای انواع سایبان PVC        """)
                st.markdown("[دکوراسیـون شادمان](https://upvcahmad.iran.liara.run/)")
    
    with col4:
            with st.expander("⚽ Delfin Gorbadan cultural and sports club ⚽" ,expanded=True):
                st.image("images/gorbedan.png")
                st.write("""
Delfin Garbdan football club is one of the most proud and most popular football clubs in Qeshm Island. Before the revolution, Delfin Garbdan was called Southern Star of Garbdan. The club is now in the second division of Qeshm. Delfin Garbdan was founded in 1324 in Qeshm Island, Garbdan village. has been placed
        """)
                st.markdown("[Delfin Gorbadan](http://gorbedan.ir/)")
    
    


    col1,col2=st.columns((2))

    with col1:
        with st.expander("Website Taleb internet services" ,expanded=True):
            st.image("images/taleb.png")
            st.write("""
Talib agency services with initial Wi-Fi installation for free and internet charging online and sale of Wi-Fi equipment at different prices all over Qeshm Island
    """)
            st.markdown("[Taleb internet services](https://taleb.vercel.app/)")
    

    with col2:
        with st.expander("Website Island driving school" ,expanded=True):
            st.image("https://abdollahchelasi.vercel.app/amoozesh.png")
            st.write("""
Island driving school in the beautiful island of Qeshm
    """)
            st.markdown("[Island driving school](http://amoozeshgahjazire.ir/)")
    
        with col2:
            with st.expander("Mazaya Car Rental, Dubai" ,expanded=True):
                st.image("images/mazaya.png")
                st.write("""
            🇦🇪 Mazaya Car Rental, Dubai 🇦🇪
    """)
            st.markdown("[Mazaya Car Rental Dubai](https://mazaya-cars.vercel.app/)")
    
        
    
        
# -------CONTACT-------

with st.container():
    st.write("---")
    st.header("GET CALL")
    st.write("##")

    st.text("Contact me to order the project .")


    contact_form="""
    <form action="https://formsubmit.co/abdollah.chelasi@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required ></textarea>
     <button type="submit">Send</button>
    </form> 
    """

    left , right = st.columns(2)

    with left:
        st.markdown(contact_form,unsafe_allow_html=True)

    with right:
        st.empty()