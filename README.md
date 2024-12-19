# Advanced Legal Robot Researcher - Agent-based RAG for Complex Legal Questions

## Abstract
This project investigates the design, implementation, and evalua-
tion of a Retrieval-Augmented Generation (RAG)-based system
tailored for the legal domain. The proposed architecture addresses
the complexity inherent in legal question-answering by decom-
posing questions into sub-components, leveraging a multi-stage
retrieval pipeline to enhance document relevance and applying
advanced prompting techniques for the final answer generation.
To systematically evaluate the system’s performance, we introduce
a novel evaluation framework that assesses key metrics such as
clarity, accuracy, and coverage of main points. Furthermore, various
prompting techniques, namely chain-of-thought prompting, least-
to-most prompting, and self-refinement prompting, are evaluated
for their effectiveness in the final analysis. Our results demonstrate
the effectiveness of our evaluation strategy in reliably assessing
system performance and aligning with expert judgments. Among
the prompting techniques, Self-Refinement Prompting proved to be
the most effective, delivering the highest clarity, accuracy, coverage
and overall score. Lastly, we highlight opportunities for further
improvements in retrieval methods and prompting strategies to
optimize the system’s performance and robustness.
![grafik](https://github.com/user-attachments/assets/0414b2aa-0e55-4da2-9996-30d8e7f891d6)


## Setup
1. Clone this repository and install the required dependencies using requirements.txt
2. Create a .env file with the following variables
  - AZURE_OPENAI_ENDPOINT
  - AZURE_OPENAI_API_KEY
  - AZURE_SEARCH_ENDPOINT
  - AZURE_SEARCH_API_KEY

NOTE: this project was build on top of the infrastructure of EY so you most likely have to adapt the retrieval mechanism for you personal needs

