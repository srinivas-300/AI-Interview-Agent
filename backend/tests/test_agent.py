from judgeval import JudgmentClient
from judgeval.data import Example
from judgeval.scorers import FaithfulnessScorer
from app.services.agent_service import run_tool_augmented_agent

# Setup the JudgeVal client
client = JudgmentClient()

# Define your test question and retrieval context (expected reference knowledge)
task = "Tell me about tesla"
retrieval = ["Tesla, Inc. is an American electric vehicle (EV) and clean energy company headquartered in Palo Alto, California (formerly based in Austin, Texas for a period). Founded in 2003, it's known primarily for revolutionizing the EV market and accelerating the world’s transition to sustainable energy."]

# Run your tool-augmented agent
output = run_tool_augmented_agent(task)

# Create the evaluation example
example = Example(
    input=task,
    actual_output=output,
    retrieval_context=retrieval,
)

# Choose a scorer (you can add more later)
scorer = FaithfulnessScorer(threshold=0.5)

# Run the test – this will raise AssertionError if the threshold isn't met
client.assert_test(
    examples=[example],
    scorers=[scorer],
    model="gpt-4.1-nano-2025-04-14",
    project_name="tool-agent-eval"
)
