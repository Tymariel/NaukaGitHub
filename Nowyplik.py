latawce_dzis = input("Ilosc latawcow Dzisiaj: ")
latawce_wczoraj = input("Ilosc latawcow wczoraj: ")
print(f"Ilosc latawcow na niebie dzisiaj: {latawce_dzis}")
print(f"ilosc latawcow na niebie wczoraj: {latawce_wczoraj}")
Latawce_w_sumie = int(latawce_dzis) + int(latawce_wczoraj)
print(f"Ilosc latawcow w tym tygodniu: {Latawce_w_sumie}")
if Latawce_w_sumie >= int(10):
    print("Musialo byc czyste niebo")
else:
    print("Malo latawcow")
