#!/usr/bin/env python
import sys
from automating_rfp_evaluation_for_consulting_firms.crew import AutomatingRfpEvaluationForConsultingFirmsCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


def run():
    """
    Run the crew.
    """
    inputs = {
        'document_folder_path': '/Users/csacco/Desktop/PolitecnicoMilano'
    }
    AutomatingRfpEvaluationForConsultingFirmsCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'document_folder_path': '/Users/csacco/Desktop/PolitecnicoMilano'
    }
    try:
        AutomatingRfpEvaluationForConsultingFirmsCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AutomatingRfpEvaluationForConsultingFirmsCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    inputs = {
        'document_folder_path': '/Users/csacco/Desktop/PolitecnicoMilano'
    }
    crew = AutomatingRfpEvaluationForConsultingFirmsCrew().crew()
    crew.test(
        n_iterations=int(sys.argv[1]),
        openai_model_name=sys.argv[2],
        inputs=inputs
    )

# ------------------------------------------------------------------
# entry-point CLI — deve finire con i ":"  e avere il blocco indentato
# ------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <n_iterations> <openai_model_name>")
        sys.exit(1)
    test()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
