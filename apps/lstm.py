import streamlit as st
from datetime import date
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.models import load_model
import yfinance as yf
from plotly import graph_objs as go

def app():
    START = "2000-01-01"
    TODAY = date.today().strftime("%Y-%m-%d")
    
    
    st.title('Long Short Term Memory')
    selected_stock = st.text_input('Enter Ticker','KPITTECH.NS')
    
    n_years = st.slider('Years of prediction:', 1, 4)
    
    @st.cache
    def load_data(ticker):
        data = yf.download(ticker, START, TODAY)
        data.reset_index(inplace=True)
        return data
    
    	
    data_load_state = st.text('Loading data...')
    data = load_data(selected_stock)
    data_load_state.text('Loading data... done!')
    
    st.subheader('Raw data')
    st.write(data.tail())
    
    # Plot raw data
    #def plot_raw_data():
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
    fig1.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
    fig1.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig1)
    	
    #plot_raw_data()
    
    # Plot Moving Averages
    
    ma100 = data.Close.rolling(100).mean()
    ma200 = data.Close.rolling(200).mean()
    #def plot_ma():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
    fig.add_trace(go.Scatter(x=data['Date'], y=ma100, name="100-Day Moving Average"))
    fig.add_trace(go.Scatter(x=data['Date'], y=ma200, name="200-Day Moving Average"))
    fig.layout.update(title_text='Moving Averages with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
    
    #plot_ma()
    
    #dividing training and testing
    
    data_training = pd.DataFrame(data['Close'][0:int(len(data)*0.70)])
    data_testing = pd.DataFrame(data['Close'][int(len(data)*0.70):int(len(data))])
    
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler(feature_range = (0,1))
    
    #loading lstm model
    model = load_model('keras_model.h5')
    
    #testing
    past_100_days = data_training.tail(100)
    final_df = past_100_days.append(data_testing,ignore_index = True)
    input_data = scaler.fit_transform(final_df)
    
    x_test = []
    y_test = []
    for i in range(100, input_data.shape[0]):
        x_test.append(input_data[i-100: i])
        y_test.append(input_data[i, 0])
    x_test,y_test = np.array(x_test),np.array(y_test)
    
    y_predicted = model.predict(x_test)
    scaler = scaler.scale_
    
    scale_factor = 1/scaler[0]
    y_predicted = y_predicted*scale_factor
    y_test = y_test*scale_factor
    
    #prediction visual
    
    st.subheader('Predictions Vs Original')
    fig2 = plt.figure(figsize = (18,10))
    plt.plot(y_test,'b',label = 'Original Price')
    plt.plot(y_predicted,'r',label = 'Predicted Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    st.pyplot(fig2)