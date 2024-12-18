from utils.logger import logResearchPlan
from utils.promt_templates import PLANNING_PROMPT
from classes.subquestion import Subquestion
import re
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser


class planner_agent:

    def __init__(self, config: dict):

        self.config = config
        self.llm = AzureChatOpenAI(
            api_version=config["planner"]["api-version"],
            deployment_name=config["planner"]["model"],
            model_name=config["planner"]["model"],
            temperature=config["planner"]["temperature"],
            max_tokens=config["planner"]["max_tokens"],
        )

    def splitQuestionIntoSubquestions(self, question: str) -> list[Subquestion]:

        # Generate the research plan
        chain = self._get_planning_chain()
        research_plan = chain.invoke({"question": question, "language": 'english'})
        logResearchPlan(research_plan)

        # Parse answer to get the subquestions
        subquestions = self._parseAnswer(research_plan)

        # Return the subquestions
        return subquestions


    ####################################################################################################
    #
    #    Private methods
    #
    ####################################################################################################

    def _parse_string(self, input_string: str) -> dict | None:

        # List of valid Hierarchy values
        hierarchy_values = ['BL', 'BS', 'GR', 'LU', 'SH', 'SZ', 'UR', 'ZG', 'ZH']

        # Regular expression to match Jurisdiction and optional Hierarchy part
        regex = r"Jurisdiction\s+equal\s+(Federal|Cantonal)(?:\s+and\s+Hierarchy\s+equal\s+(.+))?"

        # Find matches using the regex
        match = re.match(regex, input_string)

        if match:
            result = {}
            # Extract Jurisdiction
            result['Jurisdiction'] = match.group(1)

            # Extract Hierarchy if Jurisdiction is Cantonal
            if match.group(1) == 'Cantonal' and match.group(2):
                hierarchy_str = match.group(2)
                # Match the hierarchy keywords in the string (not necessarily separated by /)
                hierarchy_list = [h for h in hierarchy_values if h in hierarchy_str]
                if hierarchy_list:
                    result['Hierarchy'] = hierarchy_list

            return result
        else:
            return None

    def _parseAnswer(self, research_plan: str) -> list[Subquestion]:

        # Regex to parse the research questions and their filters
        question_pattern = re.compile(r'Research Question: "(.*?)"')
        filters_pattern = re.compile(r'Filters:\s(.*)')  # Function to parse the input text

        questions = question_pattern.findall(research_plan)
        filters = filters_pattern.findall(research_plan)
        parsed_filters = []
        for filter in filters:
            parsed_filters.append(self._parse_string(filter))
        parsed_objects = [Subquestion(i, q, f) for i, (q, f) in enumerate(zip(questions, parsed_filters))]

        return parsed_objects

    def _get_planning_chain(self):

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", PLANNING_PROMPT),
                ("human", "Question: {question}"),
            ]
        )

        return prompt | self.llm | StrOutputParser()
