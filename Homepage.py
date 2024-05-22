import streamlit as st
import csv
from pages.loginpage import a
from pages.signuppage import Dictnames

st.title("Welcome to :blue[_AUTOMARVEL_]!!")
st.header("hello user", divider = "rainbow")

class Car:


   def __init__(self, car_type, brand, models, price, variants, specs, similar_cars):
    self.car_type = car_type
    self.brand = brand
    self.models = models
    self.price = price
    self.variants = variants
    self.specs = specs
    self.similar_cars = similar_cars
    
cars_data = [
Car(
    car_type="Coupe",
    brand="BMW",
    models=["2 Series Coupe", "4 Series Coupe", "8 Series Coupe", "M2 Coupe", "M4 Coupe"],
    price=["40,000 - 150,000", "45,000 - 160,000", "85,000 - 200,000", "60,000 - 80,000", "070,000 - 090,000"],
    variants=[["M Sport", "xDrive", "Gran Coupe"], ["M Sport", "xDrive", "Gran Coupe"], ["M Sport", "xDrive", "Gran Coupe"], ["Competition", "CS"], ["Competition", "CS"]],
    specs=["Various engine options, luxurious interiors, advanced technology features.", "Powerful engines, sporty design, advanced infotainment system.", "Luxurious interior, cutting-edge technology, high-performance engines.", "High-performance engine, track-focused design, lightweight construction.", "Track-focused performance, aggressive styling, advanced technology."],
    similar_cars=[["Audi A5 Coupe", "Mercedes-Benz C-Class Coupe", "Lexus RC Coupe"], ["Audi A5 Coupe", "Mercedes-Benz C-Class Coupe", "Lexus RC Coupe"], ["Audi A5 Coupe", "Mercedes-Benz C-Class Coupe", "Lexus RC Coupe"], ["Audi RS 5 Coupe", "Mercedes-AMG C 63 Coupe", "Lexus RC F"], ["Audi RS 5 Coupe", "Mercedes-AMG C 63 Coupe", "Lexus RC F"]]
),
Car(
    car_type="Coupe",
    brand="Mercedes-Benz",
    models=["C-Class Coupe", "E-Class Coupe", "S-Class Coupe", "CLS Coupe", "AMG GT Coupe"],
    price=["050,000 - 0200,000", "060,000 - 0250,000", "090,000 - 0250,000", "070,000 - 120,000", "100,000 - 200,000"],
    variants=[["AMG Line", "4MATIC", "Cabriolet"], ["AMG Line", "4MATIC", "Cabriolet"], ["AMG Line", "4MATIC", "Cabriolet"], ["AMG Line", "4MATIC", "Cabriolet"], ["Base", "S", "C", "R"]],
    specs=["Luxury materials, advanced technology, sporty design.", "Luxurious interiors, cutting-edge technology, powerful engines.", "Premium materials, advanced features, top-of-the-line performance.", "Luxurious interior, sporty design, advanced safety features.", "Powerful engines, luxurious interiors, advanced infotainment."],
    similar_cars=[["BMW 4 Series Coupe", "Audi A5 Coupe", "Lexus RC Coupe"], ["BMW 4 Series Coupe", "Audi A5 Coupe", "Lexus RC Coupe"], ["BMW 4 Series Coupe", "Audi A5 Coupe", "Lexus RC Coupe"], ["BMW 4 Series Coupe", "Audi A5 Coupe", "Lexus RC Coupe"], ["BMW 8 Series Coupe", "Audi S5 Coupe", "Lexus LC Coupe"]]
),
Car(
    car_type="Coupe",
    brand="Audi",
    models=["A5 Coupe", "S5 Coupe", "RS 5 Coupe", "TT Coupe", "R8 Coupe"],
    price=["45,000 - 100,000", "55,000 - 150,000", "70,000 - 110,000", "50,000 - 70,000", "150,000 - 200,000"],
    variants=[["Quattro", "Black Edition", "Cabriolet"], ["Quattro", "Black Edition", "Cabriolet"], ["Quattro", "Black Edition", "Cabriolet"], ["Base", "S", "RS"], ["RWS", "Spyder", "Decennium"]],
    specs=["Luxury features, powerful engines, advanced technology.", "Sporty design, luxurious interiors, cutting-edge technology.", "High-performance engine, dynamic handling, advanced infotainment.", "Sporty design, agile handling, advanced features.", "High-performance engine, aerodynamic design, advanced technology."],
    similar_cars=[["BMW 4 Series Coupe", "Mercedes-Benz C-Class Coupe", "Lexus RC Coupe"], ["BMW 4 Series Coupe", "Mercedes- Benz C-Class Coupe", "Lexus RC Coupe"], ["BMW M4 Coupe", "Mercedes-AMG C 63 Coupe", "Lexus RC F"], ["BMW 2 Series Coupe", "Mercedes-Benz CLA Coupe", "Porsche 718 Cayman"], ["Lamborghini Huracan", "Ferrari 488 GTB", "Porsche 911 Turbo"]]
),
Car(
    car_type="Coupe",
    brand="Porsche",
    models=["911 Coupe", "718 Cayman", "Panamera Coupe", "Cayenne Coupe", "Taycan Coupe"],
    price=["90,000 - 200,000", "60,000 - 100,000", "90,000 - 200,000", "70,000 - 150,000", "100,000 - 200,000"],
    variants=[["Turbo", "GTS", "GT4"], ["S", "GTS", "GT4"], ["4S", "Turbo", "Turbo S"], ["S", "Turbo", "Turbo S"], ["4S", 
    "Turbo", "Turbo S"]],
    specs=["Legendary performance, iconic design, precision engineering.", "Agile handling, powerful engines, sporty design.", "Luxurious interiors, cutting-edge technology, high-performance engines.", "Sporty design, powerful engines, advanced technology.", "Instant acceleration, long-range capability, innovative design."],
    similar_cars=[["Audi R8", "Mercedes-AMG GT", "Nissan GT-R"], ["BMW M4 Coupe", "Audi TT RS", "Mercedes-AMG C 63 Coupe"], 
   ["Audi A7 Coupe", "BMW 8 Series Gran Coupe", "Mercedes-Benz CLS Coupe"], ["BMW X6 Coupe", "Mercedes-Benz GLE Coupe", 
   "Audi Q8"], ["Tesla Model S", "Jaguar I-PACE", "Audi e-tron GT"]]
),
Car(
    car_type="Coupe",
    brand="Lexus",
    models=["RC Coupe", "LC Coupe"],
    price=["50,000 - 100,000", "90,000 - 120,000"],
    variants=[["F Sport", "Hybrid", "Track Edition"], ["Base", "F Sport", "Hybrid"]],
    specs=["Luxury features, smooth performance, cutting-edge technology.", "High-performance engine, luxurious interiors, advanced safety features."],
    similar_cars=[["BMW 8 Series Coupe", "Audi S5 Coupe", "Mercedes-Benz S-Class Coupe"], ["Porsche 911 Coupe", "Audi R8", 
  "Mercedes-AMG GT"]]
),
Car(
    car_type="Coupe",
    brand="Ferrari",
    models=["F8 Tributo", "812 Superfast", "SF90 Stradale"],
    price=["300,000 - 400,000", "350,000 - 500,000", "600,000 - 700,000"],
    variants=[["Base", "Spider"], ["Base", "Spider"], ["Base"]],
    specs=["High-performance V8 engine, stunning design, advanced aerodynamics.", "Naturally aspirated V12 engine, breathtaking performance, luxurious interiors.", "Hybrid powertrain, exceptional handling, cutting-edge technology."],
    similar_cars=[["Lamborghini Huracan", "McLaren 720S", "Audi R8"], ["Lamborghini Aventador", "McLaren 720S", "Bentley Continental GT"], ["Porsche 911 Turbo S", "Audi R8", "McLaren GT"]]
),
Car(
    car_type="Coupe",
    brand="Lamborghini",
    models=["Huracan Coupe", "Aventador Coupe", "Urus"],
    price=["200,000 - 300,000", "400,000 - 500,000", "200,000 - 300,000"],
    variants=[["EVO", "EVO RWD", "Performante"], ["S", "SVJ"], ["Standard", "Pearl Capsule", "Graphite Capsule"]],
    specs=["Exotic design, powerful V10 engine, advanced aerodynamics.", "Iconic design, monstrous V12 engine, blistering performance.", "Luxury SUV, high-performance capabilities, cutting-edge technology."],
    similar_cars=[["Ferrari 488 GTB", "McLaren 720S", "Porsche 911 Turbo"], ["Ferrari SF90 Stradale", "McLaren Speedtail", "Bugatti Chiron"], ["Porsche Cayenne", "Audi RS Q8", "BMW X5 M"]]
),
Car(
    car_type="Coupe",
    brand="McLaren",
    models=["570S Coupe", "720S Coupe", "Artura"],
    price=["200,000 - 250,000", "300,000 - 350,000", "200,000 - 250,000"],
    variants=[["Luxury", "Track", "Spider"], ["Standard", "Performance", "Spider"], ["Standard", "Performance"]],
    specs=["Lightweight construction, powerful engine, precision handling.", "Aerodynamic design, twin-turbo V8 engine, track-focused performance.", "Hybrid powertrain, exceptional handling, futuristic design."],
    similar_cars=[["Porsche 911 Turbo", "Audi R8", "Ferrari 488 GTB"], ["Lamborghini Huracan", "Ferrari SF90 Stradale", "Porsche 911 GT3 RS"], ["Porsche 911 Turbo S", "Ferrari SF90 Stradale", "Aston Martin Vantage"]]
),
Car(
    car_type="Coupe",
    brand="Aston Martin",
    models=["Vantage", "DB11 Coupe", "DBS Superleggera"],
    price=["150,000 - 200,000", "200,000 - 250,000", "300,000 - 350,000"],
    variants=[["Base", "AMR", "Vantage F1 Edition"], ["Base", "AMR", "Volante"], ["Base", "Volante"]],
    specs=["Aggressive design, powerful engine, athletic performance.", "Elegant design, potent V12 engine, luxurious interiors.", "Stunning design, monstrous V12 engine, exhilarating performance."],
    similar_cars=[["Porsche 911 Turbo", "Audi R8", "McLaren 570S"], ["Ferrari Portofino", "Bentley Continental GT", "Mercedes-AMG GT"], ["Ferrari 812 Superfast", "Bentley Continental GT", "Lamborghini Aventador"]]
)

]



class BUYCAR:
    bought_cars = {
    '2 Series Coupe': 148,
    '4 Series Coupe': 321,
    '8 Series Coupe': 284,
    'M2 Coupe': 311,
    'M4 Coupe': 258,
    'C-Class Coupe': 234,
    'E-Class Coupe': 136,
    'S-Class Coupe': 237,
    'CLS Coupe': 418,
    'AMG GT Coupe': 448,
    'A5 Coupe': 123,
    'S5 Coupe': 458,
    'RS 5 Coupe': 207,
    'TT Coupe': 127,
    'R8 Coupe': 165,
    '911 Coupe': 479,
    '718 Cayman': 398,
    'Panamera Coupe': 384,
    'Cayenne Coupe': 379,
    'Taycan Coupe': 426,
    'RC Coupe': 162,
    'LC Coupe': 202,
    'F8 Tributo': 211,
    '812 Superfast': 442,
    'SF90 Stradale': 175,
    'Huracan Coupe': 151,
    'Aventador Coupe': 439,
    'Urus': 449,
    '570S Coupe': 132,
    '720S Coupe': 228,
    'Artura': 236,
    'Vantage': 437,
    'DB11 Coupe': 472,
    'DBS Superleggera': 160
    }

    @classmethod
    def buy_car(cls, carModel):
        if carModel in cls.bought_cars:
            cls.bought_cars[carModel] += 1
        else:
            cls.bought_cars[carModel] = 1


selected_brand = st.selectbox("Select Car Brand", sorted(list(set(car.brand for car in cars_data))))

    
selected_car = [car for car in cars_data if car.brand == selected_brand]

selected_model = st.selectbox("Select Car Model", selected_car[0].models)

    
Price = [0, 50000, 100000, 200000, 300000, 400000, 500000]

PriceRange = st.select_slider("Select Price Range", options=Price)

    
selected_index = selected_car[0].models.index(selected_model)
PriceIndex = next((i for i, price in enumerate(selected_car[0].price) if Price[i] <= PriceRange < Price[i + 1]), None)
if PriceIndex is not None:
    if PriceIndex == selected_index:
        st.write("## Car Details:")
        st.write(f"- Brand: {selected_car[0].brand}")
        st.write(f"- Model: {selected_model}")
        st.write(f"- Type: {selected_car[0].car_type}")
        st.write(f"- Price: {selected_car[0].price[selected_index]}")
        st.write("- Variants:", ", ".join(selected_car[0].variants[selected_index]))
        st.write(f"- Specs: {selected_car[0].specs[selected_index]}")
        st.write("- Similar Cars:", ", ".join(selected_car[0].similar_cars[selected_index]))

        if st.button('Buy car'):
            BUYCAR.buy_car(selected_model)
            st.write("Car Bought Successfully!")
            
    else:
        st.write("No cars in selected criteria.")
else:
     st.write("No cars  in price range.")


def write_dict_to_csv(data, filename):
    # Extract keys from the dictionary
    fieldnames = list(data.keys())

    # Write the dictionary to a CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header
        writer.writeheader()
        
        # Write data rows
        writer.writerow(data)

write_dict_to_csv(BUYCAR.bought_cars, "bought.csv")

la = {"username":"product is good"}
lb = {"username":"UI is not friendly"}
Review = st.text_input("Add review")
la["user"] = Review
complaint = st.text_input("Add complaint")
lb["user"] = complaint

