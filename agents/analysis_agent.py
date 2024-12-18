from utils.logger import *
from utils.promt_templates import ANALYSIS_PROMPT, LEAST_TO_MOST_SUBQUESTIONS_PROMPT, \
    LEAST_TO_MOST_SUBQUESTION_ANSWER_PROMPT, LEAST_TO_MOST_FINAL_ANSWER_PROMPT, FINAL_ANSWER_REORGANIZATION_PROMPT, \
    SELF_TEST_MAIN_POINTS_PROMPT, SELF_TEST_ACCURACY_PROMPT, SELF_TEST_CLARITY_PROMPT, FINAL_ANSWER_REFINEMENT_PROMPT, \
    FINAL_ANSWER_REFINEMENT_PROMPT_2
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_experimental.utilities import PythonREPL
from langchain.tools import StructuredTool
python_repl = PythonREPL()
import re


class analysis_agent:

    def __init__(self, config: dict):

        self.config = config
        self.llm = AzureChatOpenAI(
            api_version=config["analysis"]["api-version"],
            deployment_name=config["analysis"]["model"],
            model_name=config["analysis"]["model"],
            temperature=config["analysis"]["temperature"],
            max_tokens=config["analysis"]["max_tokens"],
        )

    def giveFinalAnswer(self, question: str, chunks: list[Chunk], subquestions: list[Subquestion], log: bool = True) -> str:

        if self.config["analysis"]["prompting_technique"] == "direct":
            answer = self.giveFinalAnswerDirectPrompting(question, chunks, subquestions, log)
        elif self.config["analysis"]["prompting_technique"] == "least-to-most":
            answer = self.giveFinalAnswerLeastToMost(question, chunks, subquestions, log)
        elif self.config["analysis"]["prompting_technique"] == "self-eval":
            answer = self.giveFinalAnswerWithSelfCheck(question, chunks, subquestions, log)
        else:
            raise ValueError("Invalid prompting technique")

        return answer

    def giveFinalAnswerDirectPrompting(self, question: str, chunks: list[Chunk], subquestions: list[Subquestion], log: bool = True) -> str:
        if log: logChunks(f"Chunks for final answer ({len(chunks)})", chunks)

        # Analyze the chunks and give the final answer
        retrieved_information = ""
        for subquestion, chunk in zip(subquestions, chunks):
            # Add the chunk to the retrieved information in new lines
            context_enhancement = "Retrieved information for '" + subquestion.question + "':\n"
            retrieved_information += (context_enhancement if self.config['analysis']['context_enhancement'] else "") + chunk.data + "\n"

        answer = self._get_final_answer_initial_with_calculator(question, retrieved_information)
        return answer

    def giveFinalAnswerLeastToMost(self, question: str, chunks: list[Chunk], subquestions: list[Subquestion], log: bool = True) -> str:
        if log: logChunks(f"Chunks for final answer ({len(chunks)})", chunks)

        # Create the retrieved information
        retrieved_information = ""
        for subquestion, chunk in zip(subquestions, chunks):
            # Add the chunk to the retrieved information in new lines
            retrieved_information += f"{chunk.data}\n"

        ltm_subquestions = self._get_least_to_most_subquestions(question, retrieved_information)
        if log: logLeastToMostSubquestions(ltm_subquestions)

        ltm_subquestion_answers = []
        current_context = retrieved_information

        for i, subquestion in enumerate(ltm_subquestions):
            answer = self._get_answer_for_least_to_most_subquestion(subquestion, current_context)
            ltm_subquestion_answers.append(answer)
            current_context += f"\n\nSubquestion: {subquestion}\n\nAnswer: {answer}\n\n"
            if log: logLeastToMostSubquestionWithAnswer(subquestion, answer, i)

        final_answer = self._get_least_to_most_final_answer_with_calculator_agent(question, current_context)
        if log: logFinalAnswer(final_answer)
        reorginized_final_answer = final_answer # self._reorganize_final_answer(final_answer) TODO: reorganize final answer
        return reorginized_final_answer, current_context  # TODO remove current_context after testing

    def giveFinalAnswerWithSelfCheck(self, question: str, chunks: list[Chunk], subquestions: list[Subquestion], log: bool = True) -> str:
        if log: logChunks(f"Chunks for final answer ({len(chunks)})", chunks)

        # Analyze the chunks and give the final answer
        retrieved_information = ""
        for subquestion, chunk in zip(subquestions, chunks):
            # Add the chunk to the retrieved information in new lines
            context_enhancement = "Retrieved information for '" + subquestion.question + "':\n"
            retrieved_information += (context_enhancement if self.config['analysis']['context_enhancement'] else "") + chunk.data + "\n"

        answer = self._get_final_answer_initial_with_calculator(question, retrieved_information)
        combined_output, average_score, refinements = self._self_test(question, retrieved_information, answer)

        logFinalAnswer(answer)
        logSelfEval(combined_output)

        print("REFINEMENTS: ", refinements)

        refinement_counter = 0
        while average_score < self.config["analysis"]["self-test-threshold"] and refinement_counter < self.config["analysis"]["max_refinement_steps"]:
            print(f"Average score: {average_score}   Threshold: {self.config['analysis']['self-test-threshold']}")
            print("The answer is not good enough. Trying to improve it.")
            #answer = self._get_final_answer_retry(question, retrieved_information, answer, combined_output)
            answer = self._get_final_answer_retry_2(answer, refinements) # TODO: Maybe include context so that the model does not hallucinate
            combined_output, average_score, refinements = self._self_test(question, retrieved_information, answer)
            logFinalAnswer(answer)
            logSelfEval(combined_output)
            print("REFINEMENTS: ", refinements)
            refinement_counter += 1

        print("Final score: ", average_score)

        return answer


    ####################################################################################################
    #
    #    Private methods
    #
    ####################################################################################################

    # Direct prompting

    def _get_final_answer_chain(self):

        # Prompt
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", ANALYSIS_PROMPT),
                ("human", "{retrieved_information}\n Question: {question}"),
            ]
        )

        return prompt | self.llm | StrOutputParser()

    def _get_final_answer_initial_with_calculator(self, question: str, retrieved_information: str):

        # Prompt
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", ANALYSIS_PROMPT),
                ("human", "{retrieved_information}\n Question: {question}"),
                ("placeholder", "{agent_scratchpad}"),
            ]
        )

        tools = [self._get_calculator_tool()]
        agent = create_tool_calling_agent(self.llm, tools, prompt)

        return AgentExecutor(agent=agent, tools=tools, verbose=False).invoke({"question": question, "retrieved_information": retrieved_information, "language": self.config["general"]["language"]})['output']

    def _get_calculator_tool(self):
        class CalculatorInput(BaseModel):
            math_expression: str = Field(
                description="A methematical expression you want to calculate. Must be written in Python syntax. The expression will be wrapped by a print statement."
            )

        def calculator(math_expression) -> str:
            command = f"print({math_expression})"
            return python_repl.run(command)

        calculator_tool = StructuredTool.from_function(
            func=calculator,
            name="calculator",
            description="Returns the answer to mathematical expressions.",
            args_schema=CalculatorInput,
        )

        return calculator_tool


    # Least to most prompting

    def _get_least_to_most_subquestions(self, question: str, retrieved_information: str) -> list[str]:

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", LEAST_TO_MOST_SUBQUESTIONS_PROMPT),
                ("human", "Information: {retrieved_information}\n Question: {question}"),
            ]
        )

        chain = prompt | self.llm | StrOutputParser()

        output = chain.invoke({"question": question, "retrieved_information": retrieved_information, "language": self.config["general"]["language"]})

        question_pattern = re.compile(r'Subquestion: "(.*?)"')
        parsed_output = question_pattern.findall(output)

        return parsed_output

    def _get_answer_for_least_to_most_subquestion(self, subquestion: str, current_context: str) -> str:

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", LEAST_TO_MOST_SUBQUESTION_ANSWER_PROMPT),
                ("human", "{current_context}\n Question: {subquestion}"),
            ]
        )

        chain = prompt | self.llm | StrOutputParser()

        return chain.invoke({"subquestion": subquestion, "current_context": current_context, "language": self.config["general"]["language"]})

    def _get_least_to_most_final_answer(self, question: str, current_context: str) -> str:

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", LEAST_TO_MOST_FINAL_ANSWER_PROMPT),
                ("human", "{current_context}\n Question: {question}"),
            ]
        )

        chain = prompt | self.llm | StrOutputParser()

        return chain.invoke({"question": question, "current_context": current_context, "language": self.config["general"]["language"]})

    def _get_least_to_most_final_answer_with_calculator_agent(self, question: str, current_context: str) -> str:

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", LEAST_TO_MOST_FINAL_ANSWER_PROMPT),
                ("human", "{current_context}\n Question: {question}"),
                ("placeholder", "{agent_scratchpad}"),
            ]
        )

        tools = [self._get_calculator_tool()]
        agent = create_tool_calling_agent(self.llm, tools, prompt)

        return AgentExecutor(agent=agent, tools=tools, verbose=False).invoke({"question": question, "current_context": current_context, "language": self.config["general"]["language"]})['output']

    def _reorganize_final_answer(self, final_answer: str) -> str:

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", FINAL_ANSWER_REORGANIZATION_PROMPT),
                ("human", "Original Answer: {final_answer}\n Summary:"),
            ]
        )

        chain = prompt | self.llm | StrOutputParser()
        return chain.invoke({"final_answer": final_answer})


    # Self check prompting

    def _get_final_answer_retry(self, question: str, retrieved_information: str, last_answer: str, justifications: str):

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", FINAL_ANSWER_REFINEMENT_PROMPT),
                ("human", "Question: {question} \n Preliminary answer: {answer} \n relevant context information: {retrieved_information} \n Rating: {rating}"),
                ("placeholder", "{agent_scratchpad}"),
            ]
        )

        tools = [self._get_calculator_tool()]
        agent = create_tool_calling_agent(self.llm, tools, prompt)

        return AgentExecutor(agent=agent, tools=tools, verbose=False).invoke({"question": question, "retrieved_information": retrieved_information,
                                                                              "answer": last_answer, "rating": justifications,
                                                                              "language": self.config["general"]["language"]})['output']

    def _get_final_answer_retry_2(self, last_answer: str, instructions: str):

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", FINAL_ANSWER_REFINEMENT_PROMPT_2),
                ("human", "Preliminary Answer: {answer} \n Instructions: {instructions}"),
                ("placeholder", "{agent_scratchpad}"),
            ]
        )

        tools = [self._get_calculator_tool()]
        agent = create_tool_calling_agent(self.llm, tools, prompt)

        return AgentExecutor(agent=agent, tools=tools, verbose=False).invoke({"answer": last_answer, "instructions": instructions})['output']

    def _self_test(self, question: str, context: str, answer: str):

        main_points_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", SELF_TEST_MAIN_POINTS_PROMPT),
                ("human", "Question: {question}\n Answer: {answer}"),
            ]
        )

        accuracy_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", SELF_TEST_ACCURACY_PROMPT),
                ("human", "Question: {question}\n Context: {context}\n Answer: {answer}"),
            ]
        )

        clarity_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", SELF_TEST_CLARITY_PROMPT),
                ("human", "Answer: {answer}"),
            ]
        )

        main_points_chain = main_points_prompt | self.llm | StrOutputParser()
        accuracy_chain = accuracy_prompt | self.llm | StrOutputParser()
        clarity_chain = clarity_prompt | self.llm | StrOutputParser()

        main_points_output = main_points_chain.invoke({"question": question, "answer": answer})
        accuracy_output = accuracy_chain.invoke({"question": question, "context": context, "answer": answer})
        clarity_output = clarity_chain.invoke({"answer": answer})

        logSelfEval(main_points_output)
        logSelfEval(accuracy_output)
        logSelfEval(clarity_output)

        main_points_score = float(re.compile(r'Score:\s*"(\d+(?:\.\d+)?)"').findall(main_points_output)[-1])
        accuracy_score = float(re.compile(r'Score:\s*"(\d+(?:\.\d+)?)"').findall(accuracy_output)[-1])
        clarity_score = float(re.compile(r'Score:\s*"(\d+(?:\.\d+)?)"').findall(clarity_output)[-1])

        main_points_refinement = re.compile(r'Refinements:\s*"(.*)"').findall(main_points_output)[-1]
        accuracy_refinement = re.compile(r'Refinements:\s*"(.*)"').findall(accuracy_output)[-1]
        clarity_refinement = re.compile(r'Refinements:\s*"(.*)"').findall(clarity_output)[-1]

        average_score = (main_points_score + accuracy_score + clarity_score) / 3

        combined_output = f"Main Points Evaluation:\n{main_points_output}\n\nAccuracy Evaluation:\n{accuracy_output}\n\nClarity Evaluation:\n{clarity_output}"
        combined_refinement = f"Main Points Refinement:\n{main_points_refinement}\n\nAccuracy Refinement:\n{accuracy_refinement}\n\nClarity Refinement:\n{clarity_refinement}"

        return combined_output, average_score, combined_refinement

