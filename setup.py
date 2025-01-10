from setuptools import setup, find_packages

setup(
    name="leetcode_test_case_automation",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool to automate fetching and running LeetCode test cases using the CPH VS Code extension.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/leetcode-test-case-automation",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "requests==2.31.0",
        "beautifulsoup4==4.13.0",
        "lxml==4.9.3",
        "pytest==7.4.2",
        "loguru==0.7.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "fetch-problem=backend.fetch_problem:main",
            "run-test-cases=backend.run_test_cases:main"
        ]
    },
)
