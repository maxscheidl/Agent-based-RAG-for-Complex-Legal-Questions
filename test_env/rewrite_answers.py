# %%
from datetime import datetime

import pandas as pd
import sys
import yaml
from utils.promt_templates import REWRITE_ANSWER_PROMPT
from dotenv import load_dotenv

sys.path.append('../')
load_dotenv()

# %%
with open("../config.yaml", "r") as file:
    config = yaml.safe_load(file)
# %%
data = pd.read_csv('cleaned_examples.csv')
# %%
data["Answer from database"][0]
# %%
print(data["Answer from database"][5])
# %%
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser
# %%
llm = AzureChatOpenAI(
    api_version=config["analysis"]["api-version"],
    deployment_name=config["analysis"]["model"],
    model_name=config["analysis"]["model"],
    temperature=config["analysis"]["temperature"],
    max_tokens=config["analysis"]["max_tokens"],
)
# %%
def rewrite_answer(answer: str) -> str:
    
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", REWRITE_ANSWER_PROMPT),
            ("human", "Original Answer: {original_answer}\n Synthetic Answer:"),
        ]
    )

    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"original_answer": answer})
# %%
new_answer = rewrite_answer(data["Answer from database"][5])
# %%
print(new_answer)
# %%
REWRITE_ANSWER_PROMPT
# %%
data["Answer from database"][0]
# %%
len(data["Answer from database"])
# %%
synthetic_answers = []
for i, answer in enumerate(data["Answer from database"]):
    print(f"Processing Answer {i + 1}")
    synthetic_answer = rewrite_answer(answer)
    synthetic_answers.append(synthetic_answer)

# save synthetic answers to a new csv file called synthetic_answers.csv
data["Synthetic Answer"] = synthetic_answers
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
data.to_csv(f'synthetic_answers.csv', index=False)
# %%