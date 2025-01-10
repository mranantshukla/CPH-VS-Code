const { exec } = require("child_process");
const path = require("path");

async function fetchProblem(url) {
    return new Promise((resolve, reject) => {
        const scriptPath = path.resolve(__dirname, "../src/backend/fetch_problem.py");

        exec(`python3 ${scriptPath} "${url}"`, (error, stdout, stderr) => {
            if (error) {
                return reject(new Error(stderr || error.message));
            }
            resolve(stdout.trim());
        });
    });
}

module.exports = {
    fetchProblem,
};

