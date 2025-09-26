  //QUICK QUESTION
     async  function askQuestion(msg) {
           let chatbox = document.getElementById("chatMessages");
            chatbox.innerHTML += "<p class='user'><b>You:</b> " + msg + "</p>";
              let response = await fetch("/ask", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({"message": msg})
            });

             let data = await response.json();
            chatbox.innerHTML += "<p class='bot'><b>Bot:</b> " + data.reply + "</p>";
            chatbox.scrollTop = chatbox.scrollHeight;
            document.getElementById("message").value = "";

       }




        // MANUALLY
         function handleKeyPress(event) {
                if (event.key === 'Enter') {
         sendMessage();
           document.getElementById("message").value = "";
                }}
        async function sendMessage() {
            let msg = document.getElementById("message").value;
            if (!msg) return;

            let chatbox = document.getElementById("chatMessages");
            chatbox.innerHTML += "<p class='user'><b>You:</b> " + msg + "</p>";

            let response = await fetch("/ask", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({"message": msg})
            });

            function handleKeyPress(event) {
                if (event.key === 'Enter') {
                  sendMessage();
         }
}
           
             
            let data = await response.json();
            chatbox.innerHTML += "<p class='bot'><b>Bot:</b> " + data.reply + "</p>";
            chatbox.scrollTop = chatbox.scrollHeight;
            document.getElementById("message").value = "";
        }
