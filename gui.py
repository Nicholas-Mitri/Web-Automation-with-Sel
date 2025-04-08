import tkinter as tk


class App:

    def __init__(self, root):
        self.root = root
        self.root.title("Web Automation GUI")

        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=10, pady=10, fill=tk.X)
        # Configure column widths for login_frame
        self.login_frame.columnconfigure(0, weight=1, minsize=150)
        self.login_frame.columnconfigure(1, weight=1)

        tk.Label(self.login_frame, text="Username:").grid(
            row=0, column=0, sticky="w", padx=(0, 10)
        )
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, sticky="ew")

        tk.Label(self.login_frame, text="Password:").grid(
            row=1, column=0, sticky="w", padx=(0, 10)
        )
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, sticky="ew")

        # Form submission frame
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(padx=10, pady=10, fill=tk.X)
        # Configure column widths for form_frame - same as login_frame
        self.form_frame.columnconfigure(0, weight=1, minsize=150)
        self.form_frame.columnconfigure(1, weight=1)

        tk.Label(self.form_frame, text="Full Name:").grid(
            row=0, column=0, sticky="w", padx=(0, 10)
        )
        self.url_entry = tk.Entry(self.form_frame)
        self.url_entry.grid(row=0, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Email:").grid(
            row=1, column=0, sticky="w", padx=(0, 10)
        )
        self.email_entry = tk.Entry(self.form_frame)
        self.email_entry.grid(row=1, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Current Address:").grid(
            row=2, column=0, sticky="w", padx=(0, 10)
        )
        self.address_entry = tk.Entry(self.form_frame)
        self.address_entry.grid(row=2, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Permanent Address:").grid(
            row=3, column=0, sticky="w", padx=(0, 10)
        )
        self.permanent_address_entry = tk.Entry(self.form_frame)
        self.permanent_address_entry.grid(row=3, column=1, sticky="ew")


root = tk.Tk()
app = App(root)
root.mainloop()
