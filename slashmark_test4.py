import tkinter as tk

# Set light pink background color
root = tk.Tk()
root.title("WhatsApp Chat (Demo)")
root.configure(bg="#ffc0cb")  # Light pink color code

# Create message history display area with text box style
chat_history = tk.Text(root, height=15, width=50, state="disabled", font=("Arial", 12))
chat_history.pack(padx=10, pady=10)
chat_history.configure(bg="#fff0f5")  # Light pink background for text box
chat_history.tag_configure("highlight", font=("Arial", 12, "bold"), foreground="black")  # Bold black text on light pink background

# Create input area with scrollbar and text box style
input_text = tk.Text(root, height=3, width=50, font=("Arial", 12))

input_text.pack(side="left", padx=10, pady=5)
input_scrollbar = tk.Scrollbar(root, orient="vertical", command=input_text.yview)
input_scrollbar.pack(side="right", fill="y")
input_text.config(yscrollcommand=input_scrollbar.set)
input_text.configure(bg="#fff0f5")  # Light pink background for text box
input_text.tag_configure("highlight", font=("Arial", 12, "bold"), foreground="black")  # Bold black text on light pink background

# Send button with click event handler (without a separate function)
def send_message():
  user_input = input_text.get("1.0", "end-1c")  # Get text excluding newline
  user_input=user_input.strip()
  response = model.generate_content(user_input)
  output=response.text
  chat_history.config(state="normal")  
  chat_history.insert(tk.END, f"You: {user_input}\n", "highlight")  
  chat_history.insert(tk.END, f"output: {output}\n", "highlight")
  chat_history.see(tk.END)  # Scroll to the latest message
  chat_history.config(state="disabled")  # Disable modification again
  input_text.delete("1.0", tk.END)  # Clear input box
import google.generativeai as genai
import os
# Explicitly set the API key here
os.environ["GEMINI_API_KEY"] = "AIzaSyBp73xiV4Yvw78MKDcR5DYJCbrLd96SNeo"

# Configure generative AI with the API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create a generative model
model = genai.GenerativeModel('gemini-pro')

# Generate content
  
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side="right", padx=5)

# Start the main loop
root.mainloop()