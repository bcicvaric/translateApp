import ollama
import streamlit as st

supported_languages = ['English',
                       'Spanish',
                       'French',
                       'German',
                       'Italian',
                       'Portuguese',
                       'Dutch',
                       'Russian',
                       'Chinese',
                       'Japanese',
                       'Korean']


def calc_disclaimer(input_language, output_language):
    if input_language not in supported_languages:
        if output_language not in supported_languages:
            disclaimer = f"""DISCLAIMER: {input_language} and {output_language} are not among
supported languages, so translation might be wacky."""
        else:
            disclaimer = f"""DISCLAIMER: {input_language} is not among supported languages, 
so translation might be wacky."""
    else:
        if output_language not in supported_languages:
            disclaimer = f"""DISCLAIMER: {output_language} is not among supported languages, 
so translation might be wacky."""
        else:
            disclaimer = False

    return disclaimer


def translate_text():

    disclaimer = calc_disclaimer(input_language, output_language)



    response = ollama.chat(model='llama3.1', messages=[
        {
            'role': 'user',
            'content': """
<< SYS >>
You are an expert language translator.
<< / SYS >>
Please translate the text below from {input_language} to {output_language}.
{text}""".format(input_language=input_language, output_language=output_language, text=text)
            ,
        },
    ])

    if disclaimer:
        st.text(disclaimer)

    st.text(response['message']['content'])


st.title("Llama translator")
st.write('Instructions: translate any text to a language of your choosing')
text = st.text_input('Text','Hello, please translate this.')
input_language = st.text_input('Translate from','English')
output_language = st.text_input('Translate to','French')
st.button('Translate!',on_click=translate_text)