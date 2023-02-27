import streamlit as st
import pandas as pd
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
mtr_str=["Медь","Алюминий","Медь","Алюминий","Медь","Алюминий","Медь","Алюминий","Медь","Алюминий"]
st.title("Расчёт падения напряжения")
sel_decks = st.multiselect("Материал жилы кабелей", mtr_str)
while len(sel_decks)<5:
    sel_decks.append("0")
sech_str=[1.5,2.5,4,6,10,16,25,35,50,70,95,120,150,240]
sel_sech = st.multiselect("Сечения кабелей", sech_str)
while len(sel_sech)<5:
    sel_sech.append("0")
    
nap1, nap2, nap3, nap4, nap5 = (0 for i in range(5))
mosh1, mosh2, mosh3, mosh4, mosh5 = (0 for i in range(5))
length1, length2, length3, length4, length5 = (0 for i in range(5))
cos1, cos2, cos3, cos4, cos5 = (0 for i in range(5))
x1, x2, x3, x4, x5 = (0 for i in range(5))
r1, r2, r3, r4, r5 = (0 for i in range(5))
tok1, tok2, tok3, tok4, tok5 = (0 for i in range(5))
sin1, sin2, sin3, sin4, sin5 = (0 for i in range(5))
uV1, uV2, uV3, uV4, uV5 = (0 for i in range(5))
uP1, uP2, uP3, uP4, uP5 = (0 for i in range(5))
uPE1, uPE2, uPE3, uPE4, uPE5 = (0 for i in range(5))

nap1 = st.selectbox("Напряжение участка 1", [0,400,230])
nap2 = st.selectbox("Напряжение участка 2", [0,400,230])
nap3 = st.selectbox("Напряжение участка 3", [0,400,230])
nap4 = st.selectbox("Напряжение участка 4", [0,400,230])
nap5 = st.selectbox("Напряжение участка 5", [0,400,230])
mosh1=st.number_input("Укажите мощность участка 1", min_value=0.0, max_value=None, step=0.1)
mosh2=st.number_input("Укажите мощность участка 2", min_value=0.0, max_value=None, step=0.1)
mosh3=st.number_input("Укажите мощность участка 3", min_value=0.0, max_value=None, step=0.1)
mosh4=st.number_input("Укажите мощность участка 4", min_value=0.0, max_value=None, step=0.1)
mosh5=st.number_input("Укажите мощность участка 5", min_value=0.0, max_value=None, step=0.1)
length1=st.number_input("Укажите длину участка 1", min_value=0.0, max_value=None, step=0.1)
length2=st.number_input("Укажите длину участка 2", min_value=0.0, max_value=None, step=0.1)
length3=st.number_input("Укажите длину участка 3", min_value=0.0, max_value=None, step=0.1)
length4=st.number_input("Укажите длину участка 4", min_value=0.0, max_value=None, step=0.1)
length5=st.number_input("Укажите длину участка 5", min_value=0.0, max_value=None, step=0.1)
cos1=st.number_input("Укажите коэффициент мощности участка 1", min_value=0.0, max_value=1.0, step=0.01)
cos2=st.number_input("Укажите коэффициент мощности участка 2", min_value=0.0, max_value=1.0, step=0.01)
cos3=st.number_input("Укажите коэффициент мощности участка 3", min_value=0.0, max_value=1.0, step=0.01)
cos4=st.number_input("Укажите коэффициент мощности участка 4", min_value=0.0, max_value=1.0, step=0.01)
cos5=st.number_input("Укажите коэффициент мощности участка 5", min_value=0.0, max_value=1.0, step=0.01)

if st.button("Подготовить расчёт"):
        if sel_decks[0]=="Медь":
            r1=0.0175
        if sel_decks[1]=="Медь":
            r2=0.0175
        if sel_decks[2]=="Медь":
            r3=0.0175
        if sel_decks[3]=="Медь":
            r4=0.0175
        if sel_decks[4]=="Медь":
            r5=0.0175
        if sel_decks[0]=="Алюминий":
            r1=0.027
        if sel_decks[1]=="Алюминий":
            r2=0.027
        if sel_decks[2]=="Алюминий":
            r3=0.027
        if sel_decks[3]=="Алюминий":
            r4=0.027
        if sel_decks[4]=="Алюминий":
            r5=0.027

        if sel_decks[0]=="Медь":
            x1=0.00008
        if sel_decks[1]=="Медь":
            x2=0.00008
        if sel_decks[2]=="Медь":
            x3=0.00008
        if sel_decks[3]=="Медь":
            x4=0.00008
        if sel_decks[4]=="Медь":
            x5=0.00008
        if sel_decks[0]=="Алюминий":
            x1=0.00008
        if sel_decks[1]=="Алюминий":
            x2=0.00008
        if sel_decks[2]=="Алюминий":
            x3=0.00008
        if sel_decks[3]=="Алюминий":
            x4=0.00008
        if sel_decks[4]=="Алюминий":
            x5=0.00008

        if cos1>0:
            sin1=(1-cos1)**(0.5)
        if cos2>0:
            sin2=(1-cos2)**(0.5)
        if cos3>0:
            sin3=(1-cos3)**(0.5)
        if cos4>0:
            sin4=(1-cos4)**(0.5)
        if cos5>0:
            sin5=(1-cos5)**(0.5)
        if mosh1>0:
            if nap1==230:
                tok1=mosh1*1000/230
                uV1=2*tok1*(r1*length1/sel_sech[0]*cos1+x1*length1*sin1)
            if nap1==400:
                tok1=round(mosh1/(0.4*(3**(0.5))),2)
                uV1=1*tok1*(r1*length1/sel_sech[0]*cos1+x1*length1*sin1)
            uP1=100*(uV1/230)
            uPE1=uP1
        if mosh2>0:
            if nap2==230:
                tok2=mosh2*1000/230
                uV2=2*tok2*(r2*length2/sel_sech[1]*cos2+x2*length2*sin2)
            if nap1==400:
                tok2=round(mosh2/(0.4*(3**(0.5))),2)
                uV2=1*tok2*(r2*length2/sel_sech[1]*cos2+x2*length2*sin2)
            uP2=100*(uV2/230)
            uPE2=uP1+uP2
        if mosh3>0:
            if nap3==230:
                tok3=mosh3*1000/230
                uV3=2*tok3*(r3*length3/sel_sech[2]*cos3+x3*length3*sin3)
            if nap3==400:
                tok3=round(mosh3/(0.4*(3**(0.5))),2)
                uV3=1*tok3*(r3*length3/sel_sech[2]*cos3+x3*length3*sin3)
            uP3=100*(uV3/230)
            uPE3=uP1+uP2+uP3
        if mosh4>0:
            if nap4==230:
                tok4=mosh4*1000/230
                uV4=2*tok4*(r4*length4/sel_sech[3]*cos4+x4*length4*sin4)
            if nap4==400:
                tok4=round(mosh4/(0.4*(3**(0.5))),2)
                uV4=1*tok4*(r4*length4/sel_sech[3]*cos4+x4*length4*sin4)
            uP4=100*(uV4/230)
            uPE4=uP1+uP2+uP3+uP4
        if mosh5>0:
            if nap5==230:
                tok5=mosh5*1000/230
                uV5=2*tok5*(r5*length5/sel_sech[4]*cos5+x5*length5*sin5)
            if nap5==400:
                tok5=round(mosh5/(0.4*(3**(0.5))),2)
                uV5=1*tok5*(r5*length5/sel_sech[4]*cos5+x5*length5*sin5)
            uP5=100*(uV5/230)
            uPE5=uP1+uP2+uP3+uP4+uP5
        st.write("Рассчитано ✅")
        if mosh1>0:
            df=pd.DataFrame({"Участок 1":[round(uV1,2),round(uP1,2),round(uPE1,2)]
                             })
        if mosh2>0:
            df=pd.DataFrame({"Участок 1":[round(uV1,2),round(uP1,2),round(uPE1,2)],
                             "Участок 2":[round(uV2,2),round(uP2,2),round(uPE2,2)]
                             })    
        if mosh3>0:          
            df=pd.DataFrame({"Участок 1":[round(uV1,2),round(uP1,2),round(uPE1,2)],
                             "Участок 2":[round(uV2,2),round(uP2,2),round(uPE2,2)],
                             "Участок 3":[round(uV3,2),round(uP3,2),round(uPE3,2)]
                             })   
        if mosh4>0:          
            df=pd.DataFrame({"Участок 1":[round(uV1,2),round(uP1,2),round(uPE1,2)],
                             "Участок 2":[round(uV2,2),round(uP2,2),round(uPE2,2)],
                             "Участок 3":[round(uV3,2),round(uP3,2),round(uPE3,2)],
                             "Участок 4":[round(uV4,2),round(uP4,2),round(uPE4,2)]
                             })
        if mosh5>0:          
            df=pd.DataFrame({"Участок 1":[round(uV1,2),round(uP1,2),round(uPE1,2)],
                             "Участок 2":[round(uV2,2),round(uP2,2),round(uPE2,2)],
                             "Участок 3":[round(uV3,2),round(uP3,2),round(uPE3,2)],
                             "Участок 4":[round(uV4,2),round(uP4,2),round(uPE4,2)],
                             "Участок 5":[round(uV5,2),round(uP5,2),round(uPE5,2)]
                             })
        if mosh1>0:
            df.index=["Падение напряжения на участке, В", "Падение напряжения на участке, %", "Суммарное падение напряжения, %"]
            st.write(df)
        else:
            st.write("Данные не введены ❌")
st.session_state["mosh1"]=mosh1
st.session_state["mosh2"]=mosh2
st.session_state["mosh3"]=mosh3
st.session_state["mosh4"]=mosh4
st.session_state["mosh5"]=mosh5
st.session_state["uV1"]=uV1
st.session_state["uV2"]=uV2
st.session_state["uV3"]=uV3
st.session_state["uV4"]=uV4
st.session_state["uV5"]=uV5
st.session_state["uP1"]=uP1
st.session_state["uP2"]=uP2
st.session_state["uP3"]=uP3
st.session_state["uP4"]=uP4
st.session_state["uP5"]=uP5
st.session_state["uPE1"]=uPE1
st.session_state["uPE2"]=uPE2
st.session_state["uPE3"]=uPE3
st.session_state["uPE4"]=uPE4
st.session_state["uPE5"]=uPE5
st.session_state["r1"]=r1
st.session_state["r2"]=r2
st.session_state["r3"]=r3
st.session_state["r4"]=r4
st.session_state["r5"]=r5
st.session_state["x1"]=x1
st.session_state["x2"]=x2
st.session_state["x3"]=x3
st.session_state["x4"]=x4
st.session_state["x5"]=x5
