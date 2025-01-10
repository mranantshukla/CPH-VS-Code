const vscode = require("vscode");
const { fetchProblem } = require("./commands");

function activate(context) {
    console.log("Extension activated!");

    // Register command to fetch problem
    const fetchProblemCommand = vscode.commands.registerCommand(
        "leetcode-helper.fetchProblem",
        async () => {
            const url = await vscode.window.showInputBox({
                placeHolder: "Enter LeetCode Problem URL",
                prompt: "Fetch problem details and test cases",
            });

            if (!url) {
                vscode.window.showErrorMessage("No URL provided!");
                return;
            }

            try {
                const result = await fetchProblem(url);
                vscode.window.showInformationMessage(result);
            } catch (error) {
                vscode.window.showErrorMessage(`Error: ${error.message}`);
            }
        }
    );

    context.subscriptions.push(fetchProblemCommand);
}

function deactivate() {
    console.log("Extension deactivated!");
}

module.exports = {
    activate,
    deactivate,
};
