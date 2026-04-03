def kgs_to_grams(kgs):
    return kgs * 1000

def gms_to_kgs(gms):
    return gms/1000

def kgs_to_lbs(kgs):
    return kgs * 2.20462

def multiplication(a,b):
    return a*b


def main():
    kgs = float(input("Enter weight in kgs: "))
    print(f"{kgs} kgs = {kgs_to_grams(kgs)} grams")

main()