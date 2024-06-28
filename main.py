import tkinter as tk
from tkinter import messagebox
import requests

github_api_url = 'https://api.github.com'


def get_github_data(token, username):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(f'{github_api_url}/users/{username}')
    if response.status_code == 200:
        return response.json()
    else:
        return None


def fetch_data():
    token = token_entry.get().strip()
    username = username_entry.get().strip()

    if not token or not username:
        messagebox.showerror("Error", "Please enter GitHub token and username.")
        return

    data = get_github_data(token, username)
    if data:
        key_value_pairs = {key: value for key, value in data.items() if not isinstance(value, (dict, list))}
        messagebox.showinfo("GitHub Data", f"Key-Value Pairs:\n\n{key_value_pairs}")
    else:
        messagebox.showerror("Error", "Failed to fetch GitHub data. Please check your credentials.")


root = tk.Tk()
root.title("GitHub User Data Fetcher")

token_label = tk.Label(root, text="GitHub Token:")
token_label.pack(pady=5)
token_entry = tk.Entry(root, width=50)
token_entry.pack(pady=5)

username_label = tk.Label(root, text="GitHub Username:")
username_label.pack(pady=5)
username_entry = tk.Entry(root, width=50)
username_entry.pack(pady=5)

fetch_button = tk.Button(root, text="Fetch User Data", command=fetch_data)
fetch_button.pack(pady=10)

root.mainloop()
