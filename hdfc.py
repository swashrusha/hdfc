import streamlit as st
import pandas as pd
from supabase import create_client
SUPABASE_URL="https://ozknalbtslfhisuebnbj.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im96a25hbGJ0c2xmaGlzdWVibmJqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYwNDA4OTIsImV4cCI6MjA4MTYxNjg5Mn0.hQPB8ZDxMl0uUNvML-76FcA2P1gyBcXvoD4eUVpRoAI"
supabase=create_client(SUPABASE_URL, SUPABASE_KEY)
st.title("HDFC BANK(supabase)")
menu=["REGISTER","VIEW"]
choice=st.sidebar.selectbox("Menu",menu)
if choice=="REGISTER":
    name=st.text_input("Enter name")
    age=st.number_input("AGE", min_value=18)
    account=int(st.number_input("ACCOUNT NUMBER"))
    bal=st.number_input("BALANCE",min_value=500)
    if st.button("Save"):
        supabase.table("users").insert({
            "name":name,
            "age":age,
            "account":account,
            "balance":bal}).execute()
        st.success("user added successfully")

if choice=="VIEW":
    st.subheader("view users")
    data=supabase.table("users").select("*").execute()
    df=pd.DataFrame(data.data)
    st.dataframe(df)
