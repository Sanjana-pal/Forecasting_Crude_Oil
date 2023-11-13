

import pickle
import streamlit as st 
from prophet import Prophet

pickle_in = open('prophhett.pkl', 'rb')
model = pickle.load(pickle_in)


def prediction(n_years):
    return model.predict(model.make_future_dataframe(periods=n_years*365)).tail(n_years*365)

def main():
    html_temp = """
    <div style ="background-color:tomato;padding:10x">
    <h2 style = "color:white;text-align:center;">Oil Price Prediction</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    
    n_years = st.selectbox("Select the number of years to forecast:", list(range(1, 6)))

    
    if st.button("Forecast"):
        result = prediction(n_years)
        st.subheader('Forecast Data: ')
        st.write(result[['ds','yhat']])
        
if __name__=='__main__':
    main()