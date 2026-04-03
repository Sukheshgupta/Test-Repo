def kgs_to_grams(kgs):
    return kgs * 1000


def kgs_to_lbs(kgs):
    return kgs * 2.20462


def main():
    kgs = float(input("Enter weight in kgs: "))
    print(f"{kgs} kgs = {kgs_to_grams(kgs)} grams")

main()