import streamlit as st
import requests

st.set_page_config(page_title="عبدالله چلاسی - طراح و برنامه نویس",page_icon="images/a.jpg",layout="wide",)

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

    st.header("درباره من")

    imgabdollah , abdollah = st.columns(2)

    with imgabdollah:

        st.image("images/a.jpg",caption="00989335825325",width=200)

    with abdollah:

        st.header("عبداالله چلاسی")

        st.write("""
من متولد 1373 قشم - روستای گربدان هستم که در زمینه طراحی وب , دسکتاپ و برنامه نویسی موبایل فعالیت دارم و به صورت آزاد یا همون فریلنسینگ کار میکنم, یکی از اتفاقات جالب زندگیم اینه که تفریحم و شغلم یکی هستند و اونم چیزی نیست جز توسعه وب و اپلیکیشن , این داستان از سال 1391 شروع شد که به سمت تکنولوژی و دنیای برنامه نویسی پا گذاشتم همچنان این سابقه با گذر زمان همچنان بیشتر و بیشتر میشه، چون برنامه نویسی چیزی هست که من باهاش دنیا رو می بینم، می سنجم و حس میکنم،و سعی ام بر این است که با همین روند پیش برم و روز به روز با تکنولوژی های جدید دنیای برنامه نویسی کار کنم و تجربیات جدیدی کسب کنم         """)

  



with st.container():
    st.write("---")
    st.header("نمونه کارهای من")
    st.write("##")

    col1,col2,col3=st.columns((3))

    with col1:
        with st.expander(" فروشگاه جواهری رز" ,expanded=True):
            st.image("images/roz.png")
            st.write("""
زیورآلات رز یکی از بهترین جواهرات و طلافروشی ها با بهترین محصولات و مناسب ترین قیمت در جزیره زیبای قشم می باشد.    """)
            st.markdown("[Rose jewelry](https://roz.vercel.app)")
    with col2:

        with st.expander("وب سایت خدمات پی وی سی - رمکان",expanded=True):
            st.image("images/pvc.png")
            st.write("""
اجرای نصب پی وی سی در سراسر جزیره قشم        """)
            st.markdown("[Pvc-Ramkan](pvcahmad.ir)")
        
   
    with col3:
            with st.expander("دکوراسیـون شادمان - رمکان" ,expanded=True):
                st.image("images/upvc.png")
                st.write("""
تولیدی درب و پنجره UPVC نوین ترک , فروش و نصب PVC , طراحی یا ساخت و اجرای انواع سایبان PVC        """)
                st.markdown("[Dekorasion Shademan](pvcshademan.ir)")
    
    
    


    col1,col2=st.columns((2))

    with col1:
        with st.expander("خدمات اینترنتی طالب" ,expanded=True):
            st.image("images/taleb.png")
            st.write("""
خدمات نمایندگی طالب با نصب اولیه وای فای رایگان و شارژ اینترنتی اینترنتی و فروش تجهیزات وای فای با قیمت های مختلف در سراسر جزیره قشم    """)
            st.markdown("[Taleb internet services](https://taleb.vercel.app/)")
    

    with col2:
        with st.expander("عمر الزبير المرزوقي" ,expanded=True):
            st.image("images/omar.png")
            st.write("""
اول حكم يكسر قاعدة احتكار حكام أوربا على نهائيات كاس العالم لكرة اليد """)
            st.markdown("[عمر الزبير المرزوقي](https://omarzubair.vercel.app/)")
    
        with col2:
            with st.expander("Mazaya Car Rental, Dubai" ,expanded=True):
                st.image("images/mazaya.png")
                st.write("""
🇦🇪 اجاره ماشین مازایا، دبی 🇦🇪    """)
            st.markdown("[Mazaya Car Rental Dubai](https://mazaya-cars.vercel.app/)")
    
        
        with col1:

            with st.expander("⚽ Delfin Gorbadan cultural and sports club ⚽" ,expanded=True):
                st.image("images/gorbedan.png")
                st.write("""
باشگاه فوتبال دلفین گربدان یکی از پرافتخارترین و پرطرفدارترین باشگاه های جزیره قشم است. دلفین گربدان قبل از انقلاب ستاره جنوب گربدان نامیده می شد. این باشگاه اکنون در دسته دوم قشم قرار دارد. دلفین گربدان در سال 1324 در جزیره قشم روستای گربدان تأسیس شد. قرار داده شده است        """)
                st.markdown("[Delfin Gorbadan](http://gorbedan.ir/)")
    
        
# -------CONTACT-------

with st.container():
    st.write("---")
    st.header("تماس با من")
    st.write("##")

    st.text("برای سفارش پروژه شماره تماس تون رو ارسال کنید")


    contact_form="""
    <form action="https://formsubmit.co/abdollah.chelasi@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="نام شما" required>
     <input type="email" name="email" placeholder="ایمیل شما" required>
     <textarea name="message" placeholder="شماره تماس تون رو ارسال کنید" required ></textarea>
     <button type="submit">Send</button>
    </form> 
    """

    left , right = st.columns(2)

    with left:
        st.markdown(contact_form,unsafe_allow_html=True)

    with right:
        st.empty()