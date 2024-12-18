from agents.planner_agent import planner_agent
from agents.retrieval_agent import retrieval_agent
from agents.analysis_agent import analysis_agent
from utils.database import Database
from utils.logger import *


class rag_system:

    def __init__(self, config: dict):

        self.database = Database()
        self.config = config

        self.planner_agent = planner_agent(config)
        self.retrieval_agent = retrieval_agent(config, self.database)
        self.analysis_agent = analysis_agent(config)

    def processQuestion(self, question: str):

        # Split question into subquestions
        logHeading("Planing Phase")
        logQuestion(question)
        subquestions = self.planner_agent.splitQuestionIntoSubquestions(question) if self.config["planner"]["use_subquestions"] else [Subquestion(0, question, {})]

        # Retrieve chunks for each subquestion
        logHeading("Retrieval Phase")
        chunks = []

        for subquestion in subquestions:
            logSubquestionProcessingStart(subquestion)
            subquestion_chunks = self.retrieval_agent.retrieveChunksForSubquestion(subquestion)
            chunks.extend(subquestion_chunks)

        # Give final answer
        logHeading("Generation Phase")
        final_answer = self.analysis_agent.giveFinalAnswer(question, chunks, subquestions)
        logFinalAnswer(final_answer)

        return final_answer, subquestions, chunks
