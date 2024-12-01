import os
import json
import datetime

# Define audit categories with a list of questions for each category.
# These categories help assess different aspects of data privacy compliance.
audit_criteria = {
    "data_collection": [  # Questions related to data collection practices
        "Are users informed about data collection?",
        "Is data collection limited to what's necessary?",
        "Are consent mechanisms in place?"
    ],
    "data_storage": [  # Questions related to data storage security
        "Is data encrypted at rest?",
        "Is sensitive data stored securely?",
        "Are backup policies in place?"
    ],
    "data_access": [  # Questions related to data access control
        "Is access to data restricted based on roles?",
        "Are access logs maintained and monitored?",
        "Are strong authentication mechanisms used?"
    ],
    "compliance": [  # Questions related to legal and regulatory compliance
        "Is the organization GDPR compliant?",
        "Are data retention policies clearly defined?",
        "Is there a process for handling data subject requests?"
    ]
}

# Dictionary to store the user responses for each audit question
responses = {}

def collect_responses():
    """
    Prompts the user to answer audit questions for each category.
    Stores responses (Yes/No) in the `responses` dictionary.
    """
    print("Starting Data Privacy Audit...\n")
    for category, questions in audit_criteria.items():  # Iterate over each category and questions
        print(f"Category: {category.upper()}")
        category_responses = []
        for question in questions:  # For each question in the category
            # Get user response and ensure it's either 'Yes' or 'No'
            response = input(f" - {question} (Yes/No): ").strip().lower()
            while response not in ["yes", "no"]:  # Validate input
                print("Please enter 'Yes' or 'No'.")
                response = input(f" - {question} (Yes/No): ").strip().lower()
            category_responses.append({"question": question, "response": response})  # Store the response
        responses[category] = category_responses  # Add the responses for the current category
        print("\n")

def analyze_responses():
    """
    Analyzes the collected responses to identify vulnerabilities.
    Returns a dictionary containing the categories and their associated issues.
    """
    print("\nAnalyzing Responses...\n")
    vulnerabilities = {}
    # For each category, identify the questions with a "No" response
    for category, answers in responses.items():
        category_vulnerabilities = [item["question"] for item in answers if item["response"] == "no"]
        vulnerabilities[category] = category_vulnerabilities  # Store the vulnerabilities found in the category

    return vulnerabilities

def generate_report(vulnerabilities):
    """
    Generates a JSON report with audit results and identified vulnerabilities.
    Saves the report to a file with a timestamped filename.
    """
    # Generate a timestamp for the report file name
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_filename = f"data_privacy_audit_report_{timestamp}.json"

    # Prepare the content of the report
    report_content = {
        "timestamp": timestamp,
        "audit_results": responses,  # Include the collected responses
        "vulnerabilities": vulnerabilities  # Include the identified vulnerabilities
    }

    # Write the report content to a JSON file
    with open(report_filename, "w") as report_file:
        json.dump(report_content, report_file, indent=4)

    print(f"\nAudit report generated: {report_filename}")
    return report_filename

def display_summary(vulnerabilities):
    """
    Displays a summary of the findings, including the number of issues identified 
    in each category and the specific questions flagged as vulnerabilities.
    """
    print("\nSummary of Findings:")
    # For each category, display how many issues were identified and list the specific issues
    for category, issues in vulnerabilities.items():
        print(f" - {category.upper()}: {len(issues)} issues identified.")
        for issue in issues:
            print(f"   * {issue}")

# Main script execution
if __name__ == "__main__":
    collect_responses()  # Collect responses from the user
    vulnerabilities = analyze_responses()  # Analyze responses for vulnerabilities
    display_summary(vulnerabilities)  # Display a summary of findings
    generate_report(vulnerabilities)  # Generate a detailed report in JSON format
