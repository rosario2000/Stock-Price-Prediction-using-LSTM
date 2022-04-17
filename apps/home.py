import streamlit as st
import streamlit.components.v1 as components

def app():
    st.title("Home")
    # bootstrap 4 collapse example
    components.html(
        """
        <link rel="preconnect" href="https://fonts.googleapis.com">
       <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
       <link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
       <style>
       body{line-height:1.5;color:white;}
       h1{font-family:'Montserrat', sans-serif;font-size: 2.5rem;}
       p{'Montserrat', sans-serif;font-size: 1.2rem}
       </style>

        <h1>Introduction</h1>
        <p>The stock market is a vast array of investors and traders who buy and sell stock, pushing the price up or down. The prices of stocks are governed by the principles of demand and supply, and the ultimate goal of buying shares is to make money by buying stocks in companies whose perceived value (i.e., share price) is expected to rise. Stock markets are closely linked with the world of economics — the rise and fall of share prices can be traced back to some Key Performance
           Indicators (KPI's). The five most commonly used KPI's are the opening stock price (`Open'), end-of-day price (`Close'), intraday low price (`Low'), intra-day peak price (`High'), and total volume of stocks traded during the day (`Volume').
        </p>

        <h1>About TrendSetter</h1>
        <p><b>TrendSetter</b> is one of the most accurate stock price predicting web application. The prediction of the stock prices of a particular stock is made on the basis of the data extracted from <a href="#">Yahoo finance</a> website. This application use a Machine learning algorithm called Long-Short Term Memory. To know more about this algorithm, you can visit <a href="https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjU37OFvMX2AhXXwjgGHTzaArsQFnoECAkQAQ&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FLong_short-term_memory&usg=AOvVaw0A_KKzJyoRx3J4vpb6wS3E">here</a></p>
        """,
        height=900,
    )