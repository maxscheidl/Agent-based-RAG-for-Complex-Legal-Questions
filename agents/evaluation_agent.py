import re
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from utils.promt_templates import MAIN_POINTS_PROMPT, ACCURACY_PROMPT, CLARITY_PROMPT, MATHEMATICAL_ACCURACY_PROMPT


class evaluation_agent:

    def __init__(self, config: dict):

        self.config = config
        self.llm = AzureChatOpenAI(
            api_version=config["evaluation"]["agent"]["api-version"],
            deployment_name=config["evaluation"]["agent"]["model"],
            model_name=config["evaluation"]["agent"]["model"],
            temperature=config["evaluation"]["agent"]["temperature"],
            max_tokens=config["evaluation"]["agent"]["max_tokens"],
        )


    def evaluate(self, question: str, expected_answer: str, predicted_answer: str) -> tuple:
            
            # separate evaluation
            main_points_score, accuracy_score, clarity_score, mathematical_accuracy_score, reason = self._separate_evaluation(question, expected_answer, predicted_answer)
    
            if mathematical_accuracy_score < 0.5:
                ave = (main_points_score + accuracy_score + clarity_score) / 3
            else:
                ave = (main_points_score + accuracy_score + clarity_score + mathematical_accuracy_score) / 4

            return ave, main_points_score, accuracy_score, clarity_score, mathematical_accuracy_score, reason


    ####################################################################################################
    #
    #    Private methods
    #
    ####################################################################################################

    def _separate_evaluation(self, question: str, expected_answer: str, predicted_answer: str) -> tuple:
            
            # calculate main points score
            main_points_score, main_points_reason = self._calculate_main_points_score(question, expected_answer, predicted_answer)

            # calculate accuracy score
            accuracy_score, accuracy_reason = self._calculate_accuracy_score(question, expected_answer, predicted_answer)

            # calculate clarity score
            clarity_score, clarity_reason = self._calculate_clarity_score(question, expected_answer, predicted_answer)

            # calculate mathematical accuracy score
            mathematical_accuracy_score, math_reason = self._calculate_mathematical_accuracy_score(question, expected_answer, predicted_answer)

            # Concatenate the reasons with new lines
            reason = main_points_reason + "\n" + accuracy_reason + "\n" + clarity_reason + "\n" + math_reason

            return main_points_score, accuracy_score, clarity_score, mathematical_accuracy_score, reason

    def _calculate_main_points_score(self, question: str, expected_answer: str, predicted_answer: str) -> tuple:

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", MAIN_POINTS_PROMPT),
                ("human",
                 "- Question: {question}\n- Expected Answer: {expected_output}\n- Predicted Answer: {actual_output}"),
            ]
        )

        scoring_chain = prompt | self.llm | StrOutputParser()

        scoring = scoring_chain.invoke({
            "question": question,
            "expected_output": expected_answer,
            "actual_output": predicted_answer
        })

        score = re.compile(r'Score:\s*(\d+(?:\.\d+)?)').findall(scoring)[-1]
        score = float(score)

        return score, scoring

    def _calculate_accuracy_score(self, question: str, expected_answer: str, predicted_answer: str) -> tuple:

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", ACCURACY_PROMPT),
                ("human",
                 "- Question: {question}\n- Expected Answer: {expected_output}\n- Predicted Answer: {actual_output}"),
            ]
        )

        scoring_chain = prompt | self.llm | StrOutputParser()

        scoring = scoring_chain.invoke({
            "question": question,
            "expected_output": expected_answer,
            "actual_output": predicted_answer
        })

        score = re.compile(r'Score:\s*(\d+(?:\.\d+)?)').findall(scoring)[-1]
        score = float(score)

        return score, scoring
    
    def _calculate_clarity_score(self, question: str, expected_answer: str, predicted_answer: str) -> tuple:

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", CLARITY_PROMPT),
                ("human",
                 "- Predicted Answer: {actual_output}"),
            ]
        )

        scoring_chain = prompt | self.llm | StrOutputParser()

        scoring = scoring_chain.invoke({
            "question": question,
            "expected_output": expected_answer,
            "actual_output": predicted_answer
        })

        score = re.compile(r'Score:\s*(\d+(?:\.\d+)?)').findall(scoring)[-1]
        score = float(score)

        return score, scoring
    
    def _calculate_mathematical_accuracy_score(self, question: str, expected_answer: str, predicted_answer: str) -> tuple:

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", MATHEMATICAL_ACCURACY_PROMPT),
                ("human",
                 "- Question: {question}\n- Expected Answer: {expected_output}\n- Predicted Answer: {actual_output}"),
            ]
        )

        scoring_chain = prompt | self.llm | StrOutputParser()

        scoring = scoring_chain.invoke({
            "question": question,
            "expected_output": expected_answer,
            "actual_output": predicted_answer
        })

        score = re.compile(r'Score:\s*(\d+(?:\.\d+)?)').findall(scoring)[-1]
        score = float(score)

        return score, scoring



