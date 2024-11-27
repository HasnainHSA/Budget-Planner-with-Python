import time

print("Salam! Aap ka budget track karte hain, lekin koi tension nahi, yeh koi serious kaam nahi hai!")
time.sleep(1)
print("Aur haan, chai ki expenses pe hum kabhi bhi judge nahi karte! 😜")
time.sleep(1)

# Step 1: Setting the budget
budget = float(input("\nPehle batayein, aapka total mahine ka budget kitna hai? (PKR): "))
print(f"\nZabardast! Aapka monthly budget PKR {budget} set kar diya gaya hai. Chaliye, ab kharchon ka track rakhte hain!")

# Step 2: Tracking expenses
expenses = {}
while True:
    print("\nAap kya karna chahte hain?")
    print("1. Naya kharcha add karein")
    print("2. Sare kharche dekhein")
    print("3. Kisi kharche ko edit karein")
    print("4. Kisi kharche ko delete karein")
    print("5. Budget ka summary dekhein")
    print("6. Exit karein")
    
    choice = input("\nApna choice enter karein (1-6): ").strip()
    
    if choice == "1":
        category = input("\nYe kharcha kis cheez ka hai? (e.g., Public Transport, Stationery, Printing): ").title()
        amount = float(input(f"{category} par kitna kharcha hua? (PKR): "))
        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount
        print(f"Done! {category} ka PKR {amount} add kar diya gaya hai.")
    
    elif choice == "2":
        if not expenses:
            print("\nAbhi tak koi kharcha add nahi kiya. Shuru karain, budget ka game jeetna hai!")
        else:
            print("\nYahan aapke sare kharche listed hain:")
            for category, amount in expenses.items():
                print(f"- {category}: PKR {amount}")
    
    elif choice == "3":
        if not expenses:
            print("\nEdit karne ke liye koi kharcha nahi hai. Pehle ek add karein, warna hum khali haath rahenge! 😅")
        else:
            category = input("\nKaunsa kharcha edit karna chahte hain? ").title()
            if category in expenses:
                new_amount = float(input(f"{category} ka naya amount bataein (PKR): "))
                expenses[category] = new_amount
                print(f"Update ho gaya! {category} ka naya amount PKR {new_amount} set ho gaya.")
            else:
                print(f"{category} nahi mila. Thoda dhyan se check karein!")
    
    elif choice == "4":
        if not expenses:
            print("\nDelete karne ke liye koi kharcha nahi hai. Aapne toh budget mein ghazab ka control rakha hai!")
        else:
            category = input("\nKaunsa kharcha delete karna chahte hain? ").title()
            if category in expenses:
                del expenses[category]
                print(f"{category} ko delete kar diya gaya hai. Ab aapka budget thoda aur safe hai! 😎")
            else:
                print(f"{category} nahi mila. Shayed spelling galat thi!")
    
    elif choice == "5":
        if not expenses:
            print("\nAbhi tak koi kharcha nahi hua. Aap ekdum budget-friendly ho! 😅")
        else:
            print("\nBudget ka summary yeh raha:")
            total_expenses = sum(expenses.values())
            remaining_budget = budget - total_expenses
            
            for category, amount in expenses.items():
                print(f"- {category}: PKR {amount}")
            
            print(f"\nTotal Expenses: PKR {total_expenses}")
            print(f"Remaining Budget: PKR {remaining_budget}")
            
            if remaining_budget > 0:
                print("Shabaash! Aap budget ke andar hain. Budget ka king/queen ban gaye ho! 👑")
            elif remaining_budget == 0:
                print("Wah bhai! Perfect budget planning. Aapne bilkul balance kar liya hai! 🎯")
            else:
                print("Oooops! Lagta hai thoda zyada kharch ho gaya hai. Paisay thoda tight karo, varna wallet ka dard hoga! 😖")
    
    elif choice == "6":
        print("\nShukriya Budget Planner use karne ke liye. Paisay sambhalke rakhein, warna bacha kucha budget bhi gayab ho jata hai! 💸 Allah Hafiz!")
        break
    
    else:
        print("\nInvalid choice. Thoda dhyan se choice select karein, warna kharch kaafi ho sakta hai! 😂")
