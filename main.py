from rag_system import rag_system
import yaml
from dotenv import load_dotenv



# Load the environment variables
load_dotenv()

# Define the question
question = """
Die steuerpflichtige Garage X AG, welche nach der effektiven Methode abrechnet, kauft vom nicht steuerpflichtigen Herrn Müller zwei Personenwagen, welche Herr Müller in den letzten vier Jahren privat benützt hat. Die Garage bezahlt Herrn Müller für den ersten Personenwagen CHF 30’000 und für den zweiten Personenwagen CHF 20’000. Die Garage X AG beabsichtigt, den ersten Personenwagen in der Schweiz als Occasionswagen wieder zu verkaufen. Den zweiten Personenwagen wird die Garage als Transportwagen für ihre Servicewerkstatt, welche ausschließlich steuerbare Umsätze erzielt, einsetzen.

Welche Vorsteuern könnte die Garage beim Kauf der beiden Personenwagen geltend machen? Berechnen Sie den allfälligen Vorsteuerbetrag und begründen Sie Ihre Antwort kurz zusammen mit den entsprechenden Bestimmungen des MWSTG.
"""


def run():

    # Load the configuration
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

    # Initialize the RAG system and process the question
    rag = rag_system(config)
    answer, _, _ = rag.processQuestion(question)


if __name__ == "__main__":
   run()








