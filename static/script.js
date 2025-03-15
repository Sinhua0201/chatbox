function sendMessage() {
    let userInput = document.getElementById("user-input");
    let chatBox = document.getElementById("chat-box");

    if (userInput.value.trim() === "") return;

    // 显示用户消息
    let userMessage = document.createElement("div");
    userMessage.classList.add("user-message");
    userMessage.innerText = userInput.value;
    chatBox.appendChild(userMessage);

    // 清空输入框
    let messageText = userInput.value;
    userInput.value = "";

    // 发送请求到后端
    fetch("/ask", {
        method: "POST",
        body: JSON.stringify({ message: messageText }),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        // 显示 AI 回复
        let botMessage = document.createElement("div");
        botMessage.classList.add("bot-message");
        botMessage.innerText = data.response;
        chatBox.appendChild(botMessage);

        // 滚动到底部
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}
