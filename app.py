import streamlit as st
from contrato import Vendas
from datetime import datetime, time
from pydantic import ValidationError

def main():
    st.title('Sistema de CRM e Vendas da Zapflow - Frontend Simples')

    email = st.text_input('Campo de texto para inserção do email do vendedor.')
    data = st.date_input('Data da Compra', datetime.now())
    hora = st.time_input('Hora da Compra', value=time(9, 0))
    valor = st.number_input('Campo numérico para inserir o valor monetário da venda realizada.', min_value=0.0, format="%.2f")
    quantidade = st.number_input('Campo numérico para inserir a quantidade de produtos vendidos.', step=1, min_value=1)
    produto = st.selectbox('Campo de seleção para escolher o produto vendido.',options=['ZapFlow com Gemini','ZapFlow com chatGPT','ZapFlow com Llama3.0'])

    if st.button('Salvar'):
        try:  
            data_hora = datetime.combine(data,hora)
            venda = Vendas(
                email = email,
                data = data_hora,
                valor = valor,
                quantidade = quantidade,
                produto = produto
            )
            st.write(venda)
        except ValidationError as e:
            st.error(f'Deu erro {e}')




if __name__=='__main__':
    main()