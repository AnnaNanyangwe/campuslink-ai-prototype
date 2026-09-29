async function sendMessage() {

    const input =
        document.getElementById("messageInput");

    const messages =
        document.getElementById("messages");

    const message =
        input.value.trim();

    if (!message) {
        return;
    }

    messages.innerHTML += `
        <div class="message user">
            ${message}
        </div>
    `;

    input.value = "";

    messages.innerHTML += `
        <div class="message ai" id="loading">
            Thinking...
        </div>
    `;

    try {

        const response = await fetch(
            "/api/chat",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    message: message
                })
            }
        );

        const data = await response.json();

        document.getElementById("loading").remove();

        if (data.response) {

            messages.innerHTML += `
                <div class="message ai">
                    ${data.response}
                </div>
            `;

        } else {

            messages.innerHTML += `
                <div class="message ai">
                    Something went wrong.
                </div>
            `;
        }

    } catch (error) {

        document.getElementById("loading").remove();

        messages.innerHTML += `
            <div class="message ai">
                Could not connect to the AI service.
            </div>
        `;
    }
}