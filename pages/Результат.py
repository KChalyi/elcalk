import streamlit as st
import pandas as pd
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
st.title("Результаты расчёта падения напряжения")

if st.session_state["mosh5"]>0:
    st.write("Расчёты для Участка 1:")
    st.write("Активное сопротивление: " + str(round(st.session_state["r1"],4))  + " Ом" +"┃Реактивное сопротивление: ",  str(st.session_state["x1"]) + " Ом")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uV1"],2))  + " В" + "┃По нижеследующей формуле ⬇")
    st.image("images/uv.bmp")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uP1"],2))  + "%" + "┃По нижеследующей формуле ⬇")
    st.image("images/uvp.bmp")    
    st.write(__"Суммарное падение напряжения:"__ + str(round(st.session_state["uPE1"],2)) + "%")
    st.write("Расчёты для Участка 2:")
    st.write("Активное сопротивление: " + str(round(st.session_state["r2"],4))  + " Ом" +"┃Реактивное сопротивление: ",  str(st.session_state["x2"]) + " Ом")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uV2"],2))  + " В" + "┃По нижеследующей формуле ⬇")
    st.image("images/uv.bmp")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uP2"],2))  + "%" + "┃По нижеследующей формуле ⬇")
    st.image("images/uvp.bmp")    
    st.write("Суммарное падение напряжения: " + str(round(st.session_state["uPE2"],2)) + "%")
    st.write("Расчёты для Участка 3:")
    st.write("Активное сопротивление: " + str(round(st.session_state["r3"],4))  + " Ом" +"┃Реактивное сопротивление: ",  str(st.session_state["x3"]) + " Ом")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uV3"],2))  + " В" + "┃По нижеследующей формуле ⬇")
    st.image("images/uv.bmp")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uP3"],2))  + "%" + "┃По нижеследующей формуле ⬇")
    st.image("images/uvp.bmp")    
    st.write("Суммарное падение напряжения: " + str(round(st.session_state["uPE3"],2)) + "%")
    st.write("Расчёты для Участка 4:")
    st.write("Активное сопротивление: " + str(round(st.session_state["r4"],4))  + " Ом" +"┃Реактивное сопротивление: ",  str(st.session_state["x4"]) + " Ом")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uV4"],2))  + " В" + "┃По нижеследующей формуле ⬇")
    st.image("images/uv.bmp")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uP4"],2))  + "%" + "┃По нижеследующей формуле ⬇")
    st.image("images/uvp.bmp")    
    st.write("Суммарное падение напряжения: " + str(round(st.session_state["uPE4"],2)) + "%")
    st.write("Расчёты для Участка 5:")
    st.write("Активное сопротивление: " + str(round(st.session_state["r5"],4))  + " Ом" +"┃Реактивное сопротивление: ",  str(st.session_state["x5"]) + " Ом")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uV5"],2))  + " В" + "┃По нижеследующей формуле ⬇")
    st.image("images/uv.bmp")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uP5"],2))  + "%" + "┃По нижеследующей формуле ⬇")
    st.image("images/uvp.bmp")    
    st.write("Суммарное падение напряжения: " + str(round(st.session_state["uPE5"],2)) + "%")
elif st.session_state["mosh4"]>0:
    st.write("Расчёты для Участка 1:")
    st.write("Активное сопротивление: " + str(round(st.session_state["r1"],4))  + " Ом" +"┃Реактивное сопротивление: ",  str(st.session_state["x1"]) + " Ом")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uV1"],2))  + " В" + "┃По нижеследующей формуле ⬇")
    st.image("images/uv.bmp")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uP1"],2))  + "%" + "┃По нижеследующей формуле ⬇")
    st.image("images/uvp.bmp")    
    st.write("Суммарное падение напряжения: " + str(round(st.session_state["uPE1"],2)) + "%")
    st.write("Расчёты для Участка 2:")
    st.write("Активное сопротивление: " + str(round(st.session_state["r2"],4))  + " Ом" +"┃Реактивное сопротивление: ",  str(st.session_state["x2"]) + " Ом")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uV2"],2))  + " В" + "┃По нижеследующей формуле ⬇")
    st.image("images/uv.bmp")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uP2"],2))  + "%" + "┃По нижеследующей формуле ⬇")
    st.image("images/uvp.bmp")    
    st.write("Суммарное падение напряжения: " + str(round(st.session_state["uPE2"],2)) + "%")
    st.write("Расчёты для Участка 3:")
    st.write("Активное сопротивление: " + str(round(st.session_state["r3"],4))  + " Ом" +"┃Реактивное сопротивление: ",  str(st.session_state["x3"]) + " Ом")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uV3"],2))  + " В" + "┃По нижеследующей формуле ⬇")
    st.image("images/uv.bmp")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uP3"],2))  + "%" + "┃По нижеследующей формуле ⬇")
    st.image("images/uvp.bmp")    
    st.write("Суммарное падение напряжения: " + str(round(st.session_state["uPE3"],2)) + "%")
    st.write("Расчёты для Участка 4:")
    st.write("Активное сопротивление: " + str(round(st.session_state["r4"],4))  + " Ом" +"┃Реактивное сопротивление: ",  str(st.session_state["x4"]) + " Ом")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uV4"],2))  + " В" + "┃По нижеследующей формуле ⬇")
    st.image("images/uv.bmp")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uP4"],2))  + "%" + "┃По нижеследующей формуле ⬇")
    st.image("images/uvp.bmp")    
    st.write("Суммарное падение напряжения: " + str(round(st.session_state["uPE4"],2)) + "%")
elif st.session_state["mosh3"]>0:
    st.write("Расчёты для Участка 1:")
    st.write("Активное сопротивление: " + str(round(st.session_state["r1"],4))  + " Ом" +"┃Реактивное сопротивление: ",  str(st.session_state["x1"]) + " Ом")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uV1"],2))  + " В" + "┃По нижеследующей формуле ⬇")
    st.image("images/uv.bmp")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uP1"],2))  + "%" + "┃По нижеследующей формуле ⬇")
    st.image("images/uvp.bmp")    
    st.write("Суммарное падение напряжения: " + str(round(st.session_state["uPE1"],2)) + "%")
    st.write("Расчёты для Участка 2:")
    st.write("Активное сопротивление: " + str(round(st.session_state["r2"],4))  + " Ом" +"┃Реактивное сопротивление: ",  str(st.session_state["x2"]) + " Ом")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uV2"],2))  + " В" + "┃По нижеследующей формуле ⬇")
    st.image("images/uv.bmp")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uP2"],2))  + "%" + "┃По нижеследующей формуле ⬇")
    st.image("images/uvp.bmp")    
    st.write("Суммарное падение напряжения: " + str(round(st.session_state["uPE2"],2)) + "%")
    st.write("Расчёты для Участка 3:")
    st.write("Активное сопротивление: " + str(round(st.session_state["r3"],4))  + " Ом" +"┃Реактивное сопротивление: ",  str(st.session_state["x3"]) + " Ом")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uV3"],2))  + " В" + "┃По нижеследующей формуле ⬇")
    st.image("images/uv.bmp")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uP3"],2))  + "%" + "┃По нижеследующей формуле ⬇")
    st.image("images/uvp.bmp")    
    st.write("Суммарное падение напряжения: " + str(round(st.session_state["uPE3"],2)) + "%")
elif st.session_state["mosh2"]>0:
    st.write("Расчёты для Участка 1:")
    st.write("Активное сопротивление: " + str(round(st.session_state["r1"],4))  + " Ом" +"┃Реактивное сопротивление: ",  str(st.session_state["x1"]) + " Ом")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uV1"],2))  + " В" + "┃По нижеследующей формуле ⬇")
    st.image("images/uv.bmp")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uP1"],2))  + "%" + "┃По нижеследующей формуле ⬇")
    st.image("images/uvp.bmp")    
    st.write("Суммарное падение напряжения: " + str(round(st.session_state["uPE1"],2)) + "%")
    st.write("Расчёты для Участка 2:")
    st.write("Активное сопротивление: " + str(round(st.session_state["r2"],4))  + " Ом" +"┃Реактивное сопротивление: ",  str(st.session_state["x2"]) + " Ом")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uV2"],2))  + " В" + "┃По нижеследующей формуле ⬇")
    st.image("images/uv.bmp")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uP2"],2))  + "%" + "┃По нижеследующей формуле ⬇")
    st.image("images/uvp.bmp")    
    st.write("Суммарное падение напряжения: " + str(round(st.session_state["uPE2"],2)) + "%")
elif st.session_state["mosh1"]>0:
    st.write("Расчёты для Участка 1:")
    st.write("Активное сопротивление: " + str(round(st.session_state["r1"],4))  + " Ом" +"┃Реактивное сопротивление: ",  str(st.session_state["x1"]) + " Ом")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uV1"],2))  + " В" + "┃По нижеследующей формуле ⬇")
    st.image("images/uv.bmp")
    st.write("Падение напряжения на участке: " + str(round(st.session_state["uP1"],2))  + "%" + "┃По нижеследующей формуле ⬇")
    st.image("images/uvp.bmp")    
    st.write("Суммарное падение напряжения: " + str(round(st.session_state["uPE1"],2)) + "%")
