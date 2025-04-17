from operator import is_not

prices={
	"apple":0.50,
	"milk":1.00,
	"chicken":1.59,
	"potato":0.57
}
item1_name=input("Enter Name of Item1").lower()
item1_qty=float(input(f"Enter numer of Quantity of {item1_name}"))

item2_name=input("Enter Name of Item2").lower()
item2_qty=float(input(f"Enter numer of Quantity of {item2_name}"))

item3_name=input("Enter Name of Item3").lower()
item3_qty=float(input(f"Enter numer of Quantity of {item3_name}"))

item1_price=prices.get(item1_name)
item2_price=prices.get(item2_name)
item3_price=prices.get(item3_name)

item1_total=item1_price * item1_qty
item2_total=item2_price * item2_qty
item3_total=item1_price * item3_qty

SubTotal=item1_total + item2_total + item3_total

print("Receipt:")
print(f"{item1_name.capitalize()} : {item1_qty} @ {item1_price} each = {item1_total}")
print(f"{item2_name.capitalize()} : {item2_qty} @ {item2_price} each = {item2_total}")
print(f"{item3_name.capitalize()} : {item3_qty} @ {item3_price:.2f} each = {item3_total}")

print(f"Total Bill + 18% GST = {(SubTotal * 118)/100}")

