from models import Battery

def test_models():
    new_b = Battery(1,"Parkside", 20, 2.4, 3)
    print(new_b)

if __name__ == "__main__":
    test_models()