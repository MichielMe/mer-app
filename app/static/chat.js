const form = document.querySelector("#chat-form");
const chatlog = document.querySelector("#chat-log");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  // Get the user's message from the form
  const message = form.elements.message.value;
  
  // Append the user message to the chatlog
  const userMessageElement = document.createElement("div");
  userMessageElement.classList.add("chat-message", "user-message", "bg-blue-500", "text-white", "rounded-md", "px-4", "py-2", "mt-2", "shadow-md", "ml-auto", "mr-2", "justify-self-end", "inline-block");
  userMessageElement.textContent = message;
  chatlog.appendChild(userMessageElement);

  // Clear the input message
  form.elements.message.value = "";

  // Send a request to the Flask server with the user's message
  const response = await fetch("/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ messages: [{ role: "user", content: message }] }),
  });

  // Create a new TextDecoder to decode the streamed response text
  const decoder = new TextDecoder();

  // Set up a new ReadableStream to read the response body
  const reader = response.body.getReader();
  let chunks = "";

  // Placeholder for the bot message bubble
  let botMessageElement;

  // Read the response stream as chunks and append them to the chat log
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    
    const chunkText = decoder.decode(value);
    chunks += chunkText;

    if (!botMessageElement) {
        // If the bot message bubble doesn't exist, create it
        botMessageElement = document.createElement("div");
        botMessageElement.classList.add("chat-message", "bot-message", "bg-gray-300", "rounded-md", "px-4", "py-2", "mt-2", "shadow-md", "mr-auto", "ml-2", "justify-self-start", "inline-block");
        chatlog.appendChild(botMessageElement);
    }

    // Append the chunk text to the bot message bubble
    botMessageElement.textContent += chunkText;
  }
});