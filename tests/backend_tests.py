import unittest
import subprocess

class TestFetchProblem(unittest.TestCase):
    def test_fetch_problem(self):
        # Test the fetching of LeetCode problem
        url = "https://leetcode.com/problems/two-sum/"
        command = ["python3", "src/backend/fetch_problem.py", url]
        
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, "Problem fetching failed")
        self.assertIn("Two Sum", result.stdout, "Problem title not found in output")
    
    def test_invalid_url(self):
        # Test with an invalid URL
        url = "https://invalid-url.com/problem"
        command = ["python3", "src/backend/fetch_problem.py", url]
        
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0, "Error expected for invalid URL")

if __name__ == "__main__":
    unittest.main()

