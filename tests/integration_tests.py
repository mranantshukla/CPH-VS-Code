import unittest
import subprocess

class TestIntegration(unittest.TestCase):
    def test_full_integration(self):
        url = "https://leetcode.com/problems/two-sum/"
        
        # Step 1: Fetch problem details
        fetch_command = ["python3", "src/backend/fetch_problem.py", url]
        result = subprocess.run(fetch_command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Problem fetching failed")

        # Step 2: Run the solution against fetched test cases
        run_command = ["python3", "src/frontend/run_test_cases.py"]
        result = subprocess.run(run_command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Test case execution failed")
        self.assertIn("Test cases passed", result.stdout, "Test case results not found")

if __name__ == "__main__":
    unittest.main()

