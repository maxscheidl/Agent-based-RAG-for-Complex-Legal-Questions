from datetime import datetime

import pandas as pd
import sys
import yaml
from dotenv import load_dotenv
from agents.evaluation_agent import evaluation_agent

load_dotenv()

def run():

    # Load the configuration
    with open("../config.yaml", "r") as file:
        config = yaml.safe_load(file)

    # Set up the evaluation agent
    ev = evaluation_agent(config)

    # Load the examples
    combined = pd.read_csv('../test_env/cleaned_examples.csv')

    # Prepare dataframe for storing the results
    results = pd.DataFrame(columns=[
        'id', 'Question', 'Calculated Rating', 'Actual Rating', 'Predicted Justification', 'Actual Justification'
    ])

    alignments_df = pd.DataFrame(columns=[
        'id', 'Calculated Rating', 'Actual Rating', 'C1 Score', 'C2 Score', 'C3 Score', 'C4 Score',
    ])

    for i, (question, gt, pred, comments, rating, id) in combined.iterrows():

        print(f"Processing Question {i + 1} with id: {id}")

        ave, main_points_score, accuracy_score, clarity_score, mathematical_accuracy_score, reason = ev.evaluate(question, gt, pred)

        # Calculate the final rating
        calculated_rating = float(ave) / 5.0

        # Store the results
        results.loc[i] = [id, question, calculated_rating, rating / 10, reason, comments]
 
        alignments_df.loc[i] = [id, calculated_rating, rating / 10, main_points_score, accuracy_score, clarity_score, mathematical_accuracy_score]

        print(f"Calculated rating: {calculated_rating}     Actual rating: {rating / 10}")

    # Save results with timestamp and in results folder
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    results.to_csv(f'results/score_alignment_{timestamp}.csv', index=False)
    alignments_df.to_csv(f'results/criteria_alignments_{timestamp}.csv', index=False)


if __name__ == "__main__":

    start = datetime.now()  # Start time
    run()
    print(f"Time taken: {datetime.now() - start}")  # End time

