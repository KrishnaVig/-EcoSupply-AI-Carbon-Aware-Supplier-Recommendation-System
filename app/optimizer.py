from app.schemas import OptimizeRequest


def _total_unit_carbon(supplier: dict) -> float:
    return supplier["carbon_per_unit"] + supplier["transport_emission_per_unit"]


def run_optimizer(payload: OptimizeRequest, suppliers: list[dict]) -> dict:
    ranked_suppliers = sorted(
        suppliers,
        key=lambda supplier: (
            _total_unit_carbon(supplier),
            supplier["cost_per_unit"],
        ),
    )

    remaining_units = payload.quantity
    allocation: list[dict] = []

    for supplier in ranked_suppliers:
        if remaining_units == 0:
            break

        assigned_units = min(remaining_units, supplier["max_units"])
        remaining_units -= assigned_units
        unit_carbon = _total_unit_carbon(supplier)

        allocation.append(
            {
                "supplier": supplier["supplier"],
                "units": assigned_units,
                "unit_cost": supplier["cost_per_unit"],
                "unit_carbon": round(unit_carbon, 2),
                "total_cost": round(assigned_units * supplier["cost_per_unit"], 2),
                "total_carbon": round(assigned_units * unit_carbon, 2),
            }
        )

    if remaining_units > 0:
        raise ValueError("Not enough supplier capacity to fulfill the requested quantity.")

    total_cost = round(sum(item["total_cost"] for item in allocation), 2)
    total_carbon = round(sum(item["total_carbon"] for item in allocation), 2)

    if total_cost > payload.budget:
        raise ValueError("No hard-coded sample supplier mix fits within the given budget.")

    if total_carbon > payload.carbon_limit:
        raise ValueError("No hard-coded sample supplier mix fits within the given carbon limit.")

    baseline_supplier = min(suppliers, key=lambda supplier: supplier["cost_per_unit"])
    baseline_carbon = payload.quantity * _total_unit_carbon(baseline_supplier)
    carbon_savings = max(0.0, baseline_carbon - total_carbon)
    carbon_savings_percent = round((carbon_savings / baseline_carbon) * 100, 2) if baseline_carbon else 0.0

    recommended_supplier = min(allocation, key=lambda item: item["unit_carbon"])["supplier"]

    return {
        "project_name": payload.project_name,
        "material": payload.material,
        "recommended_supplier": recommended_supplier,
        "supplier_mix": allocation,
        "total_units": payload.quantity,
        "optimized_cost": total_cost,
        "optimized_carbon": total_carbon,
        "carbon_limit": payload.carbon_limit,
        "carbon_savings_percent": carbon_savings_percent,
        "budget_remaining": round(payload.budget - total_cost, 2),
        "recommendation": (
            f"Use {recommended_supplier} as the lowest-carbon lead supplier and blend suppliers "
            "only when capacity requires it."
        ),
    }
