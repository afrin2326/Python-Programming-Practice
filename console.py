from api import (
    insert_guest, update_guest, delete_guest, show_guest,
    insert_room, update_room, delete_room, show_room,
    load_guests, load_rooms
)


def menu():
    """Display main menu"""
    print("\n" + "=" * 60)
    print("               🌟 HOTEL MANAGEMENT SYSTEM 🌟")
    print("=" * 60)
    print(" 1. Add New Guest")
    print(" 2. Update Guest Information")
    print(" 3. Delete Guest")
    print(" 4. Show Guest List")
    print("-" * 60)
    print(" 5. Add New Room")
    print(" 6. Update Room Information")
    print(" 7. Delete Room")
    print(" 8. Show Room List")
    print("-" * 60)
    print(" 9. Exit & Save")
    print("=" * 60)


def show_guests_table():
    """Display guests in formatted table"""
    data = show_guest()
    if not data:
        print("\n📭 No guest data found.")
    else:
        print("\n" + "=" * 50)
        print("                     GUEST LIST")
        print("=" * 50)
        print("{:<10} {:<20} {:<15}".format("ID", "Name", "Phone"))
        print("-" * 50)
        for g in data:
            parts = g.strip().split(',')
            if len(parts) >= 3:
                print("{:<10} {:<20} {:<15}".format(parts[0], parts[1], parts[2]))
        print("=" * 50)
        print(f"Total Guests: {len(data)}")


def show_rooms_table():
    """Display rooms in formatted table"""
    data = show_room()
    if not data:
        print("\n📭 No room data found.")
    else:
        print("\n" + "=" * 50)
        print("                     ROOM LIST")
        print("=" * 50)
        print("{:<10} {:<20} {:<10}".format("ID", "Type", "Price"))
        print("-" * 50)
        for r in data:
            parts = r.strip().split(',')
            if len(parts) >= 3:
                print("{:<10} {:<20} {:<10}".format(parts[0], parts[1], parts[2]))
        print("=" * 50)
        print(f"Total Rooms: {len(data)}")


def main():
    """Main program loop"""
    print("\n" + "=" * 60)
    print("      📁 Loading data from files...")
    print("=" * 60)

    # Load data from files at startup
    load_guests()
    load_rooms()

    print("\n✅ Data loaded successfully!")

    while True:
        menu()
        choice = input("👉 Enter your choice (1-9): ").strip()

        if choice == "1":
            print("\n" + "-" * 40)
            print("        ADD NEW GUEST")
            print("-" * 40)
            gid = input("Guest ID: ").strip()
            name = input("Guest Name: ").strip()
            phone = input("Phone Number: ").strip()

            if gid and name and phone:
                insert_guest(gid, name, phone)
            else:
                print("❌ All fields are required!")

        elif choice == "2":
            print("\n" + "-" * 40)
            print("        UPDATE GUEST")
            print("-" * 40)
            show_guests_table()
            gid = input("\nEnter Guest ID to update: ").strip()
            name = input("New Guest Name: ").strip()
            phone = input("New Phone Number: ").strip()

            if gid and name and phone:
                update_guest(gid, name, phone)
            else:
                print("❌ All fields are required!")

        elif choice == "3":
            print("\n" + "-" * 40)
            print("        DELETE GUEST")
            print("-" * 40)
            show_guests_table()
            gid = input("\nEnter Guest ID to delete: ").strip()

            if gid:
                confirm = input(f"Are you sure to delete guest {gid}? (y/n): ").lower()
                if confirm == 'y':
                    delete_guest(gid)
                else:
                    print("❌ Deletion cancelled.")
            else:
                print("❌ Guest ID is required!")

        elif choice == "4":
            show_guests_table()

        elif choice == "5":
            print("\n" + "-" * 40)
            print("        ADD NEW ROOM")
            print("-" * 40)
            rid = input("Room ID: ").strip()
            rtype = input("Room Type (e.g., Standard, Deluxe, Suite): ").strip()
            price = input("Room Price: ").strip()

            if rid and rtype and price:
                insert_room(rid, rtype, price)
            else:
                print("❌ All fields are required!")

        elif choice == "6":
            print("\n" + "-" * 40)
            print("        UPDATE ROOM")
            print("-" * 40)
            show_rooms_table()
            rid = input("\nEnter Room ID to update: ").strip()
            rtype = input("New Room Type: ").strip()
            price = input("New Room Price: ").strip()

            if rid and rtype and price:
                update_room(rid, rtype, price)
            else:
                print("❌ All fields are required!")

        elif choice == "7":
            print("\n" + "-" * 40)
            print("        DELETE ROOM")
            print("-" * 40)
            show_rooms_table()
            rid = input("\nEnter Room ID to delete: ").strip()

            if rid:
                confirm = input(f"Are you sure to delete room {rid}? (y/n): ").lower()
                if confirm == 'y':
                    delete_room(rid)
                else:
                    print("❌ Deletion cancelled.")
            else:
                print("❌ Room ID is required!")

        elif choice == "8":
            show_rooms_table()

        elif choice == "9":
            print("\n" + "=" * 60)
            print("     💾 Saving data to files...")
            print("     👋 Thank you for using Hotel Management System!")
            print("=" * 60)
            break

        else:
            print("❌ Invalid option! Please choose 1-9.")

        input("\nPress Enter to continue...")


if _name_ == "_main_":
    main()