import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("💰 Monte Carlo Profit Optimizer")
st.write("จำลองสถานการณ์เพื่อหากำไรสูงสุด")

# ส่วนรับข้อมูลจากผู้ใช้
with st.sidebar:
    st.header("Settings")
    current_price = st.number_input("ราคาสินทรัพย์ปัจจุบัน", value=100.0)
    volatility = st.slider("ความผันผวน (%)", 1, 100, 20) / 100
    days = st.number_input("จำนวนวันที่ต้องการพยากรณ์", value=30)
    simulations = st.number_input("จำนวนครั้งที่สุ่ม (Simulations)", value=1000)

if st.button("Run Simulation"):
    # คำนวณ Monte Carlo
    returns = np.random.normal(0, volatility/np.sqrt(days), (days, simulations))
    price_paths = current_price * (1 + returns).cumprod(axis=0)
    
    # วาดกราฟ
    fig, ax = plt.subplots()
    ax.plot(price_paths, alpha=0.1, color='blue')
    ax.set_title("Predicted Price Paths")
    st.pyplot(fig)
    
    # สรุปผล
    final_prices = price_paths[-1]
    st.subheader(f"📊 ผลลัพธ์คาดการณ์ในอีก {days} วัน")
    st.write(f"กำไรเฉลี่ยที่น่าจะเป็น: {np.mean(final_prices):.2f}")
    st.write(f"โอกาสขาดทุน: {(final_prices < current_price).mean()*100:.2f}%")
