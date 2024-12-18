from classes.chunk import Chunk
from classes.subquestion import Subquestion
import textwrap

def logText(text: str):
    print(text)


def logHeading(heading: str):
    print()
    print()
    print(f"\033[96m{'=' * 20} {heading} {'=' * 20}\033[0m")
    print()


def logSubHeading(subheading: str):
    print()
    print(f"\033[94m{'-' * 20} {subheading} {'-' * 20}\033[0m")
    print()


def logSubSubHeading(subsubheading: str):
    print(f"{'.' * 20} {subsubheading} {'.' * 20}")


def logQuestion(question: str):
    print()
    print(f"\033[96mQuestion\033[0m")
    print("-" * 200)
    print(textwrap.fill(question, width=200))
    print()

def logQuery(query: str):
    print()
    print(f"\033[96mQuery\033[0m")
    print("-" * 200)
    print(textwrap.fill(query, width=200))
    print()

def logSelfEval(query: str):
    print()
    print(f"\033[96mSelf Evaluation\033[0m")
    print("-" * 200)
    print(textwrap.fill(query, width=200))
    print()

def logResearchPlan(research_plan: str):
    print("\n\033[96mResearch Plan\033[0m")
    print("-" * 200)
    print(research_plan)
    print()


def logSubquestionProcessingStart(subquestion: Subquestion):
    print()
    print(f"\n\033[96mProcessing subquestion: {subquestion.id}\033[0m")
    print("-" * 200)
    print(f"\033[94m- Question:\t \033[0m{subquestion.question}")
    print(f"\033[94m- Filters:\t \033[0m{subquestion.filters}")
    print()


def logChunks(heading: str, chunks: list[Chunk]):
    print(f"\033[94m{heading}\033[0m")
    for chunk in chunks:
        print(f"- {chunk}")
    print()


def logFinalAnswer(final_answer: str):
    print(f"\n\033[96mFinal Answer:\033[0m")
    print("-" * 200)
    print(final_answer)
    print()

def logRankedChunks(chunks: list[Chunk], highlightTopK: int):
    print(f"\033[94mChunks reranked and sorted (top {highlightTopK} selected)\033[0m")
    for i, chunk in enumerate(chunks):
        if i < highlightTopK:
            print(f"\033[92m+\033[0m (score: {chunk.ranking_score})   {chunk}")
        else:
            print(f"- (score: {chunk.ranking_score})   {chunk}")
    print()

def logLeastToMostSubquestions(subquestions: list[str]):
    print(f"\033[94mLeast to Most Subquestions\033[0m")
    for subquestion in subquestions:
        print(f"- {subquestion}")
    print()

def logLeastToMostSubquestionWithAnswer(subquestion: str, answer: str, i: int):
    print()
    print(f"\033[96mSubquestion {i + 1}:\033[0m {subquestion}")
    print("-" * 200)
    print(f"{answer}")
