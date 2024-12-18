from datetime import datetime
import pandas as pd
import sys
import yaml
from dotenv import load_dotenv
from rag_system import rag_system
from agents.evaluation_agent import evaluation_agent

sys.path.append('../')
load_dotenv()




def run():

    # Load the configuration
    with open("../config.yaml", "r") as file:
        config = yaml.safe_load(file)

    # Set up the evaluation agent and the RAG system
    ev = evaluation_agent(config)
    rag = rag_system(config)

    # Load the data
    data = pd.read_csv('cleaned_examples.csv')

    # Prepare dataframe for storing the results
    results = pd.DataFrame(columns=[
        'id', 'Question', 'Reference Answer', 'AI Answer', 'Calculated Rating',
        'Correctness Score', 'Correctness Subscore Main Points', 'Correctness Subscore Accuracy',
        'Correctness Subscore Relevance', 'Correctness Subscore Clarity', 'Correctness Subscore Math',
        'Scoring Justification', 'Faithfulness Score', 'Subquestions', 'Retrieved Context',
    ])

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    for i, (question, gt, pred, comments, rating, id) in data.iterrows():

        print(f"Processing Question {i + 1} with id: {id}")

        answer, subquestions, chunks = rag.processQuestion(question)
        overall_score, main_points_score, accuracy_score, clarity_score, mathematical_accuracy_score, combined_scoring = ev.evaluate(question, gt, answer)

        # Store the results
        results.loc[i] = [
            id, question, gt, answer, overall_score,
            overall_score, main_points_score, accuracy_score, -1, clarity_score, mathematical_accuracy_score, combined_scoring,
            -1, "\n".join([str(sub) for sub in subquestions]), "\n".join([str(c) for c in chunks])
        ]

        # Save after each question
        results.to_csv(f'results/results_{timestamp}.csv', index=False)
        print(f"Calculated rating: {overall_score}")


if __name__ == "__main__":
   run()






