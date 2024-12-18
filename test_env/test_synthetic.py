from datetime import datetime

import pandas as pd
import os
import sys
import yaml
import random
from agents.evaluation_agent import evaluation_agent
from dotenv import load_dotenv
sys.path.append('../')

load_dotenv()

def run():

    # Load the configuration
    with open("../config.yaml", "r") as file:
        config = yaml.safe_load(file)

    # Set up the evaluation agent and the RAG system
    ev = evaluation_agent(config)

    # Load the data
    data = pd.read_csv('synthetic_answers.csv')

    # Prepare dataframe for storing the results
    results_pos = pd.DataFrame(columns=[
        'id', 'Question', 'Reference Answer', 'AI Answer', 'Calculated Rating',
        'Correctness Score', 'Correctness Subscore Main Points', 'Correctness Subscore Accuracy',
        'Correctness Subscore Relevance', 'Correctness Subscore Clarity', 'Correctness Subscore Math',
        'Scoring Justification', 'Faithfulness Score',
    ])

    results_neg = pd.DataFrame(columns=[
        'id', 'Question', 'Reference Answer', 'AI Answer', 'Calculated Rating',
        'Correctness Score', 'Correctness Subscore Main Points', 'Correctness Subscore Accuracy',
        'Correctness Subscore Relevance', 'Correctness Subscore Clarity', 'Correctness Subscore Math',
        'Scoring Justification', 'Faithfulness Score',
    ])

    # for i, (question, gt, pred, comments, rating, id, syn) in data.iterrows():

    #     print(f"Processing Question {i + 1} with id: {id}")

    #     answer = syn
    #     correctness_score, faithfulness_score, scoring, alignments = ev.evaluate(question, gt, answer)

    #     # Store the results
    #     results_pos.loc[i] = [
    #         id, question, gt, answer, correctness_score,
    #         correctness_score, *alignments, scoring,
    #         faithfulness_score
    #     ]

    #     print(f"Calculated rating: {correctness_score}")

    # For negative examples randomly sample a true answer from the dataset that is for a different question

    answers_len = len(data['Answer from database'])
    random.seed(42)

    for i, (question, gt, pred, comments, rating, id, syn) in data.iterrows():

        print(f"Processing Question {i + 1} with id: {id}")

        # sample a random answer from the dataset that is not i'th answer
        random_number = random.choice([num for num in range(0, answers_len) if num != i])
        print(f"Random number: {random_number}")
        print(f"Ground truth: {gt}")
        print(f"Random answer: {data['Answer from database'][random_number]}")
        answer = data['Answer from database'][random_number]

        correctness_score, faithfulness_score, scoring, alignments = ev.evaluate(question, gt, answer)

        # Store the results
        results_neg.loc[i] = [
            id, question, gt, answer, correctness_score,
            correctness_score, *alignments, scoring,
            faithfulness_score
        ]


    # Save results with timestamp and in results folder
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    #results_pos.to_csv(f'results/results_{timestamp}.csv', index=False)
    results_neg.to_csv(f'results/results_negative_{timestamp}.csv', index=False)


if __name__ == "__main__":
   run()






