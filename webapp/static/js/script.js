function submitBlog(event) {
            event.preventDefault();
            var notificationContainer = document.getElementById("notification-container");
            var speechBubble = document.createElement("div");
            speechBubble.id = "speech-bubble";
            speechBubble.textContent = "Thank you for sharing your advocacy about nature!";
            notificationContainer.appendChild(speechBubble);
            setTimeout(function () {
                speechBubble.remove();
            }, 5000);
        }

  function submitBlogs(event) {
        event.preventDefault();
        var notificationContainer = document.getElementById("notification-container");
        var speechBubble = document.createElement("div");
        speechBubble.id = "speech-bubble";
        speechBubble.textContent = "Thank you for messaging us!";
        notificationContainer.appendChild(speechBubble);
        setTimeout(function () {
            speechBubble.remove();
        }, 5000);
    }

