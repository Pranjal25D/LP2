# 🤖 Expert System for Information Management
import re

def expert_system():
    knowledge_base = {
        "policies": "Organizational policies can be found in the HR section of the intranet.",
        "leave": "You can apply for leave through the HR portal under the 'Leave' section.",
        "project": "To check project status, refer to the project dashboard or consult your manager.",
        "training": "Training schedules are posted weekly on the LMS portal.",
        "payroll": "Payroll and salary slips are accessible from your employee account dashboard.",
        "benefits": "Employee benefits information is listed in the HR portal under 'Compensation & Benefits'.",
        "support": "For IT support, raise a ticket on the internal support portal."
    }

    print("\nWelcome to the Information Management Expert System!\nType 'exit' to end the session.")

    while True:
        user_query = input("\nAsk your query: ").strip().lower()
        if user_query == "exit":
            print("\nThank you for using the Expert System. Goodbye!")
            break

        found = False
        for key, response in knowledge_base.items():
            if re.search(key, user_query):
                print(f"\nResponse: {response}")
                found = True
                break

        if not found:
            print("\nResponse: Sorry, I couldn't find an answer to that. Please contact the admin or HR.")

# Run the system
if __name__ == '__main__':
    expert_system()