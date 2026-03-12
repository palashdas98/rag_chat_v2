####################################################################################################################
#
# Web Interface
#
####################################################################################################################
# Initialise Gradio
# PDF Upload Section
# Question - Answer - Chat Interface
# Logs - Errors Capturing Screen

# Step 1.1 - Initialise Gradio
CREATE Gradio interface

DISPLAY title:
    "Multimodal Multi-Document RAG"


# Step 1.2 - PDF Upload Section
CREATE file upload widget

CREATE button "Upload & Embed"

CREATE textbox to display upload status

WHEN button clicked
    RUN upload_pdf()


# Step 1.3 Chat Interface
CREATE textbox for user question

CREATE button "Get Answers"

CREATE textbox for answer output

WHEN button clicked
    RUN get_answers()


# Step 1.3 Launch the Application
START web application
OPEN interface in browser









####################################################################################################################
#
# Front End Utilities
#
####################################################################################################################

# Step 2.1 - Intialise Libraries

# Step 2.2 - PDF Upload Section
CREATE file upload widget

CREATE button "Upload & Embed"

CREATE textbox to display upload status

WHEN button clicked
    RUN upload_pdf()



####################################################################################################################
#
# APPENDIX 1 - Libraries
#
####################################################################################################################

# Gradio
# pathlib


####################################################################################################################
#
# APPENDIX 2 - LLMs USED
#
####################################################################################################################

# ibm-granite/granite-embedding-30m-english
# ibm-granite/granite-3.2-8b-instruct
# ibm-granite/granite-vision-3.2-2b


####################################################################################################################
#
# APPENDIX 3 - Prompt Templates
#
####################################################################################################################

# Keeping the context in mind that is generated from my vector searches try to answer my questions concisely
# keep the answers brief and to the point 
# remeber the following rules at all poitns of time 
#
# Rule 1 - do not hallucinate or make up facts
# Rule 2 - if you can not find answers in teh context, reply with "Unknown"
# Rule 3 - always reply in a strict json format

# Context:
# Question:
# Answer:


# Gaurd Rail Prompt Template
# Read the following question from my user and try to answer with three options alone - the options are 
# 1. Relevant
# 2. Irrelevant 
# 3. Unknown

# You will only answer questions about automotive engineering fundamentals 
# You will only answer questions that are related to learning about this particular domain 
# You will not answer quesitons that are more technical, more into embedded systems 