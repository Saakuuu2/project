import tkinter as tk
from tkinter import scrolledtext
import time
import threading

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Animated Vibrant Chatbot")

        # Colors for vibrant theme
        self.bg_color = "#222831"  # Dark background
        self.text_color = "#eeeeee"  # Light text
        self.user_color = "#32e0c4"  # User text
        self.bot_color = "#ff5722"  # Bot text
        self.typing_color = "#f4d160"  # Typing indicator
        self.button_color = "#393e46"  # Button background
        self.button_text_color = "#ffffff"  # Button text

        # Configure root window
        self.root.configure(bg=self.bg_color)

        # Chat display area
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=50, state='disabled', font=("Helvetica", 12), bg="#393e46", fg=self.text_color)
        self.chat_area.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # User input area
        self.user_input = tk.Entry(root, width=40, font=("Helvetica", 12), bg="#eeeeee", fg="#222831")
        self.user_input.grid(row=1, column=0, padx=10, pady=10)
        self.user_input.bind("<Return>", self.respond)  # Enter key for sending

        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.respond, font=("Helvetica", 12), bg=self.button_color, fg=self.button_text_color, activebackground="#32e0c4")
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        # Clear button
        self.clear_button = tk.Button(root, text="Clear Chat", command=self.clear_chat, font=("Helvetica", 12), bg=self.button_color, fg=self.button_text_color)
        self.clear_button.grid(row=2, column=0, padx=10, pady=5, columnspan=2)

        # Welcome message
        self.display_message("Chatbot", "Hi there! I'm your animated assistant. Ask me anything!", self.bot_color)

    def display_message(self, sender, message, color):
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, f"{sender}: {message}\n", ('color',))
        self.chat_area.tag_config('color', foreground=color)
        self.chat_area.configure(state='disabled')
        self.chat_area.see(tk.END)

    def typing_animation(self, callback, *args):
        self.display_message("Chatbot", "Typing...", self.typing_color)
        time.sleep(1.5)  # Simulating typing delay
        self.chat_area.configure(state='normal')
        self.chat_area.delete("end-2l", "end-1l")  # Remove "Typing..." message
        self.chat_area.configure(state='disabled')
        callback(*args)  # Call the callback to display the actual response

    def clear_chat(self):
        self.chat_area.configure(state='normal')
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.configure(state='disabled')

    def respond(self, event=None):
        user_message = self.user_input.get().strip()
        if not user_message:
            return
        self.display_message("You", user_message, self.user_color)
        self.user_input.delete(0, tk.END)

        # Generate response in a separate thread to simulate animation
        threading.Thread(target=self.typing_animation, args=(self.show_response, user_message)).start()

    def show_response(self, user_message):
        # Generate the bot's response
        response = self.generate_response(user_message)
        self.display_message("Chatbot", response, self.bot_color)

    def generate_response(self, message):
        # Chatbot's responses
        if "hello" in message.lower():
            return "Hello! How can I assist you today?"
        elif "your name" in message.lower():
            return "I'm an animated chatbot, always here for you!"
        elif "how are you" in message.lower():
            return "I'm glowing in vibrant colors and ready to help! How can I assist you today?"
        elif "exit" in message.lower():
            self.root.destroy()
            return "Goodbye! Have a colorful day!"
        else:
            return "I'm not sure about that. Could you please provide more details?"

# Run the chatbot
root = tk.Tk()
chatbot_app = ChatbotGUI(root)
root.mainloop()
