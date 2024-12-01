import json
from datetime import datetime

# Define ethical considerations categories and questions
# Each category addresses a critical aspect of data ethics, with multiple questions under each category.
ethical_topics = {
    "Privacy vs Security": [
        # Questions related to balancing user privacy with organizational or societal security needs
        "How should organizations balance individual privacy with the need for security?",
        "What measures can be implemented to protect privacy without compromising security?",
        "What are examples of when privacy and security have conflicted?"
    ],
    "Impact on Marginalized Communities": [
        # Questions exploring how data practices might disproportionately affect underrepresented groups
        "How can data collection practices disproportionately affect marginalized communities?",
        "What steps can be taken to ensure inclusivity and fairness in data analysis?",
        "Are there cases where biased data has caused harm? If so, how could it have been prevented?"
    ],
    "Role of Data Ethics in Technology Development": [
        # Questions on ethical principles in the design and deployment of data technologies
        "What ethical principles should guide the development of data-driven technologies?",
        "How can organizations ensure accountability in the use of AI and machine learning?",
        "What are the consequences of neglecting data ethics in technology development?"
    ]
}

# Function to collect responses from users
def collect_responses():
    """
    Prompts the user to provide responses to each question under each ethical topic.
    Returns:
        - responses: A dictionary containing topics and user-provided answers.
    """
    print("\nExploring Ethical Considerations in Data Privacy...\n")
    responses = {}
    for topic, questions in ethical_topics.items():
        print(f"Topic: {topic}")
        topic_responses = []  # List to store responses for this topic
        for question in questions:
            print(f"\n - {question}")
            response = input("Your response: ").strip()  # Prompt user for their thoughts
            topic_responses.append({"question": question, "response": response})
        responses[topic] = topic_responses  # Save all responses for this topic
        print("\n" + "-" * 50 + "\n")  # Add a visual separator for clarity
    return responses

# Function to generate a summary report
def generate_report(responses):
    """
    Creates a JSON file summarizing the user's responses to the ethical questions.
    Parameters:
        - responses: A dictionary containing the topics and their corresponding responses.
    Returns:
        - report_filename: The name of the generated JSON file.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Current timestamp for unique filename
    report_filename = f"ethical_considerations_summary_{timestamp}.json"  # Construct the filename

    # Save responses to a JSON file
    with open(report_filename, "w") as report_file:
        json.dump(responses, report_file, indent=4)  # Indented for readability

    print(f"\nSummary report generated: {report_filename}")  # Inform the user about the report
    return report_filename

# Function to display a summary of discussions
def display_summary(responses):
    """
    Displays the collected responses in a user-friendly format.
    Parameters:
        - responses: A dictionary containing topics and user responses.
    """
    print("\nSummary of Ethical Considerations:")
    for topic, answers in responses.items():
        print(f"\nTopic: {topic}")  # Display topic name
        for answer in answers:
            print(f" - {answer['question']}")  # Display the question
            print(f"   * {answer['response']}")  # Display the user's response
    print("\n" + "-" * 50 + "\n")  # Add a visual separator for clarity

# Main script execution
if __name__ == "__main__":
    # Collect responses from the user
    responses = collect_responses()
    # Display a summary of the responses
    display_summary(responses)
    # Generate a report and save it as a JSON file
    generate_report(responses)
