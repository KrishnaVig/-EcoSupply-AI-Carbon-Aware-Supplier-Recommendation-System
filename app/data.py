MATERIALS = [
    {"id": 1, "material_name": "Steel"},
    {"id": 2, "material_name": "Cement"},
    {"id": 3, "material_name": "Insulation"},
]


SUPPLIERS = [
    {
        "id": 1,
        "supplier": "Supplier A",
        "material": "steel",
        "cost_per_unit": 48000,
        "carbon_per_unit": 3.2,
        "distance_km": 120,
        "transport_emission_per_unit": 0.25,
        "max_units": 70,
    },
    {
        "id": 2,
        "supplier": "Supplier B",
        "material": "steel",
        "cost_per_unit": 49000,
        "carbon_per_unit": 2.6,
        "distance_km": 80,
        "transport_emission_per_unit": 0.18,
        "max_units": 90,
    },
    {
        "id": 3,
        "supplier": "Supplier C",
        "material": "steel",
        "cost_per_unit": 46000,
        "carbon_per_unit": 2.9,
        "distance_km": 150,
        "transport_emission_per_unit": 0.28,
        "max_units": 110,
    },
    {
        "id": 4,
        "supplier": "Supplier D",
        "material": "cement",
        "cost_per_unit": 9000,
        "carbon_per_unit": 1.5,
        "distance_km": 55,
        "transport_emission_per_unit": 0.08,
        "max_units": 250,
    },
    {
        "id": 5,
        "supplier": "Supplier E",
        "material": "cement",
        "cost_per_unit": 8400,
        "carbon_per_unit": 1.9,
        "distance_km": 40,
        "transport_emission_per_unit": 0.06,
        "max_units": 320,
    },
    {
        "id": 6,
        "supplier": "Supplier F",
        "material": "insulation",
        "cost_per_unit": 12000,
        "carbon_per_unit": 0.9,
        "distance_km": 95,
        "transport_emission_per_unit": 0.04,
        "max_units": 180,
    },
]


SAMPLE_INPUT = {
    "project_name": "Metro Tower",
    "material": "steel",
    "quantity": 100,
    "budget": 5000000,
    "carbon_limit": 300,
}
