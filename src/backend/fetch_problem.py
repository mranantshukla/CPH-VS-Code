import requests
import json
from src.backend.utils import parse_test_cases, save_test_cases

def fetch_problem_details(url: str):
    """
    Fetch problem details and test cases from LeetCode problem URL.
    Args:
        url (str): LeetCode problem URL.
    """
    problem_slug = url.rstrip('/').split('/')[-1]
    graphql_url = "https://leetcode.com/graphql/"
    headers = {"Content-Type": "application/json"}
    query = {
        "query": """
        query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                title
                content
                exampleTestcases
            }
        }""",
        "variables": {"titleSlug": problem_slug},
    }

    response = requests.post(graphql_url, headers=headers, data=json.dumps(query))
    if response.status_code != 200:
        raise Exception(f"Failed to fetch problem: {response.text}")

    problem_data = response.json()["data"]["question"]
    test_cases = parse_test_cases(problem_data["exampleTestcases"])
    save_test_cases(test_cases)
    print(f"Fetched problem: {problem_data['title']}")
    print("Test cases saved successfully.")
