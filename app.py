import streamlit as st
import pandas as pd
import numpy as np
from src.laptop_price_prediction.pipeline.stage_04_prediction_pipeline import Prediction, CustomData

@st.cache_data
def load_data():
    '''
    This function loads the raw data
    '''
    try:
        data = pd.read_csv('artifacts/data_ingestion/raw.csv')
        return data

    except Exception as e:
        st.info(f':warning: An error occured while loading the data: {e}')
        return None
def main():
    '''
    This function initiates the streamlit app

    Raises:
        - Error: If there is an error in the streamlit app
    '''

    try:
        data = load_data()
        
        # Title in center
        st.markdown("<h1 style='text-align: center;'>Laptop Price Prediction 💻</h1>", unsafe_allow_html=True)

        st.write('')

        with st.container(border=True):
            comp, prod, name = st.columns(3)
            inch, scr, cpu = st.columns(3)
            ram, mem, gpu = st.columns(3)
            opsys, weight, _ = st.columns(3)

            with comp:
                Company = st.selectbox(
                    label='Company',
                    options=[None] + list(data['Company'].unique())
                )

            with prod:
                Product = st.selectbox(
                    label='Product',
                    options=[None] + list(data['Product'].unique())
                )

            with name:
                Type_Name = st.selectbox(
                    label='TypeName',
                    options=[None] + list(data['TypeName'].unique())
                )

            with inch:
                Inches = st.number_input(
                    label='Inches',
                    min_value=0.0,
                    max_value=20.0
                )
            
            with scr:
                ScreenResolution = st.selectbox(
                    label='ScreenResolution',
                    options=[None] + list(data['ScreenResolution'].unique())
                )

            with cpu:
                Cpu = st.selectbox(
                    label='Cpu',
                    options=[None] + list(data['Cpu'].unique())
                )

            with ram:
                Ram = st.number_input(
                    label='Ram',
                    min_value=0,
                    max_value=64
                )

            with mem:
                Memory = st.selectbox(
                    label='Memory',
                    options=[None] + list(data['Memory'].unique())
                )

            with gpu:
                Gpu = st.selectbox(
                    label='Gpu',
                    options=[None] + list(data['Gpu'].unique())
                )

            with opsys:
                OpSys = st.selectbox(
                    label='OpSys',
                    options=[None] + list(data['OpSys'].unique())
                )

            with weight:
                Weight = st.number_input(
                    label='Weight',
                    min_value=0.0,
                    max_value=10.0
                )

            st.write('')     # Add space between input features and button

            if 'predict' not in st.session_state:
                st.session_state.predict = False

            if st.button('Predict Price', type = 'primary'):
                st.session_state.predict = not st.session_state.predict

            if st.session_state.predict:
                if all(
                    [Company, Product, Type_Name, Inches, ScreenResolution, Cpu, Ram, Memory, Gpu, OpSys, Weight]
                ):
                    custom_data = CustomData(
                        Company=Company,
                        Product=Product,
                        Type_Name=Type_Name,
                        Inched=Inches,
                        ScreenResolution=ScreenResolution,
                        Cpu=Cpu,
                        Ram=Ram,
                        Memory=Memory,
                        Gpu=Gpu,
                        OpSys=OpSys,
                        Weight=Weight
                    )

                    features = custom_data.get_data_as_dataframe()
                    prediction = Prediction()
                    prediction = prediction.predict(features)
                    prediction = np.round(prediction[0], 2)

                    st.write('')   # Add space between button and output

                    st.info(f"""
                                
                    ### The predicted price of the laptop is:
                                
                    - **EURO**: :green[**{prediction}**]

                    - **NPR**: :green[**{round(prediction * 148, 2)}**]

                    - **USD**: :green[**{round(prediction * 1.18, 2)}**]

                    - **INR**: :green[**{round(prediction * 88, 2)}**]
                    """)
                else:
                    st.info(':warning: Please enter all the features')

    except Exception as e:
        st.error(f'An error occured: {e}')


if __name__ == '__main__':
    main()