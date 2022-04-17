from multiapp import MultiApp
from apps import home,lstm,rf
import streamlit.components.v1 as components

app = MultiApp()


components.html(
    """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
    
    <h1 style="font-family: 'Montserrat', sans-serif;font-size: 4.5rem;color:white;">TrendSetter<br><div style="font-size:1.5rem;">Predicting the trends for you :)</div></h1>
    <p style="font-family: 'Montserrat', sans-serif;font-size: 1rem;color:white;">Developed by <a href="https://github.com/rosario2000/">Harsh Mohta</a><br> All rights reserved ©</p>
    """,
    height=320,
)


# Add all your application here
app.add_app("Home", home.app)
app.add_app("Long Short Term Memory", lstm.app)
app.add_app("Random Forest", rf.app)
# The main app
app.run()

