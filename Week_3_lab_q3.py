
print("ENTER YOUR DAILY STORE SALES")

Sunday = int(input("Enter the store sales for Sunday: "))
Monday = int(input("Enter the store sales for Monday: "))
Tuesday = int(input("Enter the store sales for Tuesday: "))
Wednsday = int(input("Enter the store sales for Wednsday: "))
Thursday = int(input("Enter the store sales for Thursday: "))
Friday = int(input("Enter the store sales for Friday: "))
Saturday = int(input("Enter the store sales for Saturday: "))

store_week_sales = [Sunday, Monday, Tuesday, Wednsday, Thursday, Friday, Saturday]
print(list(store_week_sales))
total = 0

for store_sale in store_week_sales:
    total += store_sale

print ("Total week sales: %.2f" % total)