import streamlit as st
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Ollama model setup (local LLM)
llm = Ollama(model="llama3.2")

# Define a prompt template for test case generation
prompt_template = PromptTemplate(
    input_variables=["requirement"],
    template="""
You are a software quality assurance engineer.

Given the following file:

"{requirement}"

Generate a set of structured test cases, including:
- Test Case ID
- Test Description
- Reason for Test Case
- Preconditions
- Test Steps
- Expected Results

Return the test cases, test scripts and testing data in markdown table format and generate detailed unit test cases using pytest for the following python code:\n\n {requirement}.


[INSTRUCTIONS]
- Respond only with the most relevant, concise, and helpful information.
- Always provide neutral, inclusive, and non-discriminatory language.
- Avoid giving speculative, unverified, or potentially harmful information.
- Ensure you do not reference personal data or engage in discussions that violate privacy.

[VERY IMPORTANT INSTRUCTION]
STRICTLY Generate only test cases, test scripts using pytest and testing data

"""
)

# Wrap LLM with prompt
chain = LLMChain(llm=llm, prompt=prompt_template)

# Streamlit UI

st.title("QA Test Case Generator")

uploaded_file = st.file_uploader("Upload a Python code file (.txt)", type=["txt", "py"])

if uploaded_file is not None:
    code = uploaded_file.read().decode("utf-8")

    if st.button("Generate Test Cases"):
        if code:
            with st.spinner("Generating test cases..."):
                result = chain.run(requirement=code)
                st.markdown(result)
        else:
            st.warning("Invalid data")



