import os

def parse_test_cases(test_cases_str: str):
    """
    Parse raw test case string into structured input and output pairs.
    Args:
        test_cases_str (str): Raw test cases as a string.
    Returns:
        list: List of dictionaries containing inputs and expected outputs.
    """
    test_cases = []
    for case in test_cases_str.split("\n\n"):
        parts = case.strip().split("\n")
        if len(parts) < 2:
            continue
        test_cases.append({
            "input": parts[0].replace("Input: ", "").strip(),
            "output": parts[1].replace("Output: ", "").strip(),
        })
    return test_cases

def save_test_cases(test_cases, directory="tests/test_cases/"):
    """
    Save test cases into input and output text files.
    Args:
        test_cases (list): List of test cases with inputs and outputs.
        directory (str): Directory to save the test case files.
    """
    os.makedirs(directory, exist_ok=True)
    for i, case in enumerate(test_cases, start=1):
        with open(os.path.join(directory, f"input_{i}.txt"), "w") as input_file:
            input_file.write(case["input"])
        with open(os.path.join(directory, f"output_{i}.txt"), "w") as output_file:
            output_file.write(case["output"])

