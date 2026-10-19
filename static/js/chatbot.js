document.addEventListener("DOMContentLoaded", () => {
    const widget = document.querySelector(".koncepts-chat");
    if (!widget) return;

    const launcher = widget.querySelector(".koncepts-chat__launcher");
    const panel = widget.querySelector(".koncepts-chat__panel");
    const closeButton = widget.querySelector(".koncepts-chat__close");
    const messages = widget.querySelector(".koncepts-chat__messages");
    const form = widget.querySelector(".koncepts-chat__form");
    const input = widget.querySelector("#koncepts-chat-input");
    const sendButton = form.querySelector("button[type='submit']");
    const csrfToken = form.querySelector("[name='csrfmiddlewaretoken']").value;
    const inquiryForm = widget.querySelector(".koncepts-chat__inquiry");
    const conversation = { id: null };
    const whatsappButton = widget.querySelector("[data-whatsapp]");

    const setOpen = (open) => {
        panel.hidden = !open;
        launcher.setAttribute("aria-expanded", String(open));
        if (open) input.focus();
        else launcher.focus();
    };

    const addMessage = (text, sender, link, linkLabel) => {
        const bubble = document.createElement("div");
        bubble.className = `koncepts-chat__message koncepts-chat__message--${sender}`;
        bubble.textContent = text;
        if (link && link.startsWith("/") && !link.startsWith("//")) {
            const anchor = document.createElement("a");
            anchor.className = "koncepts-chat__reply-link";
            anchor.href = link;
            anchor.textContent = linkLabel || "Learn more";
            bubble.append(document.createElement("br"), anchor);
        }
        messages.appendChild(bubble);
        messages.scrollTop = messages.scrollHeight;
        return bubble;
    };

    const sendMessage = async (message) => {
        const cleanMessage = message.trim();
        if (!cleanMessage) return;

        addMessage(cleanMessage, "user");
        input.value = "";
        input.disabled = true;
        sendButton.disabled = true;
        const pending = addMessage("One moment...", "bot");

        try {
            const response = await fetch(widget.dataset.endpoint, {
                method: "POST",
                credentials: "same-origin",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken,
                    "X-Requested-With": "XMLHttpRequest",
                },
                body: JSON.stringify({ message: cleanMessage, conversation_id: conversation.id, page: location.pathname.slice(0, 180) }),
            });
            const data = await response.json();
            if (!response.ok) {
                pending.textContent = data.reply || "Please try again.";
                return;
            }
            pending.remove();
            conversation.id = data.conversation_id || conversation.id;
            addMessage(data.reply, "bot", data.link, data.link_label);
        } catch (error) {
            pending.textContent = error.message || "I couldn't send that just now. Please try again or use our contact form.";
        } finally {
            input.disabled = false;
            sendButton.disabled = false;
            input.focus();
        }
    };

    launcher.addEventListener("click", () => setOpen(panel.hidden));
    closeButton.addEventListener("click", () => setOpen(false));
    form.addEventListener("submit", (event) => {
        event.preventDefault();
        sendMessage(input.value);
    });
    widget.querySelectorAll("[data-message]").forEach((button) => {
        button.addEventListener("click", () => sendMessage(button.dataset.message));
    });
    widget.querySelector("[data-show-inquiry]").addEventListener("click", () => {
        inquiryForm.hidden = !inquiryForm.hidden;
        if (!inquiryForm.hidden) inquiryForm.querySelector("[name='full_name']").focus();
        messages.scrollTop = messages.scrollHeight;
    });
    const waNumber = (widget.dataset.whatsapp || "").replace(/[^0-9]/g, "");
    if (waNumber.length >= 8 && waNumber.length <= 15) {
        whatsappButton.hidden = false;
        whatsappButton.addEventListener("click", () => {
            const brief = [...messages.querySelectorAll(".koncepts-chat__message--user")].map((item) => item.textContent).slice(-3).join("; ");
            const message = brief ? `Hello Nine Eight Koncepts, I’d like to discuss: ${brief}` : "Hello Nine Eight Koncepts, I’d like to discuss a project.";
            window.open(`https://wa.me/${waNumber}?text=${encodeURIComponent(message)}`, "_blank", "noopener,noreferrer");
        });
    }
    inquiryForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const submit = inquiryForm.querySelector("button[type='submit']");
        const status = inquiryForm.querySelector(".koncepts-chat__inquiry-status");
        submit.disabled = true;
        status.textContent = "Sending your inquiry…";
        const data = Object.fromEntries(new FormData(inquiryForm).entries());
        data.consent = inquiryForm.elements.consent.checked;
        data.conversation_id = conversation.id;
        data.submission_token = crypto.randomUUID();
        try {
            const response = await fetch(widget.dataset.inquiryEndpoint, { method: "POST", credentials: "same-origin", headers: { "Content-Type": "application/json", "X-CSRFToken": csrfToken }, body: JSON.stringify(data) });
            const result = await response.json();
            if (!response.ok) throw new Error(result.error || "Could not submit. Please try again.");
            status.textContent = `${result.message} Reference #${result.reference}.`;
            inquiryForm.reset();
        } catch (error) { status.textContent = error.message || "Connection issue. Please use the contact page."; }
        finally { submit.disabled = false; }
    });
    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape" && !panel.hidden) setOpen(false);
    });
});
