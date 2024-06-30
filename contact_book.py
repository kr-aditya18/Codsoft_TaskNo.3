import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, master):
        self.master = master
        master.title("Contact Book")
        master.geometry("400x400")

        # Create a frame for the contact list
        self.contact_list_frame = tk.Frame(master)
        self.contact_list_frame.pack(fill="both", expand=True)

        # Create a listbox to display the contact list
        self.contact_list = tk.Listbox(self.contact_list_frame, width=40)
        self.contact_list.pack(fill="both", expand=True)

        # Create a frame for the contact details
        self.contact_details_frame = tk.Frame(master)
        self.contact_details_frame.pack(fill="x")

        # Create labels and entries for the contact details
        self.name_label = tk.Label(self.contact_details_frame, text="Name:")
        self.name_label.pack(side="left")
        self.name_entry = tk.Entry(self.contact_details_frame, width=20)
        self.name_entry.pack(side="left")

        self.phone_label = tk.Label(self.contact_details_frame, text="Phone:")
        self.phone_label.pack(side="left")
        self.phone_entry = tk.Entry(self.contact_details_frame, width=20)
        self.phone_entry.pack(side="left")

        self.email_label = tk.Label(self.contact_details_frame, text="Email:")
        self.email_label.pack(side="left")
        self.email_entry = tk.Entry(self.contact_details_frame, width=20)
        self.email_entry.pack(side="left")

        self.address_label = tk.Label(self.contact_details_frame, text="Address:")
        self.address_label.pack(side="left")
        self.address_entry = tk.Entry(self.contact_details_frame, width=20)
        self.address_entry.pack(side="left")

        # Create buttons for adding, updating, and deleting contacts
        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.pack(fill="x")

        self.update_button = tk.Button(master, text="Update Contact", command=self.update_contact)
        self.update_button.pack(fill="x")

        self.delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(fill="x")

        self.search_button = tk.Button(master, text="Search Contact", command=self.search_contact)
        self.search_button.pack(fill="x")

        # Initialize the contact list
        self.contacts = {}

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            self.contact_list.insert("end", f"{name} - {phone}")
            self.name_entry.delete(0, "end")
            self.phone_entry.delete(0, "end")
            self.email_entry.delete(0, "end")
            self.address_entry.delete(0, "end")
        else:
            messagebox.showerror("Error", "Please enter name and phone number")

    def update_contact(self):
        selected_contact = self.contact_list.get("active")
        if selected_contact:
            name, phone = selected_contact.split(" - ")
            self.contacts[name]["phone"] = self.phone_entry.get()
            self.contacts[name]["email"] = self.email_entry.get()
            self.contacts[name]["address"] = self.address_entry.get()
            self.contact_list.delete("active")
            self.contact_list.insert("end", f"{name} - {phone}")
        else:
            messagebox.showerror("Error", "Please select a contact to update")

    def delete_contact(self):
        selected_contact = self.contact_list.get("active")
        if selected_contact:
            name, phone = selected_contact.split(" - ")
            del self.contacts[name]
            self.contact_list.delete("active")
        else:
            messagebox.showerror("Error", "Please select a contact to delete")

    def search_contact(self):
        search_term = self.name_entry.get()
        if search_term:
            self.contact_list.delete(0, "end")
            for name, details in self.contacts.items():
                if search_term in name or search_term in details["phone"]:
                    self.contact_list.insert("end", f"{name} - {details['phone']}")

root = tk.Tk()
my_contact_book = ContactBook(root)
root.mainloop() 