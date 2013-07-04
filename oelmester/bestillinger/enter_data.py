from bestillinger.bestil_system.models import Packing, Product, Client

def All():
    #Packing
    b=Packing(description="33 cl flaske", value=1.0)
    b.save()

    bp=Packing(description="25 cl flaske", value=1.0)
    bp.save()

    bs=Packing(description="150 cl flaske", value=3.0)
    bs.save()

    d=Packing(description="daase", value=1.0)
    d.save()

    ka=Packing(description="alm. kasse", value=12.5)
    ka.save()

    fu=Packing(description="fustage", value=160.0)
    fu.save()
    
    gf=Packing(description="gas flaske 4kg", value=160.0)
    gf.save()
    
    #Products
    Product(identifier="carls special",
            long_name="Carls Special, 33 cl.",
            bottle_type=b,
            bottle_number=30,
            box_type=ka,
            in_price=150.50,
            sell_price= 155.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="carlsberg",
            long_name="Carlsberg pilsner, 33 cl.",
            bottle_type=b,
            bottle_number=30,
            box_type=ka,
            in_price= 137.80,
            sell_price= 140.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="cola",
            long_name="Coca Cola, 25 cl.",
            bottle_type=bp,
            bottle_number=30,
            box_type=ka,
            in_price= 132.80,
            sell_price= 135.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="cola 150",
            long_name="Coca Cola, 150 cl.",
            bottle_type=bs,
            bottle_number=10,
            box_type=ka,
            in_price= 172.75,
            sell_price= 175.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="cola light",
            long_name="Coca Cola Light, 25 cl.",
            bottle_type=bp,
            bottle_number=30,
            box_type=ka,
            in_price= 132.80,
            sell_price= 135.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="cola light 150",
            long_name="Coca Cola Light, 150 cl.",
            bottle_type=bs,
            bottle_number=10,
            box_type=ka,
            in_price= 172.75,
            sell_price= 175.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="zero",
            long_name="Coca Cola Zero, 25 cl.",
            bottle_type=b,
            bottle_number=30,
            box_type=ka,
            in_price= 132.80,
            sell_price= 135.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="cocio",
            long_name="Cocio,24 cl.",
            bottle_type=bp,
            bottle_number=30,
            box_type=ka,
            in_price= 180.35,
            sell_price= 185.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="danskvand",
            long_name="Kurvand Naturel, 25 cl.",
            bottle_type=b,
            bottle_number=30,
            box_type=ka,
            in_price= 114.20,
            sell_price= 115.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="danskvand citrus",
            long_name="Kurvand Citrus, 25 cl.",
            bottle_type=bp,
            bottle_number=30,
            box_type=ka,
            in_price= 123.55,
            sell_price= 125.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="elephant",
            long_name="Elephant, 33 cl.",
            bottle_type=b,
            bottle_number=30,
            box_type=ka,
            in_price= 194.90,
            sell_price= 200.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="fanta",
            long_name="Fanta, 25 cl.",
            bottle_type=bp,
            bottle_number=30,
            box_type=ka,
            in_price= 132.80,
            sell_price= 135.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="fanta 150",
            long_name="Fanta, 150 cl.",
            bottle_type=bs,
            bottle_number=10,
            box_type=ka,
            in_price= 172.75,
            sell_price= 175.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="ginger",
            long_name="Schweppes Ginger Ale, 25 cl.",
            bottle_type=bp,
            bottle_number=30,
            box_type=ka,
            in_price= 140.55,
            sell_price= 145.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="julebryg",
            long_name="Julebryg, 33 cl.",
            bottle_type=b,
            bottle_number=30,
            box_type=ka,
            in_price= 181.40,
            sell_price= 185.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="lemon",
            long_name="Schweppes Lemon, 25 cl.",
            bottle_type=bp,
            bottle_number=30,
            box_type=ka,
            in_price= 140.55,
            sell_price= 145.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="lemon 150",
            long_name="Schweppes Lemon, 150 cl.",
            bottle_type=bs,
            bottle_number=10,
            box_type=ka,
            in_price= 182.80,
            sell_price= 185.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="paaskebryg",
            long_name="Paaskebryg, 33 cl.",
            bottle_type=b,
            bottle_number=30,
            box_type=ka,
            in_price= 181.40,
            sell_price= 185.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="somersby",
            long_name="Somersby, 33 cl.",
            bottle_type=d,
            bottle_number=45,
            #box_type=ka,
            in_price= 275.00,
            sell_price= 290.0,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="sprite",
            long_name="Sprite, 25 cl.",
            bottle_type=bp,
            bottle_number=30,
            box_type=ka,
            in_price= 132.80,
            sell_price= 135.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="sprite 150",
            long_name="Sprite, 150 cl.",
            bottle_type=bs,
            bottle_number=10,
            box_type=ka,
            in_price= 172.75,
            sell_price= 175.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="squash",
            long_name="Tuborg Squash, 25 cl.",
            bottle_type=bp,
            bottle_number=30,
            box_type=ka,
            in_price= 132.80,
            sell_price= 135.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="squash 150",
            long_name="Tuborg Squash, 150 cl.",
            bottle_type=bs,
            bottle_number=10,
            box_type=ka,
            in_price= 172.75,
            sell_price= 175.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="tonic",
            long_name="Schweppes Tonic, 25 cl.",
            bottle_type=bp,
            bottle_number=30,
            box_type=ka,
            in_price= 140.55,
            sell_price= 145.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="tonic 150",
            long_name="Schweppes Tonic, 150 cl.",
            bottle_type=bs,
            bottle_number=10,
            box_type=ka,
            in_price= 183.05,
            sell_price= 185.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="tuborg classic",
            long_name="Tuborg Classic, 33 cl.",
            bottle_type=b,
            bottle_number=30,
            box_type=ka,
            in_price= 150.50,
            sell_price= 155.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="tuborg guld",
            long_name="Tuborg Guld, 33 cl.",
            bottle_type=b,
            bottle_number=30,
            box_type=ka,
            in_price= 181.40,
            sell_price= 185.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="tuborg",
            long_name="Tuborg Pilsner, 33 cl.",
            bottle_type=b,
            bottle_number=30,
            box_type=ka,
            in_price=  137.80 ,
            sell_price= 140.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="tuborg 25l",
            long_name="Groen Tuborg 25l",
            bottle_type=fu,
            bottle_number=1,
            in_price=  433.85 ,
            sell_price= 435.00,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="tuborg classic 25l",
            long_name="Tuborg Classic 25l",
            bottle_type=fu,
            bottle_number=1,
            in_price=  482.45 ,
            sell_price=  485.00 ,
            num_stocked=0,
            num_ordered=0).save()
    Product(identifier="kulsyre 4kg",
            long_name="Kulsyre 4kg",
            bottle_type=gf,
            bottle_number=1,
            in_price=  198.75 ,
            sell_price=  200.00 ,
            num_stocked=0,
            num_ordered=0).save()
    
    #Clients

    Client(contact_person_1= "Lovisa Lansing",
           person_1_email ="lovisa.lansing@gmail.com",
           person_1_room ="3",
           person_1_phone = "50 41 78 77",
           name ="Stue Nord").save()

    Client(contact_person_1= "Philip Ulrich",
           person_1_email = "philipulrich@ofir.dk",
           person_1_room ="39",
           name ="1. Nord").save()

    Client(contact_person_1= "Thomas Friis Munksgaard",
           person_1_email = "thomasfriis@yahoo.com",
           person_1_room ="51",
           person_1_phone = "27401741",
           name ="2. Nord").save()

    Client(contact_person_1= "Anders Rudebeck",
           person_1_email = "",
           person_1_room ="",
           person_1_phone = "",
           name ="3. Nord").save()
