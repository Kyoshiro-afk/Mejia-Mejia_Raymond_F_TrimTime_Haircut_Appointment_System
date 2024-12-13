import os
import platform
from datetime import datetime

class BarberShop:
    def __init__(self):
        self.customers = {}  # Store customers by phone number
        self.appointments = []  # Store appointments
        self.haircut_options = {
            "1": {"name": "Fade", "price": 100},
            "2": {"name": "Fringe", "price": 100},
            "3": {"name": "Mullet", "price": 100},
            "4": {"name": "Blowout", "price": 100},
            "5": {"name": "Barbers", "price": 100},
            "6": {"name": "Buzz cut", "price": 100},
            "7": {"name": "Undercut", "price": 100},
            "8": {"name": "Two Block", "price": 100},
            "9": {"name": "Taper Fade", "price": 100},
            "10": {"name": "French crop", "price": 100},
        }
        self.barbers = ["Ronel", "Robert", "Andrei", "Lawrence", "John Rex"]
        self.available_time_slots = [
            "08:00 AM", "08:30 AM", "09:00 AM", "09:30 AM", "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM",
            "12:00 PM", "12:30 PM", "01:00 PM", "01:30 PM", "02:00 PM", "02:30 PM", "03:00 PM", "03:30 PM",
            "04:00 PM", "04:30 PM", "05:00 PM", "05:30 PM", "06:00 PM", "06:30 PM", "07:00 PM", "07:30 PM", "08:00 PM"
        ]

    def clear_screen(self):
        if platform.system() == "Windows":
            os.system("cls")  # Clear screen on Windows
        else:
            os.system("clear")  # Clear screen on Linux/macOS

    def view_haircut_options(self):
        print("\n--- Available Haircut Options ---")
        for option_id, details in self.haircut_options.items():
            print(f"{option_id}. {details['name']} - {self.format_price(details['price'])}")

    def view_barbers(self):
        print("\n--- Available Barbers ---")
        for idx, barber in enumerate(self.barbers, start=1):
            print(f"{idx}. {barber}")

    def add_customer(self):
        name = input("Enter customer name (First and Last, or include second names if applicable): ")
        name_parts = name.split()
        if len(name_parts) >= 2:  # Ensure at least a first and last name
            formatted_name = " ".join(part.capitalize() for part in name_parts)  # Capitalize all parts
            name = formatted_name
        else:
            print("Invalid name format. Please enter at least a first and last name.")
            return

        while True:
            phone = input("Enter customer phone number (11 digits, starts with '09'): ")
            if phone.isdigit() and len(phone) == 11 and phone.startswith("09"):
                if phone in self.customers:
                    print("A customer with this phone number already exists.")
                    return
                break
            else:
                print("Invalid phone number. Please enter exactly 11 digits starting with '09'.")

        self.customers[phone] = name
        print(f"Customer {name} added successfully!")

    def search_name(self):
        name_to_search = input("Enter the customer name to search: ").lower()
        found = False
        print("\n--- Search Results ---")
        for phone, name in self.customers.items():
            if name_to_search in name.lower():
                print(f"Name: {name}")
                found = True
        if not found:
            print("No matching customer found.")

    def show_available_time_slots(self, date):
        taken_times = [appt["time"] for appt in self.appointments if appt["date"] == date]
        available_times = [time for time in self.available_time_slots if time not in taken_times]
        return available_times

    def book_appointment(self):
        name = input("Enter customer name (First and Last, or include second names if applicable): ")
        name_parts = name.split()
        if len(name_parts) >= 2:
            formatted_name = " ".join(part.capitalize() for part in name_parts)
            name = formatted_name
        else:
            print("Invalid name format. Please enter at least a first and last name.")
            return

        while True:
            phone = input("Enter customer phone number (11 digits, starts with '09'): ")
            if phone.isdigit() and len(phone) == 11 and phone.startswith("09"):
                if phone in self.customers:
                    print("A customer with this phone number already exists.")
                    return
                break
            else:
                print("Invalid phone number. Please enter exactly 11 digits starting with '09'.")

        self.customers[phone] = name
        print(f"Customer {name} added successfully!")

        date = input("Enter appointment date (YYYY-MM-DD): ")
        date = self.format_date(date)

        available_times = self.show_available_time_slots(date)
        if not available_times:
            print("No available time slots for the selected date. Please try another date.")
            return

        print("\n--- Available Time Slots ---")
        for idx, time in enumerate(available_times, start=1):
            print(f"{idx}. {time}")

        time_choice = input("Choose a time slot by entering the number: ")
        if not time_choice.isdigit() or not (1 <= int(time_choice) <= len(available_times)):
            print("Invalid time slot choice. Please try again.")
            return
        time = available_times[int(time_choice) - 1]

        self.view_haircut_options()
        haircut_choice = input("Choose a haircut option by entering the number: ")
        if haircut_choice not in self.haircut_options:
            print("Invalid haircut option. Please try again.")
            return

        self.view_barbers()
        barber_choice = input("Choose a barber by entering the number: ")
        if not barber_choice.isdigit() or not (1 <= int(barber_choice) <= len(self.barbers)):
            print("Invalid barber choice. Please try again.")
            return
        selected_barber = self.barbers[int(barber_choice) - 1]

        selected_haircut = self.haircut_options[haircut_choice]
        self.appointments.append({
            "phone": phone,
            "date": date,
            "time": time,
            "haircut": selected_haircut["name"],
            "price": selected_haircut["price"],
            "barber": selected_barber
        })

        print(f"\nAppointment booked successfully with {selected_barber} for {selected_haircut['name']}!")
        print("\n--- Appointment Record ---")
        print(f"Name: {name}")
        print(f"Phone: {phone}")
        print(f"Haircut: {selected_haircut['name']}")
        print(f"Barber: {selected_barber}")
        print(f"Date: {date}")
        print(f"Time: {time}")
        print("---")

    def view_appointments(self):
        if not self.appointments:
            print("No appointments found.")
        else:
            print("\n--- Appointment List ---")
            for appt in self.appointments:
                name = self.customers[appt['phone']]
                print(f"Customer: {name}")
                print(f"Date: {appt['date']}")
                print(f"Time: {appt['time']}")
                print("---")

    def cancel_appointment(self):
        name_to_cancel = input("Enter the customer name to cancel appointment: ").lower()
        found = False
        for appt in self.appointments:
            customer_name = self.customers[appt["phone"]].lower()
            if name_to_cancel in customer_name:
                found = True
                print("\n--- Appointment to Cancel ---")
                print(f"Name: {self.customers[appt['phone']]}")  # Display the customer details
                print(f"Phone: {appt['phone']}")  # Display the customer's phone number
                print(f"Haircut: {appt['haircut']}")  # Display the haircut chosen
                print(f"Barber: {appt['barber']}")  # Display the barber assigned
                print(f"Date: {appt['date']}")
                print(f"Time: {appt['time']}")
                confirm = input("Do you want to cancel this appointment? (yes/no): ").lower()
                if confirm == "yes":
                    self.appointments.remove(appt)
                    print(f"Appointment for {self.customers[appt['phone']]} canceled successfully.")
                    return
                else:
                    print("Appointment cancellation aborted.")
                    return
        if not found:
            print("No matching customer found for cancellation.")

    def is_valid_datetime(self, date_str, time_str):
        try:
            datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %I:%M %p")
            return True
        except ValueError:
            return False

    def format_price(self, price):
        return f"₱{price:,.2f}"

    def format_date(self, date):
        return date[:4] + '-' + date[4:6] + '-' + date[6:]

    def run(self):
        while True:
            self.clear_screen()  # Clear the screen at the start of each loop
            print("\nTrimTime: Haircut Appointment System")
            print("1. Book Appointment")
            print("2. View Appointments")
            print("3. Search Name")
            print("4. Cancel Appointment")
            print("5. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.book_appointment()
            elif choice == "2":
                self.view_appointments()
            elif choice == "3":
                self.search_name()
            elif choice == "4":
                self.cancel_appointment()
            elif choice == "5":
                print("Exiting the System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

            # Pause after each loop to allow time for the user to see the output
            input("Press Enter to continue...")

# Run the system
if __name__ == "__main__":
    shop = BarberShop()
    shop.run()
