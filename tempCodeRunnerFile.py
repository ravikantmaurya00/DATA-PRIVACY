import os
import json
import datetime

# Define audit categories with a list of questions for each category
# These categories help assess different aspects of data privacy compliance.
audit_criteria = {
    "data_collection": [
        "Are users informed about data collection?",
        "Is data collection limited to what's necessary?",
        "Are consent mechanisms in place?"
    ],
    "data_storage": [
        "Is data encrypted at rest?",
        "Is sensitive data stored securely?",
        "Are backup policies in place?"
    ],
    "data_access": [
        "Is access to data restricted based on roles?",
        "Are access logs maintained and monitored?",
        "Are strong authentication mechanisms used?"
    ],
    "compliance": [
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
    for category, questions in audit_criteria.items():
        print(f"Category: {category.upper()}")
        category_responses = []
        for question in questions:
            # Validate user input to ensure it is either "Yes" or "No"
            response = input(f" - {question} (Yes/No): ").strip().lower()
            while response not in ["yes", "no"]:
                print("Please enter 'Yes' or 'No'.")
                response = input(f" - {question} (Yes/No): ").strip().lower()
            category_responses.append({"question": question, "response": response})
        responses[category] = category_responses
        print("\n")

def analyze_responses():
    """
    Analyzes the collected responses to identify vulnerabilities.
    Returns a dictionary containing the categories and their associated issues.
    """
    print("\nAnalyzing Responses...\n")
    vulnerabilities = {}
    for category, answers in responses.items():
        # Identify questions where the response was "No" as vulnerabilities
        category_vulnerabilities = [item["question"] for item in answers if item["response"] == "no"]
        vulnerabilities[category] = category_vulnerabilities

    return vulnerabilities

def generate_report(vulnerabilities):
    """
    Generates a JSON report with audit results and identified vulnerabilities.
    Saves the report to a file with a timestamped filename.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_filename = f"data_privacy_audit_report_{timestamp}.json"

    report_content = {
        "timestamp": timestamp,
        "audit_results": responses,
        "vulnerabilities": vulnerabilities
    }

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
    for category, issues in vulnerabilities.items():
        print(f" - {category.upper()}: {len(issues)} issues identified.")
        for issue in issues:
            print(f"   * {issue}")

# Main script execution
if __name__ == "__main__":
    collect_responses()  # Collect responses from the user
    vulnerabilities = analyze_responses()  # Analyze responses for vulnerabilities
    display_summary(vulnerabilities)  # Display a summary of findings
    generate_report(vulnerabilities) # Generate a detailed report in JSON format
