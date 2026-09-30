async function findMatches() {

    const input = document.getElementById("messageInput");
    const messages = document.getElementById("messages");

    const message = input.value.trim();

    if (!message) {
        return;
    }

    messages.innerHTML = `
        <div class="message user">
            ${message}
        </div>
    `;

    input.value = "";

    messages.innerHTML += `
        <div class="message ai" id="loading">
            Finding relevant opportunities...
        </div>
    `;

    try {

        const response = await fetch("/api/match", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        document.getElementById("loading").remove();

        if (data.matches) {

            let result = `
                <div class="message ai">
                    <strong>CampusLink AI Match</strong><br><br>
            `;

            data.matches.forEach(match => {

                result += `
                    <div style="margin-bottom: 18px;">
                        <strong>${match.title}</strong><br>
                        ${match.description}
                    </div>
                `;

            });

            result += `</div>`;

            messages.innerHTML += result;

        } else {

            messages.innerHTML += `
                <div class="message ai">
                    ${data.error || "No matches found."}
                </div>
            `;
        }

    } catch (error) {

        document.getElementById("loading").remove();

        messages.innerHTML += `
            <div class="message ai">
                Could not connect to CampusLink.
            </div>
        `;
    }
}