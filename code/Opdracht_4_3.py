phone_numbers = {
    "the Simpsons" : "636-555-3226",
    "Vegas Vacation": "555-0100",
    "Ghostbusters": "555-23678",
    "Billy Madison": "555-0840",
    "Swingers": "213-555-4679",
    "Bruce Almighty": "555-0123",
    "Seinfeld": "555-FILK",
    "Arrested Development": "555-0113",
    "Die Hard With a Vengeance": "555-0001",
    "The A-Team": "555-6162"
}
print(f"Het telefoonnummer van Bruce Almighty is {phone_numbers['Bruce Almighty']}.")
phone_numbers["Harry Potter"] = "605-475-6961"
print(f"Het telefoonnummer {phone_numbers["Ghostbusters"]} van de Ghostbusters is gewijzigd naar 555-2368.")
phone_numbers.update({"Ghostbusters": "555-2368"})

print(phone_numbers)

print(f"Telefoonnummer {phone_numbers["Seinfeld"]} van Seinfeld is verwijderd.")
phone_numbers.pop("Seinfeld")
print(f"In de dictionary zitten {len(phone_numbers)} telefoonnummers.")